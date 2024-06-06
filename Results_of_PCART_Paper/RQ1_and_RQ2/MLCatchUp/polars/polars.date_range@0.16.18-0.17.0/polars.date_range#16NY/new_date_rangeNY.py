import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1), time_zone=None, end=date(2022, 3, 1))
