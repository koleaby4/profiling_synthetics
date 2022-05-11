from utils import profile_function


dates_range = {
        "year_start": 1950,
        "year_end": 2050,
    }

fun_mapper = {
    "fun_python.random_date": dates_range,
    "fun_faker.random_date": dates_range,
    "fun_mimesis.random_date": dates_range,
}

def main() -> None:
    times_to_run = 100_000  # dates are slow hence lower number or calls

    for function_path, kwargs in fun_mapper.items():
        profile_function(function_path, times_to_run, **kwargs)


if __name__ == '__main__':
    main()

