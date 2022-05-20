import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
from functools import partial
from typing import Union

import fun_python

PoolExecutor = Union[ThreadPoolExecutor, ProcessPoolExecutor]


def _get_chunks(records_count: int, chunk_size: int) -> list[int]:
    """
    _get_chunks(10, 3) -> [3, 3, 3, 1]
    _get_chunks(14, 4) -> [4, 4, 4, 2]
    _get_chunks(3, 5) -> [3]
    """
    n_count, remainder = divmod(records_count, chunk_size)
    return (chunk_size,) * n_count + (remainder,)


def random_dates_thread_pool(year_start: int, year_end: int, records_count: int, chunk_size: int, max_workers: int = None) -> list[datetime.date]:
    return _random_dates_process_pool(year_start, year_end, records_count, chunk_size, ThreadPoolExecutor)


def random_dates_process_pool(year_start: int, year_end: int, records_count: int, chunk_size: int, max_workers: int = None) -> list[datetime.date]:
    return _random_dates_process_pool(year_start, year_end, records_count, chunk_size, ProcessPoolExecutor)


def _random_dates_process_pool(year_start: int, year_end: int, records_count: int, chunk_size: int, pool_executor: PoolExecutor, max_workers: int = None) -> list[datetime.date]:
    if max_workers:
        pool_executor = partial(pool_executor, max_workers=max_workers)

    with pool_executor() as executor:
        chunks = _get_chunks(records_count, chunk_size)
        futures = [executor.submit(random_dates, year_start, year_end, chunk) for chunk in chunks]

        results = []
        for future in as_completed(futures):
            r = future.result()
            results.extend(r)

    return results


def random_dates(year_start: int, year_end: int, records_count: int) -> list[datetime.date]:
    return [fun_python.random_date(year_start, year_end) for _ in range(records_count)]
