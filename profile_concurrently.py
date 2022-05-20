from utils import profile_all_from_config, render_stats
import psutil

# /!\ this file is more complex that other profilers.
# if you are after a straightforward scenario - don't use this one

args = {
    "year_start": 1950,
    "year_end": 2050,
    "records_count": 100_000
}


def main():
    core_stats = []

    # how many iterations we want to run
    for i in range(2):
        # multiplication factor for records_count
        args["records_count"] *= 2

        config = {
            "fun_concurrently.random_dates": args,
            "fun_concurrently.random_dates_thread_pool": {**args, "chunk_size": 1_000_000},
            # "fun_concurrently.random_dates_process_pool": {**args, "chunk_size": 1_000_000},
        }
        results, stats = profile_all_from_config(1, 1, 1, config)
        for s in stats:
            s.total_calls = args["records_count"]
        core_stats.extend(stats)

    # now with different 'max_workers' and a constant number of records
    # this is to see the effect of explicitly setting the number of processes
    args["records_count"] = 100_000_000
    config = {"fun_concurrently.random_dates_process_pool": {**args, "chunk_size": 1_000_000}}

    physical_cores = psutil.cpu_count(logical=False)
    for i in range(0, physical_cores + 1, 2):
        
        if i > 0:  # use default for 0
            config["fun_concurrently.random_dates_process_pool"]["max_workers"] = i

        results, stats = profile_all_from_config(1, 1, 1, config)
        for s in stats:
            s.total_calls = args["records_count"]
            core_stats.extend(stats)

    render_stats(core_stats)


if __name__ == '__main__':
    main()
