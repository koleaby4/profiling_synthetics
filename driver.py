import cProfile
from importlib import import_module
from pathlib import Path

fun_mapper = {
    "fun_python.random_int": {
        "min": 1,
        "max": 10_000
    },

    "fun_python.random_int_type_hinted": {
        "min": 1,
        "max": 10_000
    },

    "fun_faker.random_int": {
        "min": 1,
        "max": 10_000
    },

    "fun_cython.fun_python_random_int": {
        "min": 1,
        "max": 10_000
    },

    "fun_cython.fun_python_random_int_type_hinted": {
        "min": 1,
        "max": 10_000
    },

    "fun_cython.fun_faker_random_int": {
        "min": 1,
        "max": 10_000
    },

    "fun_cython.fun_faker_random_int_type_hinted": {
        "min": 1,
        "max": 10_000
    }
}


if __name__ == '__main__':
    REPORTS_DIR = "reports"

    reports_path = Path(REPORTS_DIR)
    if not reports_path.exists():
        reports_path.mkdir()

    for function_path, kwargs in fun_mapper.items():
        module_name, function_name = function_path.split(".")
        module = import_module(module_name)
        fun = module.__dict__[function_name]

        for n in [1_000_000]:
            with cProfile.Profile() as pr:
                for i in range(n):
                    fun(**kwargs)

            print(f"\n{'-' * 50 } -> {function_path} : {n:_}\n")
            pr.dump_stats(f"{REPORTS_DIR}/{function_path}_{n:_}")
            # p = pstats.Stats(stats_file)
            # p.strip_dirs().sort_stats(-1).print_stats()
            pr.print_stats()



