# Agent Guidelines for HKU-CG.github.io

## Project Overview

This is the **HKU Computer Graphics Lab (CGVU)** group website, built with [Hugo](https://gohugo.io/) + [Wowchemy](https://wowchemy.com/) (formerly Academic).

- **Live site**: https://hku-cg.github.io
- **Framework**: Hugo static site generator (v0.128.0 in CI, v0.161.0+ locally)
- **Theme**: Wowchemy via Hugo Modules (`go.mod`)
- **Deployment**: GitHub Actions → GitHub Pages

## Agent Session Principles

These are high-level rules to minimize context loss across sessions.

### 1. Always check `git status` first
Before editing anything, run `git status` to see if there are uncommitted changes left by previous sessions. Do not blindly stage and commit — understand what you are about to push.

### 2. The site is English-only
All user-visible content (lab intro, publication abstracts, news, people profiles) must be in **English**. Do not write Chinese into any `.md` file under `content/`.

### 3. Distinguish "Lab intro" from "PI profile"
- `content/authors/admin/_index.md` = **Lab-wide** intro + recruitment info.
- `content/authors/Taku-Komura/_index.md` = **Personal** PI profile.
Do not mix the two. Update the lab intro when the user asks about "our research" or "website description"; update the PI profile only when asked about Taku's personal page.

### 4. Commit scope awareness
When the user says "push", the working tree may contain changes from previous sessions. Make sure the commit message describes **all** staged changes, not just the file you touched last. If unrelated changes exist, ask the user whether to include them or stash them.

### 5. The user often dictates via voice input in Chinese
- Expect homophones and near-homophone typos (e.g., "NUS" → "news").
- Expect **Chinese-English mixed input**: professional terms are usually spoken in English while the rest is in Chinese (e.g., "中oral" means "中 [了] Oral", "pub" means "publication").
- Do not over-analyze literal spellings. Infer the intended meaning from **context**.
- If still ambiguous after 1–2 seconds of thought, **ask a single concise clarifying question** rather than debating internally.

### 6. Keep AGENTS.md focused on "cross-session memory"
Only add rules that future sessions need to remember (conventions, constraints, current contact lists). Do not add step-by-step tutorials that are already in `README.md`.

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
4. **Update `content/talk/` news** to include the new paper. A publication is **not complete** until the corresponding news entry exists.
5. The `publications.bib` at repo root is **not** auto-synced to the site; it's a backup reference file.

#### Oral / Award Annotations

When a paper receives special recognition, append it in parentheses after the venue in the `publication:` field:

- Oral: `'CVPR 2025 (Oral)'`
- Highlight: `'NeurIPS 2025 (Highlight)'`
- Spotlight: `'ICLR 2025 (Spotlight)'`
- Best Paper Candidate: `'CVPR 2026 (Oral, Best Paper Candidate)'`

**Rules:**
- Always wrap special awards in parentheses.
- Do **not** write `'ICCV 2021 Oral'` (without parentheses) — fix legacy entries to the parenthesized form.
- Only include awards that are officially announced by the venue (Oral, Highlight, Spotlight, Best Paper, Best Paper Candidate). Do not invent categories.

#### Conference Acceptance Timeline (for date sorting)

When multiple papers share the same year, set `date` according to the **approximate acceptance-notification month** so that newer results appear first in `ByDate.Reverse` order. Use the table below as a reference.

| Area | Venue | Accept. (approx.) | Suggested `date` |
|------|-------|-------------------|------------------|
| **ML** | ICLR | Jan–Mar | `YYYY-03-01` |
| | ICML | Apr | `YYYY-04-01` |
| | NeurIPS | Sep | `YYYY-09-01` |
| **CV** | CVPR | Feb–Mar | `YYYY-03-01` |
| | ICCV | Jun–Jul | `YYYY-07-01` |
| | ECCV | Jun–Jul | `YYYY-07-01` |
| | 3DV | Nov | `YYYY-11-01` |
| **CG** | SIGGRAPH | Mar–Apr | `YYYY-04-01` |
| | SIGGRAPH Asia | Jul–Aug | `YYYY-08-01` |
| | Eurographics | Dec–Jan | `YYYY-01-01` |
| | SGP | Mar / May | `YYYY-03-01` or `YYYY-05-01` |
| | IEEE VIS | Jun–Jul | `YYYY-07-01` |
| | SCA | May | `YYYY-05-01` |
| **Robotics** | RSS | Apr–May | `YYYY-05-01` |
| | ICRA | Jan–Feb | `YYYY-02-01` |
| | IROS | Jun–Jul | `YYYY-07-01` |
| | CoRL | Aug–Sep | `YYYY-09-01` |
| **AI/NLP** | AAAI | Nov | `YYYY-11-01` |
| | IJCAI | Apr | `YYYY-04-01` |
| | ACL | May | `YYYY-05-01` |
| | EMNLP | Aug | `YYYY-08-01` |

**Rules:**
- If a venue is not listed, use its actual acceptance month.
- Preprints / arXiv papers should use the **first public release month** (or keep `YYYY-01-01` if unknown).
- Journal-only papers (e.g., pure TOG without SIGGRAPH presentation) can use `YYYY-01-01` or the official publication month.

### Moving Someone to Alumni

- Change `user_groups` to the appropriate `* Alumni` category.
- **Change `weight` to negative graduation year-month** (e.g., `-202406`). This ensures correct reverse-chronological ordering on the alumni page.
- Update `role` to include the date range (e.g., `MPhil, Sept. 2022 - Jun. 2024.`).

### Homepage & People Page

- `content/authors/admin/_index.md` controls the lab intro text on the homepage.
- `content/People/alumni.md` defines which alumni groups are displayed and their order.
- `content/People/people.md` defines the current members display.
- Publication dates follow the **Conference Acceptance Timeline** (see table above). This controls reverse-chronological ordering on the site.

#### Lab Intro & Recruitment

- `content/authors/admin/_index.md` controls **both** the lab intro text **and** the recruitment section on the homepage.
- **Research directions**: Use broad domains (e.g., *physical simulation*, *humanoid robotics*, *3D vision*) rather than narrow technical keywords. Do not copy-paste from old descriptions like "physically-based animation and the application of machine learning techniques for animation synthesis" without checking recent publications.
- **Recruitment contacts**: If adding/changing contact emails for MPhil / PhD / RA / collaboration inquiries, append them to the same paragraph. Current contacts:
  - `taku@cs.hku.hk`
  - `wwj2022@connect.hku.hk`
  - `zliao@connect.hku.hk`
  - `kmhuang@connect.hku.hk`
- **Copy style**: Avoid repetitive "or" lists (e.g., "A, or B, or C"). Prefer: "Please feel free to reach out to any of us: ..." or "Please contact us at the following emails: ..."

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

`view.sh` supports custom ports via the `PORT` or `port` environment variable (default is `1313`):

```bash
PORT=3000 bash view.sh
port=3000 bash view.sh
```

Site will be at **http://localhost:1313/** by default.

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

- **Strict rule: ONLY push when the user explicitly says "push" or similar.** Do not push automatically after every commit. Wait for an explicit instruction.
- **Before pushing, always check the remote first:** run `git fetch` and `git pull` to merge any remote changes. Do **not** force-push (`git push -f`) to this repo.
- After pushing, check the GitHub Actions tab for green ✅ / red ❌ on the commit.
- Deployment takes a few minutes after CI succeeds.
- Do not delete or rename existing author folders unless updating all publication `authors:` fields that reference them.
