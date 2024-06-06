from faker import Faker
fake = Faker()
email_address = fake.email(domain=None)
