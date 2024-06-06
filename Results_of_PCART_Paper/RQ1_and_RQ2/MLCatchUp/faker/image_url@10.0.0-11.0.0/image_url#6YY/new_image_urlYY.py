from faker import Faker
fake = Faker()
image_url = fake.image_url(width=800, height=600, placeholder_url=None)
