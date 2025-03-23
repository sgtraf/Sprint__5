import pytest
import random
from faker import Faker

fake = Faker()

@pytest.fixture
# фикстура, которая генерирует логин
def generate_random_email():
    return fake.email()

