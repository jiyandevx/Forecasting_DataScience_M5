# Forecasting on M5: FOODS, 10 stores

Research project on sales forecasting with the M5 dataset (Walmart), as the base for inventory forecasting.
Scope: the FOODS category in all 10 stores (3 states), at item-store level. The aim is to understand the
data, explain every modelling choice, and tell the story simply.

## Layout

```
data/            NOT in git. raw/ = M5 files as downloaded, processed/ = files made by code
src/m5food/      shared code: data.py (loading), plots.py (chart style)
notebooks/       exploring; messy is fine; outputs are stripped on commit
reports/         one dated notebook per review, charts only; figures/ holds slide PNGs
docs/            decisions.md: what was decided, and why
```

Added later, when needed: models, evaluation, and model notebooks.

## Setup

```bash
uv sync
```

Then pick the `.venv` interpreter as the notebook kernel in VS Code.

## Data

The M5 data is not included. Download it yourself from the competition page
(Kaggle: "M5 Forecasting - Accuracy"; needs a Kaggle account and accepting the competition rules) and put
these three files in `data/raw/`:

- `sales_train_evaluation.csv`
- `calendar.csv`
- `sell_prices.csv`

## Working rules

- Cleaning and loading live in `src/m5food`, never copied between notebooks.
- Review notebooks only draw charts. Their title states the finding and bars carry numbers.
- Notebook names: `YYYY-MM-DD_short_topic.ipynb`, so files sort in date order.
- Commit at the end of each day.
