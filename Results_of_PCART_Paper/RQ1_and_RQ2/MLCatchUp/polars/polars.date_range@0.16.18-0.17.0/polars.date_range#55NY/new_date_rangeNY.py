import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1), interval='1mo', time_unit=None, end=date(2022, 3, 1))
