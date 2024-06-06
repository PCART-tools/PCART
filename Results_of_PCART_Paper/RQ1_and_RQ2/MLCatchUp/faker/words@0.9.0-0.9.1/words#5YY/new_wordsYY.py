from faker import Faker
fake = Faker()
words = fake.words(5, ext_word_list=['apple', 'banana', 'orange'], unique=False)
