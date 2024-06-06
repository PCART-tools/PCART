import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(dtype_formats=None, autofit=False, table_name=None, position='A1', float_precision=3, autofilter=True, hidden_columns=None, row_heights=None, column_widths=None, has_header=True, conditional_formats=None, column_totals=None, table_style=None, workbook=None, sparklines=None, column_formats=None)
