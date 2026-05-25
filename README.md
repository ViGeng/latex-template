# Latex Template

This repository contains `custom.sty`, a small reusable LaTeX package providing checklist symbols, framed quotes, and simple comment macros you can drop into other projects.

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
- `enumitem`
- `amssymb`
- `xparse`
- `ifthen`
- `mdframed`

You generally do not need to `\usepackage` these yourself — `custom.sty` loads them — but if you need to set options for any of them, load that package first in your preamble.

## Notes

- Exported macros include `\cmark`, `\xmark`, `\done`, `\gcheck`, `\unsure`, and `\wei` (a comment macro). They are short names and may collide with other packages; consider renaming or namespacing if you reuse them across many packages.
