import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(conditional_formats=None, column_totals=None, sheet_zoom=None, column_formats=None, autofilter=True, table_style=None, table_name=None, has_header=True, row_heights=None, float_precision=3, workbook=None, position='A1', column_widths=None, sparklines=None, autofit=False, hidden_columns=None, dtype_formats=None, hide_gridlines=False)
