from faker import Faker
from datetime import datetime
fake = Faker()
unix_time = fake.unix_time(end_datetime=datetime(2020, 1, 1), start_datetime=None)
