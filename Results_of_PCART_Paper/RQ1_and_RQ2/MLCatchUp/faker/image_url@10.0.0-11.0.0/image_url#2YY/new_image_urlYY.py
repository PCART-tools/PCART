from faker import Faker
fake = Faker()
image_url = fake.image_url(800, placeholder_url=None)
