import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(has_header=True, dtype_formats=None, column_widths=None, autofilter=True, table_style=None, float_precision=3, column_formats=None, row_heights=None, table_name=None, column_totals=None, autofit=False, sparklines=None, conditional_formats=None, workbook=None, hide_gridlines=False, hidden_columns=None, position='A1', worksheet=None)
