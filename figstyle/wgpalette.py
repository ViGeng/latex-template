"""GENERATED from palette.toml by gen.py -- DO NOT EDIT.

Edit palette.toml and run: python gen.py
Import as e.g. ``import wgpalette as wg`` then ``wg.use_style()`` and
reference ``wg.TEAL``. ``use_style()`` applies wgeng.mplstyle.
"""

import os as _os

try:
    import matplotlib.pyplot as _plt
except ImportError:  # palette is still usable without matplotlib
    _plt = None

# --- core hues (each with a light _BG tint) ---
TEAL = "#1C7C6C"  # primary / ours / hero
TEAL_BG = "#E7F3EF"
BLUE = "#2E6FB0"  # secondary / infrastructure / control
BLUE_BG = "#E8F1FB"
AMBER = "#C9821F"  # attention / the costly thing
AMBER_BG = "#FBEEDB"
SLATE = "#6E767E"  # neutral / pipeline / outputs
SLATE_BG = "#EEF1F3"
GREEN = "#2E8B57"  # good / health / ideal
GREEN_BG = "#E9F4EC"
RED = "#C4313C"  # problem / drift / failure
RED_BG = "#FBE9EA"
PURPLE = "#6A51A3"  # alternative method / 4th category
PURPLE_BG = "#ECE8F4"
PINK = "#CC79A7"  # alternative method / penalty region
PINK_BG = "#F7EAF1"

# --- saturated line accents ---
VIVID = "#D55E00"
AZURE = "#0072B2"

# --- extras ---
INK = "#2B2B2B"
EDGE_BG = "#F4F8F7"

# --- venue column widths (inches) ---
COL_ACM = 3.34
DBL_ACM = 7.0
COL_USENIX = 3.32
DBL_USENIX = 7.0
COL_IEEE = 3.5
DBL_IEEE = 7.16

_MPLSTYLE = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "wgeng.mplstyle")


def use_style():
    """Apply the shared figure rcParams (wgeng.mplstyle)."""
    if _plt is None:
        raise ImportError("matplotlib is required for use_style()")
    _plt.style.use(_MPLSTYLE)
