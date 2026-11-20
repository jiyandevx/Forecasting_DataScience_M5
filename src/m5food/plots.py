"""One clean chart style for the morning presentations: big text, no clutter, numbers on bars."""
import matplotlib.pyplot as plt

PALETTE = ["#2a6f97", "#e07a1f", "#4c9f70", "#a23b72", "#6c757d"]


def set_style() -> None:
    plt.rcParams.update({
        "figure.figsize": (11, 6), "figure.dpi": 110,
        "font.size": 14, "axes.titlesize": 18, "axes.titleweight": "bold",
        "axes.titlelocation": "left", "axes.labelsize": 14,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.alpha": 0.25, "axes.axisbelow": True,
        "axes.prop_cycle": plt.cycler(color=PALETTE),
    })


def label_bars(ax, fmt: str = "{:,.0f}") -> None:
    """Write each bar's value on top of it, so the chart reads without a speaker."""
    for bar in ax.patches:
        ax.annotate(fmt.format(bar.get_height()),
                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    ha="center", va="bottom", fontsize=13, xytext=(0, 3),
                    textcoords="offset points")


def save(fig, name: str) -> None:
    """Save a slide-ready PNG into reports/figures."""
    from .data import ROOT
    fig.savefig(ROOT / "reports" / "figures" / f"{name}.png", bbox_inches="tight", dpi=200)
