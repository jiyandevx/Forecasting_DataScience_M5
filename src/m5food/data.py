"""Load the M5 files from data/raw. FOODS only, kept wide: one row per item-store."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"

CATEGORY = "FOODS"
SALES_FILE = "sales_train_evaluation.csv"  # 1,941 days; the validation file has 1,913


def load_calendar(raw_dir: Path = RAW) -> pd.DataFrame:
    """One row per day: date, weekday, events, SNAP flags per state."""
    return pd.read_csv(raw_dir / "calendar.csv", parse_dates=["date"])


def load_prices(raw_dir: Path = RAW) -> pd.DataFrame:
    """One row per store, item and week. No row means no price that week."""
    prices = pd.read_csv(raw_dir / "sell_prices.csv")
    return prices[prices.item_id.str.startswith(CATEGORY)].reset_index(drop=True)


def load_sales_foods(raw_dir: Path = RAW, sales_file: str = SALES_FILE) -> pd.DataFrame:
    """Wide table: id columns, then d_1 ... d_N units sold per day. FOODS rows only."""
    sales = pd.read_csv(raw_dir / sales_file)
    return sales[sales.cat_id == CATEGORY].reset_index(drop=True)


def day_columns(sales: pd.DataFrame) -> list[str]:
    """The d_1 ... d_N columns of the wide sales table."""
    return [c for c in sales.columns if c.startswith("d_")]
