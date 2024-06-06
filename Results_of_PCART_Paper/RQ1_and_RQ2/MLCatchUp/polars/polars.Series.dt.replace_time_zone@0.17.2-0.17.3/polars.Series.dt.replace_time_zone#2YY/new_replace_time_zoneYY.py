import polars as pl
pl.col('london_timezone').dt.replace_time_zone(time_zone='Europe/Amsterdam')
