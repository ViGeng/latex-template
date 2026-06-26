"""theme.py --- THIS paper's semantic map (the PROJECT / meaning layer).

Copy this file into your project's plot folder (e.g. figs/) and edit the
bindings. It is the ONLY file that knows where the vendored figstyle/ kit
lives -- adjust _FIGSTYLE if your layout differs (default: ../figstyle).

Plot scripts then stay path-agnostic:

    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import theme as T
    fig, ax = plt.subplots(figsize=(T.COL, T.COL * 0.7))
    ax.plot(x, y, color=T.OURS)

Golden rule: figures reference these CONCEPT names (OURS, COST, ...),
never the raw wg* hues.
"""
import os
import sys

_FIGSTYLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figstyle")
sys.path.insert(0, _FIGSTYLE)
import wgpalette as wg  # noqa: E402

wg.use_style()  # apply the shared rcParams (wgeng.mplstyle)

# --- bind this paper's concepts to palette hues ------------------------
OURS = wg.TEAL       # our system / method / hero
INFRA = wg.BLUE      # infrastructure / control plane
COST = wg.AMBER      # the costly / attention-worthy thing
NEUTRAL = wg.SLATE   # pipeline / generic components
GOOD = wg.GREEN      # fixes / health / ideal
BAD = wg.RED         # problems / drift / failure
ALT_A = wg.PURPLE    # a 4th category, if needed
ALT_B = wg.PINK      # a 5th category, if needed

# saturated accents for two max-contrast lines
LINE_A = wg.VIVID
LINE_B = wg.AZURE

# --- this venue's column widths (inches) -------------------------------
COL = wg.COL_ACM
DBL = wg.DBL_ACM
