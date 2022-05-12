#!python
#cython: language_level=3
from faker import Faker

import fun_python
import fun_faker
import datetime

# import pyximport
# pyximport.install()

fake = Faker()

def fun_python_random_int(min: int, max: int) -> int:
    return fun_python.random_int(min=min, max=max)


def fun_faker_random_int(min: int, max: int) -> int:
    return fun_faker.random_int(min=min, max=max)


def fun_faker_random_date(year_start: int, year_end: int) -> datetime.date:
    start_date = datetime.date(year_start, 1, 1)
    end_date = datetime.date(year_end, 12, 31)
    try:
        return fake.date_between_dates(start_date, end_date)
    except OSError:
        print("Ops, failed to pick a date...")
        return fun_faker_random_date(year_start, year_end)


