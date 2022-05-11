from faker import Faker
import datetime

fake = Faker()
# fake = Faker(use_weighting=False) # this should speed things up

def random_int(min, max):
    return fake.random_int(min=min, max=max)


def random_int_type_hinted(min: int, max: int) -> int:
    return fake.random_int(min=min, max=max)


def random_date(year_start, year_end):
    start_date = datetime.date(year_start, 1, 1)
    end_date = datetime.date(year_end, 12, 31)
    return fake.date_between_dates(start_date, end_date)
