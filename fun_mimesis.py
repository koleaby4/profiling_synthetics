from mimesis.random import Random
from mimesis import Datetime

from typing import List
import datetime

random = Random()
mimesis_datetime = Datetime()


def random_int(min: int, max: int) -> int:
    return random.randint(min, max)


def random_ints(amount: int, min: int, max: int) -> List[int]:
    return random.randints(amount, min, max)


def random_date(year_start: int, year_end: int) -> datetime.date:
    return mimesis_datetime.date(year_start, year_end)

