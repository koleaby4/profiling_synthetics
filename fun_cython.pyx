#!python
#cython: language_level=3

import fun_python
import fun_faker
import datetime

import pyximport
pyximport.install()


def fun_python_random_int(min: int, max: int) -> int:
    return fun_python.random_int(min=min, max=max)


def fun_faker_random_int(min: int, max: int) -> int:
    return fun_faker.random_int(min=min, max=max)


def fun_faker_random_date(year_start: int, year_end: int) -> datetime.date:
    return fun_faker.random_date(year_start, year_end)

