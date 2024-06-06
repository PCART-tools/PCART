import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1),  date(2022, 3, 1), time_zone=None, lazy=False, closed='both', name=None, time_unit=None)
