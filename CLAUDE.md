# Portfolio Gal — Claude Instructions

## What this project is

Professional portfolio for **Gal Ganon**, Senior Product Designer. Static site in vanilla HTML/CSS/JS — no frameworks, no build tools, no external dependencies. Everything lives in a single directory.

## Stack

- Vanilla HTML/CSS/JS
- No npm, webpack, bundlers, or anything similar
- Fonts via Google Fonts and Fontshare (CDN, inlined in `<head>`)
- No external JS libraries

## File structure

```
/Portfolio Gal/
├── index.html          ← Landing page (COMPLETE)
├── work/               ← Case studies (to be created)
│   └── [project].html
├── uploads/            ← Images and assets
└── CLAUDE.md           ← This file
```

## Fonts in use

| Font | Usage | How it loads |
|------|-------|-------------|
| **Poppins** | Body, UI, chips | Google Fonts |
| **Space Grotesk** | Section headings (e.g. "Featured Work") | Google Fonts |
| **Array** | Main hero ("Senior") | Fontshare |
| **Crimson Pro** | Decorative italic (chip "Information Design") | System / Google |

## Icons

Lucide style — always inline SVG, never emoji or images for UI iconography:

```html
<svg style="display:inline-block;width:0.85em;height:0.85em;vertical-align:-0.15em;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;margin:0 0.05em;" viewBox="0 0 24 24">
  <!-- paths from lucide.dev -->
</svg>
```

## Colors

The landing page uses `#FBF6E9` / `#FFFCF2` (cream) and `#141414` (near-black). **Case studies have their own colors** based on each product — there is no fixed palette for content pages.

## Landing page sections (index.html) — already built

- **NAV**: Fixed, blur backdrop, `GAL GANON` + ABOUT / WORK / CONTACT links + LinkedIn (`https://www.linkedin.com/in/gal-ganon/`)
- **HERO**: "Senior" (Array font) / "PRODUCT" with decorative red toggle switch / "DESIGNER" with profile photo as the letter "I" + animated Figma emoji
- **ABOUT**: Bio with inline profile photo, Lucide icons inside the text, "2021" badge
- **SKILLS**: 11 chips with `position:absolute` inside a 200px-height container. Hover lift via `cubic-bezier(0.34,1.56,0.64,1)` with box-shadow. Chips with rotation: Empathy `rotate(-36deg)`, Collaboration `rotate(28deg)`, `&` `rotate(8deg)`
- **WORK**: "Featured Work" section — content to be filled with case studies
- **CONTACT / FOOTER**: Email `galganonn@gmail.com` with a copy-to-clipboard button. Confirmation toast appears **below** the email. Footer with animated bouncing cursor

## JS behaviors already implemented

- Nav border appears on scroll (`header.scrolled`)
- Decorative toggle in HERO (red switch, animates the knob)
- Floating particles in the hero (`#dots-container`)
- Email copy: uses `navigator.clipboard` with `execCommand` fallback. Toast: `#copy-toast`
- Hover lift on chips: JS in `DOMContentLoaded` adds `translateY(-7px)` on top of the chip's existing transform, restores on mouseleave

## Code conventions

- Everything inline (no separate CSS or JS files for now)
- Styles via `style=""` attributes directly in HTML
- CSS classes are only used when `:hover`, `::after`, `@keyframes`, or media queries are needed
- Section comments in HTML: `<!-- NAV -->`, `<!-- HERO -->`, etc.
- All JS lives in a single `<script>` block before `</body>`, wrapped in `document.addEventListener('DOMContentLoaded', ...)`

## About case studies (work/)

- Each case study = one independent `.html` file in `/work/`
- Each has its own color palette based on the product
- Must be linked from the WORK section in `index.html`
- Keep the same nav and footer as the landing page for consistency

## Git

- Main branch: `main`
- Commit before every significant change
- No prior commit history (project was started without commits)
