# Joint Lab Maintenance

The Miro Dynamics - HKU CGVU Joint Lab is rendered by
`layouts/partials/widgets/joint_lab.html` on the standalone `/mirod-lab/`
page. The section is data-driven: any author profile with `joint_lab_role` is
included automatically. The Home and People pages do not render a separate
Joint Lab block. Home places selected Joint Lab members into the regular Main
Lab display groups and adds a short affiliation link below their names.
Keep the complete Joint Lab member markup in the shared partial and do not
duplicate it in the Home or People widgets.

## Joint Lab publications

Publication membership is explicit and must be provided by the lab owner. Add
this field only to an article that should belong to Joint Lab:

```yaml
joint_lab: true
```

The Main Lab publication page continues to show all articles. A publication
with `joint_lab: true` is additionally shown on `/mirod-lab/`; an unmarked
article remains Main Lab-only. Do not infer this flag from the article authors'
Joint Lab roles or research interests. Until articles are explicitly marked,
the Joint Lab Publications section remains empty.

## Main Lab and Joint Lab

The two sections share author profiles, verified links, and portraits, but they
are maintained independently:

- **Main Lab membership** on the People page comes from the
  `content.user_groups` list in `content/People/people.md`, together with each
  profile's `user_groups` field. Main Lab cards use the profile's standard
  fields, including `role`, `interests`, and `social`.
- **Home display placement** may use `home_display_group` for a Joint Lab
  member who is not in a Main Lab `user_groups` value. This is a visual Home
  placement field, not a membership claim. Its value must match one of the
  labels in `content/home/people.md`.
- **People display placement** may use `people_display_group` for an external
  Joint Lab collaborator who should be visible in the full directory. This is
  also a visual placement field, not a Main Lab membership claim. Its value
  must match one of the labels in `content/People/people.md`.
- **Joint Lab membership** is controlled only by the presence of
  `joint_lab_role` in an author profile. Its grouping, order, identity, and
  short research line come from `joint_lab_role`, `joint_lab_order`,
  `joint_lab_identity`, and `joint_lab_intro` respectively.
- `joint_lab_intro` takes precedence over `interests` on the Joint Lab card.
  When a research-direction change should appear in both sections, update the
  profile's `interests` and its `joint_lab_intro` together.
- A Joint Lab member may be an external collaborator and does not need to be a
  Main Lab member or an HKU student. Adding or removing a Joint Lab role should
  not by itself change `user_groups` or move the person to an alumni group. If
  someone genuinely belongs to both labs, keep their Main Lab `user_groups`
  entry and Joint Lab fields. External-only collaborators keep `user_groups`
  empty and use `home_display_group` and/or `people_display_group` when they
  should also appear in those visual directories.
- The Joint Lab is rendered only by `layouts/mirod_lab/single.html` through
  `layouts/partials/widgets/joint_lab.html`. Main Lab alumni rules apply to
  the People page; Joint Lab role assignments are maintained independently.

## Member fields

Add these fields to the member's `content/authors/<Name>/_index.md`:

```yaml
joint_lab_role: RA
joint_lab_order: 1
joint_lab_identity: RA
joint_lab_intro: Computer Vision, Embodied AI
home_display_group: Research Assistant
people_display_group: Research Assistant
```

- `joint_lab_role` controls the section. Use `Lead`, `RA`, `PhD`, `MPhil`, or
  `JuniorRA`. `PhD` and `MPhil` are displayed together as `Graduate Students`.
- `joint_lab_order` controls the order within a section. Use consecutive values
  starting at `1`.
- `joint_lab_identity` is an optional personal identity line shown below the
  name. Use it for information that adds context, such as `RA`, `PhD student`,
  `MSc 3rd year, ShanghaiTech University`, or `Undergraduate 3rd year,
  Sichuan Agricultural University`. For graduates, include the degree and
  year, such as `B.S. graduate, Zhejiang University (2026)`. Use the full
  position name, such as `Research Assistant`, when clarity is more important
  than avoiding a repeated section label.
