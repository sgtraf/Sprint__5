from faker import Faker

fake = Faker()
def generate_random_email():
    return fake.email()