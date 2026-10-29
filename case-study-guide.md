# Case Study Pages — Guide

## File location

Each case study lives at `/work/[project-name].html`  
Example: `/work/monday.html`, `/work/ai-assistant.html`

## Structure of each case study page

Every case study is a standalone `.html` file that includes:
- The same **nav** as `index.html` (copy/paste it)
- The same **footer** as `index.html` (copy/paste it)
- Its own content in between
- Its own color palette (no fixed colors — each product has its own)

## Linking from the landing page

In `index.html`, the WORK section has an `<article>` card per case study.  
The card links to the case study file:
```html
<a href="work/project-name.html">...</a>
```

## What a case study page typically contains

1. **Hero** — Project title, one-line description, hero image or visual
2. **Overview** — Role, timeline, tools, team
3. **Problem** — What was the challenge
4. **Process** — Research, ideation, iterations (with images/mockups)
5. **Solution** — Final design with visuals
6. **Results** — Metrics, outcomes, learnings

## Code conventions (same as landing page)

- Vanilla HTML/CSS/JS only — no frameworks
- Styles inline via `style=""` attributes
- CSS classes only for `:hover`, `@keyframes`, or media queries
- All JS inside `document.addEventListener('DOMContentLoaded', ...)`
- Section comments: `<!-- HERO -->`, `<!-- OVERVIEW -->`, etc.
- Fonts: load same Google Fonts + Fontshare as `index.html`
- Icons: Lucide SVG inline (stroke:currentColor, fill:none, stroke-width:2, 0.85em)

## Images

- Store in `/uploads/` folder
- Reference as `../uploads/filename.png` from `/work/` files

## Nav to copy into each case study

```html
<header id="top" style="position: fixed; top: 0; left: 0; right: 0; z-index: 50; backdrop-filter: blur(12px); border-bottom: 1px solid transparent; transition: border-color 250ms cubic-bezier(0.16,1,0.3,1); background-color: #FFFCF2E0">
  <nav style="display: flex; align-items: center; justify-content: space-between; padding: 20px 32px; max-width: 1500px; margin: 0 auto; letter-spacing: 0.08em;" aria-label="Main">
    <a href="../index.html" class="nav-link" style="font-weight: 400; font-family: Poppins; font-size: 14px; text-transform: uppercase; text-decoration: none;">Gal Ganon</a>
    <ul class="nav-links-list" style="display: flex; gap: 32px; list-style: none;">
      <li><a href="../index.html#about" class="nav-link" style="font-weight: 300; font-family: Poppins; font-size: 14px; text-transform: uppercase;">About</a></li>
      <li><a href="../index.html#work" class="nav-link" style="font-weight: 300; font-family: Poppins; font-size: 14px; text-transform: uppercase;">Work</a></li>
      <li><a href="../index.html#contact" class="nav-link" style="font-weight: 300; font-family: Poppins; font-size: 14px; text-transform: uppercase;">Contact</a></li>
    </ul>
    <a href="https://www.linkedin.com/in/gal-ganon/" target="_blank" rel="noopener" class="nav-link" style="font-weight: 400; font-family: Poppins; font-size: 14px; text-decoration: none;">LinkedIn</a>
  </nav>
</header>
```
