import datetime
import random
from random import randint


def random_int(min: int, max: int) -> int:
    return randint(min, max)


def random_date(year_start: int, year_end: int) -> datetime.date:
    start_date = datetime.date(year_start, 1, 1)
    end_date = datetime.date(year_end, 12, 31)
    delta_days = (end_date - start_date).days
    random_days = random.randint(1, delta_days)
    return start_date + datetime.timedelta(days=random_days)