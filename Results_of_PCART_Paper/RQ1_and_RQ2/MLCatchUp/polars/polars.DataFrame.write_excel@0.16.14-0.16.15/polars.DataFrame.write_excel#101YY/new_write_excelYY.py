import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(workbook=None, hide_gridlines=False, sparklines=None, has_header=True, column_formats=None, column_totals=None, column_widths=None, table_name=None, table_style=None, float_precision=3, hidden_columns=None, row_heights=None, autofilter=True, dtype_formats=None, conditional_formats=None, position='A1', autofit=False)
