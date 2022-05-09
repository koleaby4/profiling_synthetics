#!python
#cython: language_level=3

import fun_python
import fun_faker


def fun_python_random_int(min, max):
    return fun_python.random_int(min=min, max=max)


def fun_python_random_int_type_hinted(min: int, max: int) -> int:
    return fun_python.random_int_type_hinted(min=min, max=max)


def fun_faker_random_int(min, max):
    return fun_faker.random_int(min=min, max=max)


def fun_faker_random_int_type_hinted(min: int, max: int) -> int:
    return fun_faker.random_int(min=min, max=max)
