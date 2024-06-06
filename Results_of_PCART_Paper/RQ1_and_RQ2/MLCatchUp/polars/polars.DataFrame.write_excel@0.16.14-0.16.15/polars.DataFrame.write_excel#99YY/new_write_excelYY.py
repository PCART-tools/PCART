import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(dtype_formats=None, has_header=True, table_style=None, column_formats=None, table_name=None, column_totals=None, autofit=False, autofilter=True, column_widths=None, workbook=None, conditional_formats=None, sparklines=None, float_precision=3, row_heights=None, position='A1')
