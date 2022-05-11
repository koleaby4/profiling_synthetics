from utils import profile_function
import datetime
import pyximport

pyximport.install()

dates_range = {
        "start_date": datetime.date(1950, 1, 1),
        "end_date": datetime.date(2050, 12, 31),
    }

fun_mapper = {
    "fun_python.random_date": dates_range
}


if __name__ == '__main__':

    times_to_run = 1_000_000

    for function_path, kwargs in fun_mapper.items():
        profile_function(function_path, times_to_run, **kwargs)

