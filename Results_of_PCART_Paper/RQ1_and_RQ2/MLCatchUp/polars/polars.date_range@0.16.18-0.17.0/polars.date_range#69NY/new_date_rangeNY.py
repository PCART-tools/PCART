import polars as pl
from datetime import date
pl.date_range(name=None, lazy=False, interval='1mo', time_unit=None, closed='both', start=date(2022, 1, 1), end=date(2022, 3, 1))
