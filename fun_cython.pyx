#!python
#cython: language_level=3

import fun_python
import fun_faker

import pyximport
pyximport.install()


def fun_python_random_int(min: int, max: int) -> int:
    return fun_python.random_int(min=min, max=max)


def fun_faker_random_int(min: int, max: int) -> int:
    return fun_faker.random_int(min=min, max=max)

