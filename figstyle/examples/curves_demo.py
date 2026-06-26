"""curves_demo.pdf -- shows the matplotlib half of wgstyle.

Two curves in the saturated accent colors, a shaded fill-between band to
name a quantity, a turn-point marker, and an arrow annotation -- the
recurring idioms of these papers. In a real project the color/width names
come from theme.py (T.LINE_A, T.COL); here we import the palette directly.

Run:  python curves_demo.py   (needs matplotlib + numpy)
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import wgpalette as wg

wg.use_style()  # the shared rcParams: serif 8pt, no top/right spines, etc.
import matplotlib.pyplot as plt

x = np.linspace(0.0, 1.0, 201)
a = 1.0 + 2.0 * x          # line A
b = 1.6 + 0.8 * x          # line B
cross = (1.6 - 1.0) / (2.0 - 0.8)  # where they meet

fig, ax = plt.subplots(figsize=(wg.COL_ACM, wg.COL_ACM * 0.7))

# shade the gap to name it; green where A wins, pink where B wins
above = x >= cross
ax.fill_between(x, a, b, where=above, color=wg.TEAL, alpha=0.16, lw=0)
ax.fill_between(x, b, a, where=~above, color=wg.PINK, alpha=0.30, lw=0)

ax.plot(x, a, color=wg.VIVID, label=r"method A")
ax.plot(x, b, color=wg.AZURE, label=r"method B")

ax.axvline(cross, color="0.5", ls=(0, (3, 2)), lw=0.8, zorder=1)
ax.scatter([cross], [1.0 + 2.0 * cross], s=16, color="0.2", zorder=6)
ax.annotate("crossover", xy=(cross, 1.0 + 2.0 * cross),
            xytext=(cross + 0.12, 1.3), fontsize=7, color="0.2",
            arrowprops=dict(arrowstyle="->", color="0.5", lw=0.7))

ax.set_xlabel(r"budget  $\rho$")
ax.set_ylabel("cost (a.u.)")
ax.set_xlim(0, 1)
ax.set_ylim(0, a.max() * 1.15)
ax.legend(loc="upper left")
ax.grid(axis="y")

here = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(here, "curves_demo.pdf"), bbox_inches="tight")
fig.savefig(os.path.join(here, "curves_demo_preview.png"), dpi=200, bbox_inches="tight")
print("wrote curves_demo.pdf (+ _preview.png)")
