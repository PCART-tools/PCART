import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, column_widths=None, autofilter=True, column_totals=None, row_heights=None, table_style=None, has_header=True, autofit=False, position='A1', table_name=None, column_formats=None, sparklines=None, dtype_formats=None, worksheet=None, float_precision=3, conditional_formats=None)
