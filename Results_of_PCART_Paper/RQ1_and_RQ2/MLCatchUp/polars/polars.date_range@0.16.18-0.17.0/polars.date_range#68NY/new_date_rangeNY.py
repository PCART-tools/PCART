import polars as pl
from datetime import date
pl.date_range(name=None, interval='1mo', closed='both', lazy=False, start=date(2022, 1, 1), end=date(2022, 3, 1))
