import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None,  None, float_precision=3, conditional_formats=None, autofilter=True, sparklines=None, column_widths=None, position='A1', column_formats=None, autofit=False, table_name=None, row_heights=None, hidden_columns=None, has_header=True, table_style=None, dtype_formats=None, column_totals=None)
