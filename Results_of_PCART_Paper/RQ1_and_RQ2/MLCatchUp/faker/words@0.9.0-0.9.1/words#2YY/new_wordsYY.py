from faker import Faker
fake = Faker()
words = fake.words(5, unique=False)
