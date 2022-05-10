import datetime
import random
from random import randint


def random_int(min, max):
    return randint(min, max)


def random_int_type_hinted(min: int, max: int) -> int:
    return randint(min, max)


def random_date(start_date=None, end_date=None, max_delta_days=365 * 70):
    if start_date and end_date:
        delta_days = (end_date - start_date).days
        random_days = random.randint(1, min(delta_days, max_delta_days))
        return start_date + datetime.timedelta(days=random_days)

    if start_date is not None and end_date is None:
        random_delta_days = random.randint(1, max_delta_days)
        return start_date + datetime.timedelta(days=random_delta_days)

    if start_date is None and end_date is not None:
        random_delta_days = random.randint(1, max_delta_days)
        return end_date - datetime.timedelta(days=random_delta_days)

    if start_date is None and end_date is None:
        today = datetime.datetime.now()

        random_delta_days = random.randint(-max_delta_days, max_delta_days)
        return today + datetime.timedelta(days=random_delta_days)
