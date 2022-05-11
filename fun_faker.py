from faker import Faker
import datetime

fake = Faker()
weightless_fake = Faker(use_weighting=False) # this might speed things up


def random_int(min: int, max: int) -> int:
    return fake.random_int(min=min, max=max)


def random_int_type_hinted(min: int, max: int) -> int:
    return fake.random_int(min=min, max=max)


def random_date(year_start: int, year_end: int, f: Faker = fake) -> datetime.date:
    start_date = datetime.date(year_start, 1, 1)
    end_date = datetime.date(year_end, 12, 31)
    return f.date_between_dates(start_date, end_date)


def random_date_weightless(year_start: int, year_end: int) -> datetime.date:
    return random_date(year_start, year_end, weightless_fake)