- `joint_lab_intro` is the short research-interest line shown below the identity.
  If it is absent, the card uses the profile's `interests` list. Keep it concise;
  use `Embodied AI` when no more specific direction is available.
- `home_display_group` is optional. Set it only when the member should appear
  on Home under a Main Lab-style group. For junior members use the exact value
  `Junior Research Assistant`.
- `people_display_group` is optional. Set it for an external Joint Lab
  collaborator who should appear in the full People directory. It does not add
  the person to Main Lab `user_groups`.
- People and Home show the affiliation link for Joint Lab members by default
  when those profiles are displayed. Set `hide_joint_lab_affiliation: true` for
  a lab-level leader whose Main Lab role already establishes the relationship,
  such as Taku Komura.

For dated identities, keep the same wording in `role` and `joint_lab_identity`
when the date should be visible on both the profile and the card. For example,
an upcoming intake can use `MPhil, Jan. 2027 -`; after enrollment, update it to
the site's established `since` wording. Leadership identities can be specific
to the person, such as `Joint Lab Director` and `Research Lead`.

The section labels are fixed in the template:

| Field | Display label |
| --- | --- |
| `Lead` | Joint Lab Leadership |
| `RA` | Research Assistant |
| `PhD` / `MPhil` | Graduate Students |
| `JuniorRA` | Junior Research Assistant |

## Links and portraits

Put verified links in the profile's `social` list. The Joint Lab uses the same
`social_links_plus_university` partial as the Main Lab, so each icon is a real
hyperlink. Keep this order when the links exist:

1. `home`
2. `google-scholar`
3. `github`
4. `envelope`
5. Other verified links

Use the actual personal homepage and Scholar profile; do not infer Scholar IDs.
Author portraits must be named `avatar.jpg` or `avatar.png` in the author folder.
If no verified portrait is available, keep the standard placeholder rather than
using an unrelated avatar or an autogenerated account icon.
The four recruitment contacts intentionally omit envelope icons; their
obfuscated public addresses are maintained in `content/authors/admin/_index.md`.

## Layout behavior

- `/mirod-lab/` is the only page with the full Joint Lab section and its empty
  Publications area.
- Home currently shows a compact Principal Investigator preview with links to
  the full `/people/` directory and the `/mirod-lab/` page. If Home is later
  expanded with `home_display_group`, profiles with `joint_lab_role` receive
  the `Affiliated with Mirod Joint Lab` link below their name by default;
  profiles with `hide_joint_lab_affiliation: true` are intentionally omitted.
- The People page shows the same affiliation link for current Main Lab members
  who also have a Joint Lab role, and for external Joint Lab collaborators with
  `people_display_group`. The latter remain outside Main Lab `user_groups`.
- The People/About page has no standalone Joint Lab block.
- The Joint Lab page uses four columns on desktop, two columns at tablet/mobile
  widths, and one column below 480px. Smaller groups are centered using the
  count-specific classes in `layouts/partials/site_head.html`.
- The People page is independent of the Joint Lab grid. Its member class in
  `layouts/partials/widgets/awesome.html` produces five columns on desktop,
  three on tablet, and two below 576px. Home keeps its single Principal
  Investigator card full-width on mobile through the separate `people.html`
  widget.
- Shared CSS in `layouts/partials/site_head.html` keeps portraits circular and
  links aligned.
- Do not add per-widget `<style>` blocks. Update the global style block instead.

## Adding a member

1. Create the author profile and verify the name, school, role, interests, links,
   and portrait from a first-party source.
2. Set the Joint Lab fields above, adding `joint_lab_identity` when a distinct
   personal identity is useful, and choose the next `joint_lab_order` in the
   relevant section.
3. Run `git diff --check` and `hugo --gc --minify`.
4. Check Home, `/people/`, and `/mirod-lab/` in light and dark themes at desktop
   and mobile widths. Confirm the People page has no standalone Joint Lab block.

Do not push changes unless the user explicitly requests it.
