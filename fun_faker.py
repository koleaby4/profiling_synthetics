from faker import Faker

fake = Faker()

def random_int(min, max):
    return fake.random_int(min=min, max=max)


def random_int_type_hinted(min: int, max: int) -> int:
    return fake.random_int(min=min, max=max)