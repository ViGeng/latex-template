# Changelog

## figstyle: pin mathtext to the serif body font — 2026-06-27

Fixed a within-figure font inconsistency. `wgeng.mplstyle` set `font.family:
serif` but left `mathtext.fontset` unset, so matplotlib rendered every `$…$`
label (e.g. `$\Delta\!\mathrm{AP}$`, `$\mathrm{MORIC}^{+}$`) in its default
**DejaVu Sans**, while plain strings used the serif body font — two typefaces in
one plot.

- **Fix in `gen.py`** (the generator, so it survives regeneration): added
  `mathtext.fontset: dejavuserif` to the `wgeng.mplstyle` block; regenerated.
  Math now matches the serif text. Re-render existing figures to pick it up.

## figstyle kit: shared figure palette + TikZ/matplotlib style — 2026-06-26

Added `figstyle/`, the global "appearance" layer for figures so diagrams and
plots look consistent across every paper.

- **Single source of truth.** `palette.toml` holds the Okabe-Ito/Wong palette,
  venue column widths, and type sizes. `gen.py` regenerates `wgpalette.tex`
  (LaTeX `\definecolor`), `wgpalette.py` (matplotlib constants + `use_style()`),
  and `wgeng.mplstyle` — so the LaTeX and Python sides can never drift.
- **wgstyle.sty** provides neutral TikZ node/edge styles and a generic icon
  library (camera, cloud, chip, server, gear, doc, envelope, check, pulse,
  spark). It bakes in no concept colors: `[wgbox, draw=ours]` gives meaning.
- **Two-layer model.** Appearance is global (this kit); meaning is per-paper in
  `theme.tex` / `theme.py` (copy + edit). Golden rule: figures address colors
  by meaning (`ours`, `cost`), never by hue (`wgTeal`).
- **Examples** under `figstyle/examples/` (a TikZ pipeline and a matplotlib cost
  plot) build clean with `pdflatex` / `python`; previews in the kit README.

## \todo tag: TODO-prefixed label + case-insensitive matching — 2026-06-07

Refined the `\todo[label]{text}` macro in `custom.sty`.

- **Tag now always leads with `TODO`.** Previously a label like `[FIXME]` replaced
  the tag entirely, so the box showed only "FIXME". Now the base "TODO" is always
  shown and a non-default label is appended as `TODO·FIXME` (middle-dot separator),
  keeping every annotation scannable as a TODO with a priority sub-tag.
- **Label matching is case-insensitive.** The label is normalised to uppercase
  before the colour branch, so `[fixme]`, `[FixMe]`, and `[FIXME]` all map to the
  same priority colour. The appended label also displays uppercased for consistency.

Colour mapping: `FIXME`/`BUG` red, `TODO` orange (default/normal),
`NOTE`/`LATER`/`HOLD` gray (`HOLD` added to the low-priority group, consistent
with `\ai[hold]`), anything else normal orange.

Updated the quick-reference and the `\todo` doc block in `custom.sty`, the README
note, and the `report.tex` demo (uses lowercase `[fixme]` to exercise the
case-insensitive path). Verified with `pdflatex report.tex` (clean build); the PDF
text layer shows `TODO`, `TODO · FIXME`, `TODO · NOTE`, `TODO · HOLD`.
