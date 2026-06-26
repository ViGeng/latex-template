#!/usr/bin/env python3
"""Generate the LaTeX and matplotlib palette files from palette.toml.

Single source of truth: palette.toml. Run this after editing it:

    python gen.py

Writes (all stamped "DO NOT EDIT"):
  wgpalette.tex   -- \\definecolor block for wgstyle.sty
  wgpalette.py    -- color constants + widths + use_style() for matplotlib
  wgeng.mplstyle  -- shared rcParams

Requires Python >= 3.11 (tomllib). No third-party dependencies.
"""
import os
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "palette.toml")

TEX_HEAD = (
    "%% GENERATED from palette.toml by gen.py -- DO NOT EDIT.\n"
    "%% Edit palette.toml and run: python gen.py\n"
    "%% Loaded by wgstyle.sty via \\input{<path>wgpalette}.\n"
)
PY_HEAD = (
    '"""GENERATED from palette.toml by gen.py -- DO NOT EDIT.\n\n'
    "Edit palette.toml and run: python gen.py\n"
    "Import as e.g. ``import wgpalette as wg`` then ``wg.use_style()`` and\n"
    "reference ``wg.TEAL``. ``use_style()`` applies wgeng.mplstyle.\n"
    '"""\n'
)
MPL_HEAD = "# GENERATED from palette.toml by gen.py -- DO NOT EDIT.\n"


def camel(name):
    return "wg" + name[:1].upper() + name[1:]


def main():
    with open(SRC, "rb") as f:
        p = tomllib.load(f)

    fills = p["fill"]
    curve = p["curve"]
    extra = p["extra"]
    widths = p["widths"]
    typ = p["type"]

    # ---- wgpalette.tex --------------------------------------------------
    tex = [TEX_HEAD]
    for name, c in fills.items():
        tex.append(
            f"\\definecolor{{{camel(name)}}}{{HTML}}{{{c['hex'].upper()}}}"
            f"\\definecolor{{{camel(name)}Bg}}{{HTML}}{{{c['bg'].upper()}}}"
            f"% {c['role']}"
        )
    tex.append("%% --- saturated line accents ---")
    for name, hex_ in curve.items():
        tex.append(f"\\definecolor{{{camel(name)}}}{{HTML}}{{{hex_.upper()}}}")
    tex.append("%% --- extras ---")
    for name, hex_ in extra.items():
        texname = "wgEdgeBg" if name == "edgebg" else camel(name)
        tex.append(f"\\definecolor{{{texname}}}{{HTML}}{{{hex_.upper()}}}")
    tex.append("\\colorlet{wgComment}{wgSlate}% muted algorithm-comment text")
    write(os.path.join(HERE, "wgpalette.tex"), "\n".join(tex) + "\n")

    # ---- wgpalette.py ---------------------------------------------------
    py = [PY_HEAD, "import os as _os", "", "try:", "    import matplotlib.pyplot as _plt",
          "except ImportError:  # palette is still usable without matplotlib",
          "    _plt = None", "", "# --- core hues (each with a light _BG tint) ---"]
    for name, c in fills.items():
        u = name.upper()
        py.append(f'{u} = "#{c["hex"].upper()}"  # {c["role"]}')
        py.append(f'{u}_BG = "#{c["bg"].upper()}"')
    py.append("")
    py.append("# --- saturated line accents ---")
    for name, hex_ in curve.items():
        py.append(f'{name.upper()} = "#{hex_.upper()}"')
    py.append("")
    py.append("# --- extras ---")
    for name, hex_ in extra.items():
        u = "EDGE_BG" if name == "edgebg" else name.upper()
        py.append(f'{u} = "#{hex_.upper()}"')
    py.append("")
    py.append("# --- venue column widths (inches) ---")
    for name, val in widths.items():
        py.append(f"{name.upper()} = {val}")
    py.append("")
    py.append('_MPLSTYLE = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "wgeng.mplstyle")')
    py.append("")
    py.append("")
    py.append("def use_style():")
    py.append('    """Apply the shared figure rcParams (wgeng.mplstyle)."""')
    py.append("    if _plt is None:")
    py.append('        raise ImportError("matplotlib is required for use_style()")')
    py.append("    _plt.style.use(_MPLSTYLE)")
    write(os.path.join(HERE, "wgpalette.py"), "\n".join(py) + "\n")

    # ---- wgeng.mplstyle -------------------------------------------------
    mpl = [MPL_HEAD,
           "font.family:        serif",
           f"font.size:          {typ['font']}",
           f"axes.labelsize:     {typ['label']}",
           f"legend.fontsize:    {typ['legend']}",
           f"xtick.labelsize:    {typ['tick']}",
           f"ytick.labelsize:    {typ['tick']}",
           "axes.spines.top:    False",
           "axes.spines.right:  False",
           "axes.linewidth:     0.8",
           "axes.grid:          False",
           "grid.alpha:         0.16",
           "grid.linewidth:     0.5",
           "lines.linewidth:    1.9",
           "legend.frameon:     False",
           "legend.handlelength: 1.5",
           "legend.labelspacing: 0.3",
           "legend.borderpad:   0.3",
           "figure.dpi:         150",
           "savefig.dpi:        300",
           "savefig.bbox:       tight",
           "pdf.fonttype:       42  # embed TrueType, no Type-3 (camera-ready safe)",
           "ps.fonttype:        42"]
    write(os.path.join(HERE, "wgeng.mplstyle"), "\n".join(mpl) + "\n")


def write(path, text):
    with open(path, "w") as f:
        f.write(text)
    print(f"wrote {os.path.relpath(path, HERE)}")


if __name__ == "__main__":
    main()
