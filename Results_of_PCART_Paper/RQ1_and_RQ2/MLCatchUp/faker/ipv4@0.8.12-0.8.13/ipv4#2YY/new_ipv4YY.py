from faker import Faker
fake = Faker()
ipv4_address = fake.ipv4(False, address_class=None, private=None)
