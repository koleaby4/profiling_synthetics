from utils import profile_all_from_config, render_stats

import pyximport
pyximport.install()

int_min_max = {
    "min": 1,
    "max": 10_000_000
}

config = {
    "fun_python.random_int": int_min_max,
    "fun_faker.random_int": int_min_max,
    "fun_mimesis.random_int": int_min_max,
    "fun_cython.fun_python_random_int": int_min_max,
    "fun_cython.fun_faker_random_int": int_min_max,
}


def main() -> None:
    results, core_stats = profile_all_from_config(50_000, 2, 5, config)
    render_stats(core_stats)


if __name__ == '__main__':
    main()
