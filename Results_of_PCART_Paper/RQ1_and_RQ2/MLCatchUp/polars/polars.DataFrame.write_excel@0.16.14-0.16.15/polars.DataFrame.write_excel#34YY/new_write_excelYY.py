import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(row_heights=None, autofilter=True, conditional_formats=None, column_totals=None, hidden_columns=None, hide_gridlines=False, autofit=False, has_header=True, sparklines=None, table_style=None, dtype_formats=None, column_formats=None, position='A1', sheet_zoom=None, column_widths=None, table_name=None, float_precision=3)
