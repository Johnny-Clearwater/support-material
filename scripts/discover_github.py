#!/usr/bin/env python3
"""Find under-the-radar 3D printing repos on GitHub.

Searches the GitHub repository search API for repos tagged with any of the
configured topics, pushed within the last N days, with fewer than MAX_STARS
stars. Results are de-duplicated and written to data/candidates.json.

Usage:
    GITHUB_TOKEN=ghp_... python3 scripts/discover_github.py [--days 14] [--max-stars 150]

Standard library only; no dependencies.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://api.github.com/search/repositories"
TOPICS = [
    "3d-printing",
    "3d-printer",
    "klipper",
    "reprap",
    "voron",
    "toolchanger",
    "non-planar",
]
PER_PAGE = 100
MAX_PAGES = 10  # search API returns at most 1000 results per query
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "candidates.json"


def request(url: str, token: str) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "support-material-discover",
        "Authorization": f"Bearer {token}",
    }
    for attempt in range(5):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")[:500]
            reset = e.headers.get("X-RateLimit-Reset")
            retry_after = e.headers.get("Retry-After")
            rate_limited = e.code == 429 or (
                e.code == 403
                and (retry_after or e.headers.get("X-RateLimit-Remaining") == "0"
                     or "rate limit" in body.lower())
            )
            # Primary or secondary rate limit: wait and retry.
            if rate_limited:
                if retry_after:
                    wait = int(retry_after)
                elif reset and e.headers.get("X-RateLimit-Remaining") == "0":
                    wait = max(int(reset) - int(time.time()), 1)
                else:
                    wait = 2 ** (attempt + 2)
                print(f"  rate limited, sleeping {wait}s", file=sys.stderr)
                time.sleep(min(wait, 120))
                continue
            if e.code == 422:  # e.g. paging past the 1000-result cap
                return {"items": []}
            raise SystemExit(f"GitHub API error {e.code} for {url}: {body}")
        except urllib.error.URLError as e:
            wait = 2 ** (attempt + 1)
            print(f"  network error ({e.reason}), retrying in {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise SystemExit(f"Giving up on {url}")


def search_topic(topic: str, since: str, max_stars: int, token: str) -> list[dict]:
    q = f"topic:{topic} pushed:>={since} stars:<{max_stars} archived:false fork:false"
    items: list[dict] = []
    for page in range(1, MAX_PAGES + 1):
        params = urllib.parse.urlencode(
            {"q": q, "sort": "updated", "order": "desc", "per_page": PER_PAGE, "page": page}
        )
        data = request(f"{API}?{params}", token)
        batch = data.get("items", [])
        items.extend(batch)
        if page == 1:
            print(f"  topic:{topic} -> {data.get('total_count', 0)} results", file=sys.stderr)
        if len(batch) < PER_PAGE:
            break
        time.sleep(2)  # stay well under 30 search requests/minute
    return items


def slim(repo: dict) -> dict:
    lic = repo.get("license") or {}
    return {
        "full_name": repo["full_name"],
        "url": repo["html_url"],
        "description": repo.get("description"),
        "homepage": repo.get("homepage") or None,
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "open_issues": repo.get("open_issues_count", 0),
        "language": repo.get("language"),
        "license": lic.get("spdx_id"),
        "topics": repo.get("topics", []),
        "created_at": repo.get("created_at"),
        "pushed_at": repo.get("pushed_at"),
        "owner": repo["owner"]["login"],
        "matched_topics": [],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--days", type=int, default=14, help="pushed within this many days (default 14)")
    ap.add_argument("--max-stars", type=int, default=150, help="exclusive star ceiling (default 150)")
    ap.add_argument("--out", type=Path, default=OUT, help=f"output path (default {OUT.relative_to(ROOT)})")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN is not set.", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc)
    since = (now - timedelta(days=args.days)).strftime("%Y-%m-%d")
    print(f"Searching repos pushed since {since}, < {args.max_stars} stars", file=sys.stderr)

    found: dict[str, dict] = {}
    for i, topic in enumerate(TOPICS):
        if i:
            time.sleep(2)
        for repo in search_topic(topic, since, args.max_stars, token):
            entry = found.setdefault(repo["full_name"].lower(), slim(repo))
            if topic not in entry["matched_topics"]:
                entry["matched_topics"].append(topic)

    candidates = sorted(found.values(), key=lambda r: r["pushed_at"] or "", reverse=True)
    out = {
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "criteria": {"topics": TOPICS, "pushed_since": since, "max_stars_exclusive": args.max_stars},
        "count": len(candidates),
        "candidates": candidates,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} candidates to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
