#!/usr/bin/env python3
"""
Auto-generate a lab member profile from a personal homepage URL.
Usage:
    python scripts/add_member.py <homepage_url> [--name "First Last"] [--group "Graduate Students"] [--start 202409]

The script will:
1. Scrape the page for name, photo, affiliation, email, interests, etc.
2. Create content/authors/<First-Last>/
3. Write _index.md and download avatar.jpg/avatar.png
"""

import argparse
import os
import re
import sys
import urllib.request
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

# Try to import bs4; fallback to regex-only if not installed
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except Exception:
    HAS_BS4 = False


def slugify(name: str) -> str:
    return "-".join(re.sub(r"[^\w\s-]", "", name).strip().split())


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def download_image(img_url: str, out_dir: Path, filename: str = "avatar") -> Optional[Path]:
    try:
        req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "").lower()
            if "png" in ctype or data[:8] == b"\x89PNG\r\n\x1a\n":
                ext = "png"
            else:
                ext = "jpg"
            out_path = out_dir / f"{filename}.{ext}"
            out_path.write_bytes(data)
            return out_path
    except Exception as e:
        print(f"[warn] Failed to download image {img_url}: {e}")
        return None


def extract_meta(html: str, base_url: str) -> dict:
    info = {
        "name": None,
        "photo": None,
        "email": None,
        "affiliation": None,
        "interests": [],
        "role": None,
    }

    if HAS_BS4:
        soup = BeautifulSoup(html, "html.parser")

        # Open Graph / meta tags
        def meta(prop):
            tag = soup.find("meta", property=prop) or soup.find("meta", attrs={"name": prop})
            return tag["content"].strip() if tag and tag.get("content") else None

        info["name"] = meta("og:title") or meta("twitter:title") or meta("title")
        info["photo"] = meta("og:image") or meta("twitter:image")
        desc = meta("og:description") or meta("description") or meta("twitter:description")

        # Try to parse email from page text
        text = soup.get_text(separator=" ", strip=True)
        emails = re.findall(r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}", text)
        if emails:
            info["email"] = emails[0]

        # Try to infer affiliation from description
        if desc:
            # simple heuristics
            for keyword in ["University", "College", "Institute", "Lab", "School"]:
                if keyword in desc:
                    # grab a short phrase around the keyword
                    m = re.search(r"[^.\n]{0,40}" + re.escape(keyword) + r"[^.\n]{0,40}", desc)
                    if m:
                        info["affiliation"] = m.group(0).strip()
                        break

        # If no OG photo, look for <img> near header/h1 with alt containing "photo", "avatar", "profile"
        if not info["photo"]:
            for img in soup.find_all("img"):
                alt = (img.get("alt", "") + " " + img.get("class", [""])[0] if isinstance(img.get("class"), list) else "").lower()
                src = img.get("src") or img.get("data-src")
                if src and any(k in alt for k in ("photo", "avatar", "profile", "portrait", "head")):
                    info["photo"] = urljoin(base_url, src)
                    break
            # fallback: first reasonably-sized img
            if not info["photo"]:
                for img in soup.find_all("img"):
                    src = img.get("src") or img.get("data-src")
                    if src:
                        w = img.get("width", "")
                        if w and int(w) >= 80:
                            info["photo"] = urljoin(base_url, src)
                            break

        # Try to find interests / research keywords
        if desc:
            # Simple keyword extraction from description
            keywords = ["Animation", "Graphics", "Vision", "Robotics", "Simulation",
                        "Machine Learning", "Deep Learning", "Rendering", "Geometry",
                        "Motion", "Character", "Virtual Reality", "AR", "VR",
                        "Human", "Interaction", "AI", "Physics", "Modeling"]
            found = [k for k in keywords if k.lower() in desc.lower()]
            info["interests"] = found[:3]
    else:
        # Regex-only fallback
        m = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']+)', html)
        info["name"] = m.group(1) if m else None
        m = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']+)', html)
        info["photo"] = m.group(1) if m else None
        emails = re.findall(r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}", html)
        if emails:
            info["email"] = emails[0]

    return info


