import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1), time_unit=None, name=None, lazy=False, interval='1mo', closed='both', end=date(2022, 3, 1))
