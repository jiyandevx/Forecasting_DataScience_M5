# Decisions

One line each: what, why, status. Update it as choices change.

| # | Decision | Why | Status |
|---|---|---|---|
| 1 | Scope: FOODS category, all 10 stores | Largest category by items (1,437 of 3,049). Ten stores let us train on one store and test on others, and compare states. Slow movers in HOBBIES and HOUSEHOLD are left out on purpose, so every result stays explainable. | Agreed |
| 2 | Level: each item in each store (14,370 series) | Stock is decided per item per store | Working assumption |
| 3 | Horizon: 28 days | Matches the M5 competition setting | Proposed |
| 4 | FOODS has the fewest zero-sales days | Not yet checked by category | To verify |
