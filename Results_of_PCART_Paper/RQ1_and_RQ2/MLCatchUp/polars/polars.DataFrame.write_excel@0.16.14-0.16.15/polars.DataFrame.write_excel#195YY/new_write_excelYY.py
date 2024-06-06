import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(conditional_formats=None, table_name=None, column_widths=None, dtype_formats=None, workbook=None, table_style=None, column_totals=None, position='A1', worksheet=None, column_formats=None)
