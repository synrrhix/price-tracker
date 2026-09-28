# Price Tracker

A terminal app for tracking product prices over time. Add products, log new prices with dates, and see how each price has changed.

## Features

- Add, find, update and remove products
- Log a new price with a date, kept in a price history
- Product statistics: current, lowest and highest price, percentage change, number of records
- Group products by category (20 categories, held in an `Enum`)
- Save to and load from `products.json`
- Input checks for prices, dates and categories, so bad input asks again instead of crashing

## Run it

Needs Python 3.8 or newer. No extra packages.

```
python main.py
```

## Project layout

| File | What it does |
| --- | --- |
| `main.py` | Menu and program loop |
| `models.py` | `Category` enum, `PriceRecord` and `Product` classes |
| `tracker.py` | Adding, finding, updating and grouping products, price drop helpers |
| `storage.py` | Saving and loading JSON |

## What I practised

- Classes with `@property`, `@classmethod` and `@staticmethod`
- `Enum` for a fixed list of categories
- Generators (`yield`) for price drops
- `Counter` and `defaultdict` from `collections`
- `*args` and `**kwargs`
- Type hints and docstrings
- Converting objects to and from JSON, including dates
