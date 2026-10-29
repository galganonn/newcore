# NewCore IAM — Claude Instructions

## What this project is

Design exercise for **NewCore** — an Identity Security startup ($300M, seed $66M).
The task: design the **agentic experience** for an IAM Admin around the prompt:
> *"I want to harden the access of my marketing agents"*

## Files

```
/
├── newcore-assignment.md       ← Full research, decisions, and spec
├── deployment-overview.html    ← Interactive prototype (Piper AI agent)
├── uploads/
│   └── deployment-overview/      ← All assets for the prototype
└── serve.py                    ← Local dev server (python3 serve.py)
```

## Stack

Vanilla HTML/CSS/JS — no frameworks, no build tools.
Run locally: `python3 serve.py` → open `http://localhost:9955/deployment-overview.html`

## Prototype: deployment-overview.html

monday.com-style product shell with Piper (AI agent) chat UI.

### Layout

Full-height, no body scroll. Three-layer flex chain (each needs `min-height: 0`):
```
body { height: 100vh; overflow: hidden; }
.main-area → .content-panel → .content-body → .chat-wrap → .chat-area (scrollable)
```

Side panel: `position: absolute; top: 0; right: 0; bottom: 0; width: 340px` inside `.content-panel`.

### CTA block order (canonical)

```
1. .chat-recommended   ← recommended text
2. .chat-action-rows   ← buttons (secondary left, primary right)
3. .sources-row        ← sources label "Sources" (English)
4. .chat-action-feedback ← 👍👎 (ALWAYS LAST)
```

### Colors

- Sidebar bg: `#F5F6F8`
- Content panel: `white`
- Borders: `#e7e9ef`, `#e0e3ee`
- Text primary: `#1F2033`
- Text secondary: `#676879`, `#9699A6`
- Primary blue: `#0073EA`
- AI accent (robot): `#6366F1`
- Risk badge red: `#D83A52`

### Intro animation

1. User message — visible immediately
2. AI description — fades in after 600ms
3. Thinking card + PROC_STEPS — fades in after 1500ms, then 5 steps (8300ms total)

### Code conventions

- Everything inline — no separate CSS/JS files
- `style=""` attributes directly, classes only for `:hover` / `::after` / `@keyframes`
- All JS in single `<script>` before `</body>`, wrapped in `DOMContentLoaded`
