from random import randint


def random_int(min, max):
    return randint(min, max)


def random_int_type_hinted(min: int, max: int) -> int:
    return randint(min, max)