from utils import profile_all_from_config, render_stats

import pyximport

pyximport.install()


dates_range = {
    "year_start": 1950,
    "year_end": 2050,
}

config = {
    "fun_python.random_date": dates_range,
    "fun_faker.random_date": dates_range,
    "fun_mimesis.random_date": dates_range,
    "fun_cython.fun_faker_random_date": dates_range,
}


def main():
    core_stats = profile_all_from_config(10_000, 2, 5, config)
    render_stats(core_stats)


if __name__ == '__main__':
    main()
