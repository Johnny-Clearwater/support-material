# Support Material

A biweekly newsletter of under-the-radar open-source 3D printing projects.
Slogan: **"Small projects, big overhangs."**

## Repo layout

- `hugo.toml`: site config (title, slogan, menus, privacy settings)
- `themes/support-material/`: the custom theme (layouts, `assets/css/main.css`)
- `content/issues/NNN-slug.md`: one file per issue, e.g. `001-first-layer.md`
- `content/about.md`: the About page
- `scripts/discover_github.py`: finds candidate repos and writes `data/candidates.json`
- `sites.txt`: other sources to check by hand
- `.github/workflows/deploy.yml`: builds with Hugo and deploys to GitHub Pages on push to `main`

## Issue front matter

```yaml
---
title: "Issue title"
issue: 1             # integer; shown as #001
date: 2026-11-14
summary: "One sentence, shown on the homepage and in RSS."
---
```

Start a new issue with `hugo new content issues/NNN-slug.md` (the draft is set to `draft: true`).

## Workflow

1. `GITHUB_TOKEN=... python3 scripts/discover_github.py` (options: `--days`, `--max-stars`)
2. Review `data/candidates.json` and the sources in `sites.txt`
3. Write the issue in `content/issues/` and preview it with `hugo server -D`
4. Push to `main` to publish

## Site constraints

- No trackers, analytics, cookies or third-party embeds. Do not add any.
- No external fonts, scripts or CDNs. The theme is self-contained.

## Editorial rules

Every issue follows `content/issues/000-pilot.md` as the reference format.

**Structure**
- One **Deep cut**: a long write-up of a single project.
- **Quick finds**: 4–5 short picks.
- **Tooling corner**: 3 tooling picks.
- **From the bench**: leave a placeholder for Johnny to fill in. Never write bench results yourself.
- Then the sign-off, house rules and sources.

**Credit and licensing**
- Credit every maker by name and link to their own page (repo, project page or profile).
- Note each project's license. If none is stated, say so and tell readers to check before remixing.

**Images**
- Never re-host makers' photos. Link to them instead.

**Safety**
- Never include weapon-related projects, from any source.
- Never reproduce hazardous chemistry (etchants, reactive inks and the like). Point to the maker's own logs and add a safety note.

**Eligibility**
- Skip any project that appears on the coverage-check list in `sites.txt` (section 3): 2+ hits means skip, and 1 small or regional hit is the editor's call. Never scan the sites in section 4.
- Stay within a two-week window: projects must have been created, released or updated in the 14 days before the issue date. (Issue #0 relaxed this once, for the pilot only.)

**sites.txt upkeep**
- Each issue, scan the ACTIVE list and try 2–3 sites from TO TRY. Then update the file: last-scanned dates, yield ratings, promotions and demotions, and a LOG entry listing picks and rejections with the reason for each.
