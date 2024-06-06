import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1), time_unit=None, name=None, closed='both', lazy=False, interval='1mo', time_zone=None, end=date(2022, 3, 1))
