import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(workbook=None, hidden_columns=None, column_widths=None, column_formats=None, row_heights=None, sparklines=None, position='A1', table_style=None, column_totals=None, dtype_formats=None, float_precision=3, has_header=True, autofit=False, table_name=None, worksheet=None, conditional_formats=None, autofilter=True)
