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

<!-- TODO: the editorial rules were not included in the setup request. Paste them here. -->
