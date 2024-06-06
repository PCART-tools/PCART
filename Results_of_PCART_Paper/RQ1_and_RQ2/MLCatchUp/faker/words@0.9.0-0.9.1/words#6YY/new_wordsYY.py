from faker import Faker
fake = Faker()
words = fake.words(nb=5, ext_word_list=['apple', 'banana', 'orange'], unique=False)