INDEX_TEMPLATE = """---
# Display name
title: {name}

# Username (this should match the folder name)
authors:
- {slug}

#Author Names (alternative spellings etc)
names:
- {name}

# This decides the order of people,
# set it as your start year&month (e.g., 202301)
weight: {weight}

# Is this the primary user of the site?
superuser: false

# Role/position
role: {role}

university: {affiliation}

department:
- Computer Science

# Organizations/Affiliations
organizations:
- name: {affiliation}

# Short bio (displayed in user profile at end of posts)
# bio:

interests:
{interests_yaml}

# Social/Academic Networking
# For available icons, see: https://sourcethemes.com/academic/docs/page-builder/#icons
social:
# - icon: envelope
#   icon_pack: fas
#   link: 'mailto:{email}'
# - icon: twitter
#   icon_pack: fab
#   link:
# - icon: google-scholar
#   icon_pack: ai
#   link:
- icon: github
  icon_pack: fab
  link:

# Enter email to display Gravatar (if Gravatar enabled in Config)
email: "{email}"

# Organizational groups that you belong to (for People widget)
user_groups:
- {user_group}

#any user groups to display on the page
display_groups:

---

<!-- # write your biography here -->
"""


def main():
    parser = argparse.ArgumentParser(description="Add a lab member from their homepage")
    parser.add_argument("url", help="Personal homepage URL")
    parser.add_argument("--name", help="Full name (auto-detected if omitted)")
    parser.add_argument("--group", default="Graduate Students",
                        help="User group (e.g., 'Graduate Students', 'PhD Alumni')")
    parser.add_argument("--start", default="202401", help="Start year-month or negative grad date for alumni")
    parser.add_argument("--role", default="", help="Role description")
    args = parser.parse_args()

    print(f"[info] Fetching {args.url} ...")
    html = fetch(args.url)
    meta = extract_meta(html, args.url)

    name = args.name or meta.get("name")
    if not name:
        print("[error] Could not detect name. Please provide --name.")
        sys.exit(1)

    # Clean up name (remove site titles like "| Home" etc.)
    name = re.split(r"[|\-–—]", name)[0].strip()
    slug = slugify(name)
    author_dir = Path("content/authors") / slug
    author_dir.mkdir(parents=True, exist_ok=True)

    # Photo
    photo_path = None
    if meta.get("photo"):
        full_photo_url = urljoin(args.url, meta["photo"])
        print(f"[info] Downloading photo from {full_photo_url} ...")
        photo_path = download_image(full_photo_url, author_dir)
        if photo_path:
            print(f"[ok] Saved photo to {photo_path}")

    # Build YAML interests
    interests = meta.get("interests") or []
    interests_yaml = "\n".join(f"- {i}" for i in interests) if interests else "# - Example Interest"

    # Affiliation fallback
    affiliation = meta.get("affiliation") or "University of Hong Kong"

    # Role fallback
    role = args.role or f"{args.group.rstrip('s')}, since {args.start[:4]}."

    content = INDEX_TEMPLATE.format(
        name=name,
        slug=slug,
        weight=args.start,
        role=role,
        affiliation=affiliation,
        interests_yaml=interests_yaml,
        email=meta.get("email") or "",
        user_group=args.group,
    )

    index_path = author_dir / "_index.md"
    index_path.write_text(content, encoding="utf-8")
    print(f"[ok] Created {index_path}")

    print(f"\n[next steps]")
    print(f"  1. Open {index_path} and fill in missing fields (GitHub, Google Scholar, bio, etc.)")
    if not photo_path:
        print(f"  2. Add an avatar manually: {author_dir}/avatar.jpg or avatar.png")
    else:
        print(f"  2. Verify the downloaded avatar looks correct.")
    print(f"  3. Run 'bash view.sh' and check the People page.")


if __name__ == "__main__":
    main()
