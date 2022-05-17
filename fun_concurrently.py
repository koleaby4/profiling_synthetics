import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import fun_python


def _get_chunks(records_count: int, chunk_size: int) -> list[int]:
    """
    _get_chunks(10, 3) -> [3, 3, 3, 1]
    _get_chunks(14, 4) -> [4, 4, 4, 2]
    _get_chunks(3, 5) -> [3]
    """
    n_count, remainder = divmod(records_count, chunk_size)
    return (chunk_size,) * n_count + (remainder,)


def random_dates(year_start: int, year_end: int, records_count: int) -> list[datetime.date]:
    return [fun_python.random_date(year_start, year_end) for _ in range(records_count)]


def random_dates_concurrently(year_start: int, year_end: int, records_count: int, chunk_size: int) -> list[datetime.date]:
    with ThreadPoolExecutor(max_workers=10) as thread_pool:
        chunks = _get_chunks(records_count, chunk_size)
        futures = [thread_pool.submit(random_dates, year_start, year_end, chunk) for chunk in chunks]

        results = []
        for future in as_completed(futures):
            r = future.result()
            results.extend(r)

    return results
