from utils import profile_all_from_config, render_stats
import psutil


def main():
    core_stats = []

    config = {
        "fun_concurrently.random_dates_process_pool": {
            "year_start": 1950,
            "year_end": 2050,
            "records_count": 150_000_000,
            "chunk_size": 1_000_000
        }
    }

    physical_cores = psutil.cpu_count(logical=False)
    for i in range(0, physical_cores + 1, 2):
        args = config["fun_concurrently.random_dates_process_pool"]
        if i > 0:  # default configuration for 0; else -> explicitly set a limit
            args["max_workers"] = i

        results, stats = profile_all_from_config(1, 1, 1, config)
        for s in stats:
            s.total_calls = args["records_count"]
            core_stats.extend(stats)

    render_stats(core_stats)


if __name__ == '__main__':
    main()
