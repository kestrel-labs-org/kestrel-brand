# Kestrel Labs — Brand Guide v1.0

Open source tools for Linux · kestrellabs.org

## The idea

A kestrel is the falcon that *hovers* — it holds perfectly still in moving air, watching, then commits. That's the brand: precise, patient, unflashy tools that do one job well. The mark is a kestrel seen from below, wings spread, tail fanned, mid-hover. It's built from straight cuts only (no curves) so it stays crisp at 16 px and reads as "engineered," not "illustrated." The rust terminal band on the tail is the one accent — real kestrels have a dark band there, and it's the single detail that separates this silhouette from a generic eagle.

Visual direction: **geometric, faceted, technical** — Swiss restraint with a workshop temperature.

## Colour

| Name | Hex | Role |
|---|---|---|
| Charcoal | `#2A2B2E` | Primary. Backgrounds, primary logo colour on light surfaces. |
| Rust | `#C9512A` | Accent. Tail band, "LABS", links, one CTA per screen. Never more than ~10% of a surface. |
| Bone | `#F2EDE4` | Light surface / reversed logo colour. Warm, not pure white. |
| Slate | `#5C5F66` | Secondary text on light surfaces. |
| Ash | `#A9ABB0` | Secondary text on dark surfaces, hairlines. |
| Ink | `#151618` | Deepest background (code blocks, footers). |

Contrast: Bone on Charcoal ≈ 12.9:1, Rust on Charcoal ≈ 4.6:1 (large text / UI only), Charcoal on Bone ≈ 12.9:1.

Rule of thumb: charcoal does the work, bone gives it air, rust points. If a layout has more than one rust element competing for attention, one of them is wrong.

## Type

- **Wordmark / display:** Tektur Medium, all caps, tracking +5%. `KESTREL` in the primary colour, `LABS` in rust. Do not re-set the wordmark — use the supplied SVGs.
- **Labels, URLs, taglines, code:** Geist Mono Regular, caps with wide tracking (+20–28%) for labels; normal case for URLs.
- **Body / UI text (websites, READMEs, app UI):** Inter or system sans (Noto Sans on Linux). Nothing in the kit depends on it.

Both display fonts are OFL-licensed: Tektur and Geist Mono are free to bundle with apps and websites.

## Logo system

| File | Use |
|---|---|
| `kestrel-mark` | Symbol alone. App icons, favicons, avatars, small spaces. |
| `kestrel-labs-horizontal` | Default lockup. Headers, READMEs, docs. |
| `kestrel-labs-stacked` | Square-ish spaces: social avatars with text, splash screens, stickers. |
| `*-reversed` | Bone + rust on dark backgrounds (transparent). |
| `*-on-charcoal` / `*-on-bone` | Same, with the background baked in. |
| `*-mono-black` / `*-mono-white` | Single-colour for embossing, watermarks, print. |
| `kestrel-mark-rust` | All-rust symbol. Sparingly. |

Clear space: keep a margin around the mark equal to the width of the tail band (~1/3 of the mark's width). Minimum size: mark 16 px, horizontal lockup 120 px wide.

Don't: rotate it, add gradients or shadows, outline it, put it on rust unless it's bone, recolour the band anything but rust or the body colour, or set "Kestrel Labs" in another font next to the mark.

## Icons

- `icons/svg/app-icon.svg` — charcoal rounded tile, bone bird, rust band. Default for `.desktop` files, GitHub org avatar, PWA icons.
- `icons/svg/app-icon-rust.svg` / `app-icon-light.svg` — alternates.
- `icons/png/app-icon-{16…1024}.png` — sizes 16, 22, 24, 32, 48, 64, 128, 256, 512, 1024. Covers the freedesktop hicolor set (`/usr/share/icons/hicolor/<size>x<size>/apps/`) plus store/PWA sizes.
- `icons/svg/kestrel-symbolic.svg` — 16 px single-colour symbolic icon for tray/panel (`*-symbolic` naming; set `fill` to `currentColor` if your toolkit recolours it).
- `icons/favicon.ico` (16/32/48) and `icons/favicon.svg`.

For individual apps (Kestrel App Manager, wgclient) the intent is: same tile, same bird, and a small per-app glyph or colour shift — decide that when the second app icon is needed rather than now.

## Banners

All in `banners/` as SVG + PNG, charcoal background, hairline grid, hover-field rings behind the mark:

- `github-social-preview-1280x640` — GitHub repo/org social preview image.
- `readme-banner-1200x300` — top of README.md.
- `social-header-1500x500` — X / generic profile header.
- `website-hero-1920x600` — kestrellabs.org hero.

The SVGs have text converted to outlines, so they render identically anywhere and need no fonts installed.

## README snippet

```markdown
<p align="center">
  <img src="https://kestrellabs.org/brand/readme-banner-1200x300.png" alt="Kestrel Labs" width="100%">
</p>
```

## Desktop file snippet

```ini
[Desktop Entry]
Name=Kestrel App Manager
Icon=org.kestrellabs.AppManager   # install app-icon-*.png into hicolor under this name
```

## Files

```
logo/svg, logo/png   – marks and lockups (PNG at 4–8× for retina)
icons/svg, icons/png – app icon tiles, symbolic icon, favicons
banners/             – four banner sizes, SVG + PNG
preview/             – brand-sheet.png overview
```

Regenerating: everything is produced from `mark.py` + `build.py` (pure polygons + fontTools outlines). Change a hex in one place and rebuild.
