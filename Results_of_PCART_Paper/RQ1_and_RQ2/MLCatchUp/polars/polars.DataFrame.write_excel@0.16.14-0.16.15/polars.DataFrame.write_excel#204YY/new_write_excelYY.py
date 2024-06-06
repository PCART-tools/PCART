import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(sheet_zoom=None, worksheet=None, dtype_formats=None, has_header=True, sparklines=None, column_formats=None, hide_gridlines=False, float_precision=3, column_widths=None, table_style=None, workbook=None, column_totals=None, hidden_columns=None, autofilter=True, row_heights=None, autofit=False, position='A1', conditional_formats=None, table_name=None)
