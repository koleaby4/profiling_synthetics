from utils import profile_all_from_config, render_stats

args = {
    "year_start": 1950,
    "year_end": 2050,
    "records_count": 100_000
}


def main():
    core_stats = []

    for i in range(10):
        args["records_count"] *= 2

        config = {
            "fun_concurrently.random_dates": args,
            "fun_concurrently.random_dates_thread_pool": {**args, "chunk_size": 1_000_000},
            "fun_concurrently.random_dates_process_pool": {**args, "chunk_size": 1_000_000}
        }
        results = profile_all_from_config(1, 1, 1, config)
        for r in results:
            r.total_calls = args["records_count"]

        core_stats.extend(results)

    render_stats(core_stats)


if __name__ == '__main__':
    main()
