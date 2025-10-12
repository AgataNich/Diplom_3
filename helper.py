from faker import Faker


def generate_registration_data():
    faker = Faker()
    email = email = f"{faker.user_name()}@my_test_yandex.com"
    password = faker.password(length=10)
    name = faker.name()
    return email, password, name

