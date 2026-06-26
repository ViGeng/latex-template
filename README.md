# Latex Template

This repository holds reusable LaTeX building blocks shared across papers:

- **`custom.sty`** — checklist symbols, framed quotes, and AI-collaboration comment macros (`\ai`, `\todo`, `\wei`).
- **`figstyle/`** — the figure style kit: one Okabe-Ito palette plus TikZ and matplotlib conventions so diagrams and plots look consistent across every project. See [`figstyle/README.md`](figstyle/README.md).

## Figure style kit (`figstyle/`)

A shared "house style" for figures, split into two layers: **appearance** (the
palette, fonts, line weights, TikZ styles, and an icon library) lives globally
in this kit; **meaning** (which concept gets which color, column widths) lives
per-paper in a small `theme.tex` / `theme.py` you copy and edit. Figures
reference colors by meaning (`draw=ours`), never by hue (`wgTeal`), so one
palette edit reflows every paper.

Vendor it by copying `figstyle/` into a project root, then `\usepackage{figstyle/wgstyle}` and `\input{theme}`. The palette is generated from `figstyle/palette.toml` via `python figstyle/gen.py`. Full reference and examples: [`figstyle/README.md`](figstyle/README.md).

## Quick usage

1. Copy `custom.sty` into your project folder (the same folder as `main.tex`) or install it into your local texmf tree.
2. In your document preamble add:

```latex
\documentclass{article}
% (optional) if you need specific xcolor options, load xcolor before custom:
% \usepackage[dvipsnames]{xcolor}
\usepackage{custom}
\begin{document}
...
\end{document}
```

3. If you need to pass package-specific options (for example color name sets for `xcolor`), load that package with options before `\usepackage{custom}` so the options take effect.

### Placing `custom.sty` alongside your `main.tex`

If you put `custom.sty` in the same folder as your `main.tex`, LaTeX will find it automatically when you write `\usepackage{custom}` in the preamble. No installation into texmf is required for local project use.

If you put it in a subfolder which is in the same folder with your main.tex, then you need to specify the relative path to the style file, like this:

```latex
\usepackage{subfolder/custom}
```

## Dependencies

`custom.sty` loads the following packages internally:

- `xcolor`
- `pifont`
- `fontawesome5` (chat-bubble icons for `\ai`)
- `enumitem`
- `amssymb`
- `xparse`
- `ifthen`
- `mdframed`
- `siunitx`
- `xfp`
- `hyperref`
- `cleveref`

You generally do not need to `\usepackage` these yourself — `custom.sty` loads them — but if you need to set options for any of them, load that package first in your preamble. Note: because `custom.sty` loads `hyperref` and `cleveref`, do **not** load `hyperref` yourself; apply options via `\hypersetup{...}` after `\usepackage{custom}`.

## Editor setup

`.vscode/settings.json` recolors the custom/generic LaTeX commands (e.g. `\wei`, `\skp`, `\cnd`, `\ph`) so they no longer blend into body text in the editor. It targets the shared TextMate scope `support.function.general.{tex,latex}` used by LaTeX Workshop; built-in commands like `\ref`, `\cite`, and `\emph` keep their own theme colors. Change the `foreground` hex value to pick a different color, or remove the file to opt out.

## Notes

- Review/collaboration macros — `\wei` (an author comment), `\mynote`, `\todo` (an inline action item), and `\ai` (hand a span to an AI with a prompt, rendered as a chat bubble) — all honor the `showcomments` toggle, so they disappear in camera-ready output (set `\setboolean{showcomments}{false}`).
- `\todo[label]{text}` always leads its tag with `TODO` and appends a non-default label (e.g. `TODO·FIXME`), then colors itself by priority from that label: `FIXME`/`BUG` are high (red), `TODO` (the default) is normal (orange), and `NOTE`/`LATER`/`HOLD` are low (gray); any other label uses the normal color. Label matching is case-insensitive, so `[fixme]`, `[FixMe]`, and `[FIXME]` are equivalent.
- `\ai{quoted text}{instruction}` carries an action state in its optional argument: by default the AI should apply the instruction now; use `\ai[hold]{...}{...}` to park a request for later instead of acting on it.
- Macro names are short and may collide with other packages (notably `\todo` from `todonotes`); consider renaming or namespacing if you reuse `custom.sty` alongside such packages.
