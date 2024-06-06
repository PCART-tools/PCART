import polars as pl
from datetime import date
pl.date_range(interval='1mo', start=date(2022, 1, 1), end=date(2022, 3, 1))
