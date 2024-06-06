from faker import Faker
fake = Faker('pl_PL')
pesel = fake.pesel(date_of_birth=None, sex=None)
