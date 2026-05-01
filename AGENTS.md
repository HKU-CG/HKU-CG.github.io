# Agent Guidelines for HKU-CG.github.io

## Project Overview

This is the **HKU Computer Graphics Lab (CGVU)** group website, built with [Hugo](https://gohugo.io/) + [Wowchemy](https://wowchemy.com/) (formerly Academic).

- **Live site**: https://hku-cg.github.io
- **Framework**: Hugo static site generator (v0.128.0 in CI, v0.161.0+ locally)
- **Theme**: Wowchemy via Hugo Modules (`go.mod`)
- **Deployment**: GitHub Actions → GitHub Pages

## Key Technology Details

- **No git submodules**: Despite the presence of `.gitmodules`, the theme is managed via **Hugo Modules** (`go.mod`). The `.gitmodules` file is a legacy artifact and can be ignored.
- **Go is required**: Hugo needs the `go` binary to download Wowchemy modules on first build.
- **Content format**: Most content uses YAML front matter (`---`) or TOML (`+++`).
- **Avatar naming**: Author avatars **must** be named exactly `avatar.jpg` or `avatar.png`.

## Directory Structure

```
├── config/_default/        # Site config (params.toml, menus.toml, languages.toml)
├── content/
│   ├── authors/            # One folder per person (e.g., Wenjia-Wang/)
│   │   ├── admin/          # Lab PI / homepage profile
│   │   └── <name>/
│   │       ├── _index.md   # Profile metadata
│   │       └── avatar.jpg  # Profile photo (required name)
│   ├── People/             # People page widgets
│   ├── publication/        # One folder per paper
│   ├── talk/               # News / events
│   └── home/               # Homepage widgets
├── static/media/           # General images referenced in content
├── assets/images/          # Logo, icon, favicon
├── layouts/                # Custom HTML templates (override theme)
└── .github/workflows/      # CI/CD (hugo.yml)
```

## Content Editing Conventions

### Adding a Person

**Preferred workflow** — give the script a homepage URL and let it scaffold everything:

```bash
python3 scripts/add_member.py <homepage_url> --name "First Last" --group "Graduate Students" --start 202409
```

The script will:
1. Scrape the page for name, photo, email, affiliation, and interests.
2. Create `content/authors/<First-Last>/`.
3. Write `_index.md` pre-filled with extracted data.
4. Download the avatar image (if detectable on the page).

**Then manually review** the generated `_index.md` and fill in missing links (GitHub, Google Scholar, personal page, etc.).

**Critical fields** (check these after generation):
- `title`: Display name
- `weight`: Start year-month for students (e.g., `202301`). For alumni, use **negative** graduation date (e.g., `-202307`).
- `user_groups`: Must be exactly one of:
  - `Principal Investigator`
  - `Research Staff`
  - `Graduate Students`
  - `Research Assistant`
  - `Undergraduate Students`
  - `Postdoctoral Alumni`
  - `PhD Alumni`
  - `Masters Alumni`
  - `MPhil Alumni`
  - `Undergraduate Alumni`
  - `RA Alumni`
- Avatar file **must** be named `avatar.jpg` or `avatar.png`.

**Manual fallback** (if the URL doesn't work):
1. Create `content/authors/<Firstname-Lastname>/`
2. Copy `_index.md` from an existing person and modify.
3. Add the avatar image manually.

### Author Profile Maintenance

#### Google Scholar Links

Most personal academic homepages list a Google Scholar link. The fastest way to find it is to scrape the raw HTML:

```bash
curl -s -L -A "Mozilla/5.0" <homepage_url> | grep -oiE "scholar\.google\.com/[^\"'<> ]+"
```

If multiple links appear, the one with `authuser=1` or the first occurrence is usually the profile owner's.

Add the extracted link to the author's `_index.md` under `social:` with:
```yaml
- icon: google-scholar
  icon_pack: ai
  link: https://scholar.google.com/citations?user=XXXXXX
```

**Note:** Do **not** use `google-scholar` icon for personal homepages — use `user-graduate` (fas) instead.

#### Social Icon Order

All author `social:` lists **must** follow this exact order:

1. `home` (personal homepage)
2. `google-scholar`
3. `github`
4. `envelope` (email)
5. Everything else (`orcid`, `university-logo`, `cv`, `linkedin`, `twitter`, etc.)

**Rules:**
- Only reorder icons that already exist. **Never guess or add missing links** (especially HKU emails).
- If an icon is missing, skip its position and continue with the next available icon.
- Do **not** leave `personal_homepage` as a separate field if the author also has a `home` icon in `social:` — the `home` icon in `social:` is sufficient.

#### Avatar Images

- Avatars **must** be named exactly `avatar.jpg` or `avatar.png`.
- If downloading from a personal page fails due to Cloudflare / bot protection, try using the Kimi image-proxy URL (visible via `FetchURL`), or ask the user for a direct link / file upload.
- After any image download, verify with:
  ```bash
  python3 -c "from PIL import Image; img = Image.open('path'); img.verify(); print(img.size)"
  ```

### Adding a Publication

1. Create `content/publication/<YYYY-Venue-Title>/`
2. Create `index.md` with front matter and abstract.
3. Add `featured.jpg`/`featured.png` as thumbnail.
   - **Primary source**: author's personal homepage (`/img/<project>.png` or similar). **Do NOT use arXiv** as the first choice.
4. Update `content/talk/` news to include the new paper.
5. The `publications.bib` at repo root is **not** auto-synced to the site; it's a backup reference file.

### Moving Someone to Alumni

- Change `user_groups` to the appropriate `* Alumni` category.
- **Change `weight` to negative graduation year-month** (e.g., `-202406`). This ensures correct reverse-chronological ordering on the alumni page.
- Update `role` to include the date range (e.g., `MPhil, Sept. 2022 - Jun. 2024.`).

### Homepage & People Page

- `content/authors/admin/_index.md` controls the lab intro text on the homepage.
- `content/People/alumni.md` defines which alumni groups are displayed and their order.
- `content/People/people.md` defines the current members display.

## Local Development

### Prerequisites

```bash
# macOS
brew install hugo go
```

### Run Locally

```bash
bash view.sh
# or directly:
hugo server --baseURL http://localhost:1313/ --disableFastRender --printI18nWarnings
```

Site will be at **http://localhost:1313/**.

### Build (dry-run)

```bash
hugo
```

Output goes to `public/` (gitignored).

## Common Pitfalls

- **Do not use `--i18n-warnings`** with Hugo ≥ 0.160. It was renamed to `--printI18nWarnings`.
- **Deprecated config**: `languages.en.languageCode` is deprecated in Hugo 0.158+. Use `languages.en.locale` instead.
- **Missing avatar**: If an author has no `avatar.jpg/png`, their profile shows a blank placeholder.
- **YAML indentation**: All `.md` front matter is YAML. Be strict with 2-space indentation.
- **Special characters in tags**: Tags with `.`, `?`, or non-alphanumeric characters can break the site build. Keep tags simple.

## People Widget Layout

To keep author cards aligned (same height, icons at bottom), the following CSS is injected in `layouts/partials/site_head.html`:

```css
.people-widget { display: flex; flex-wrap: wrap; }
.people-person {
  display: flex; flex-direction: column; align-items: center;
}
.people-person .portrait-title {
  display: flex; flex-direction: column; align-items: center;
  flex-grow: 1; width: 100%;
}
.people-person .people-interests { flex-grow: 1; text-align: center; }
.people-person .network-icon { margin-top: auto; }
```

Do **not** add per-widget `<style>` tags in partials — they may not render. Use the global `<style>` block in `site_head.html` instead.

## Change Safety

- **Do NOT push without explicit user instruction.** Wait for the user to say "push" or similar before committing and pushing changes.
- Do **not** force-push (`git push -f`) to this repo.
- After pushing, check the GitHub Actions tab for green ✅ / red ❌ on the commit.
- Deployment takes a few minutes after CI succeeds.
- Do not delete or rename existing author folders unless updating all publication `authors:` fields that reference them.
