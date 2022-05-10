import cProfile
from importlib import import_module
from pathlib import Path

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


def _get_header(function_name, calls_count):
    header = f"{function_name} : {calls_count:_}"
    delimiter = '-' * len(header)
    return f"{delimiter}\n{header}\n{delimiter}"


def _assure_report_dir(dir_name):
    report_dir = Path("reports") / dir_name

    if not report_dir.exists():
        report_dir.mkdir(parents=True)

    return report_dir


def profile_function(function_path, times_to_run, *args, **kwargs):
    module_name, function_name = function_path.split(".")
    module = import_module(module_name)
    fun = module.__dict__[function_name]

    report_dir = _assure_report_dir(Path(__file__).stem)

    for n in [times_to_run]:
        with cProfile.Profile() as pr:
            for i in range(n):
                fun(*args, **kwargs)

        print(_get_header(function_path, n))

        pr.dump_stats(f"{report_dir}/{function_path}_{n:_}")
        pr.print_stats()


if __name__ == '__main__':

    times_to_run = 1_000_000

    for function_path, kwargs in fun_mapper.items():
        profile_function(function_path, times_to_run, **kwargs)

    mimesis_args = {
        "amount": times_to_run,
        **int_min_max
    }

    profile_function("fun_mimesis.random_ints", 1, **mimesis_args)
