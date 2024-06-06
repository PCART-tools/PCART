import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None,  None, column_widths=None, column_formats=None, autofilter=True, sheet_zoom=None, hidden_columns=None, position='A1', table_name=None, row_heights=None, hide_gridlines=False, float_precision=3, column_totals=None, sparklines=None, autofit=False, has_header=True, dtype_formats=None, conditional_formats=None, table_style=None)
