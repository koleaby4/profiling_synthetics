from mimesis.random import Random

random = Random()


def random_int(min, max):
    return random.randint(min, max)


def random_ints(amount, min, max):
    return random.randints(amount, min, max)
