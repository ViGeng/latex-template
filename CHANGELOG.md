# Changelog

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
