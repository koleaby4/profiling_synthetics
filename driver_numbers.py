import cProfile
from importlib import import_module
from pathlib import Path

from utils import profile_function

int_min_max = {
        "min": 1,
        "max": 10_000
    }

fun_mapper = {
    "fun_python.random_int": int_min_max,
    "fun_faker.random_int": int_min_max,
    "fun_mimesis.random_int": int_min_max,

    # "fun_cython.fun_python_random_int": int_min_max,
    # "fun_cython.fun_python_random_int_type_hinted": int_min_max,
    # "fun_cython.fun_faker_random_int": int_min_max,
    # "fun_cython.fun_faker_random_int_type_hinted": int_min_max
}


if __name__ == '__main__':

    times_to_run = 1_000_000

    for function_path, kwargs in fun_mapper.items():
        profile_function(function_path, times_to_run, **kwargs)

    mimesis_args = {
        "amount": times_to_run,
        **int_min_max
    }

    profile_function("fun_mimesis.random_ints", 1, **mimesis_args)
