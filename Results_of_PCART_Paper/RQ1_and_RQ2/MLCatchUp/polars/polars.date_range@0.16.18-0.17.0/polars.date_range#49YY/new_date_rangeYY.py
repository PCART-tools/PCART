import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1),  date(2022, 3, 1), lazy=False, time_unit=None, interval='1mo', name=None, closed='both')
