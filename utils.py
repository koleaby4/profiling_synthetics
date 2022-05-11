from pathlib import Path
from importlib import import_module
import cProfile

from typing import Callable
import types


def _get_header(function_name: str, calls_count: int) -> str:
    header = f"{function_name} : {calls_count:_}"
    delimiter = '-' * len(header)
    return f"{delimiter}\n{header}\n{delimiter}"


def _assure_report_dir(dir_name: str) -> Path:
    report_dir = Path("reports") / dir_name

    if not report_dir.exists():
        report_dir.mkdir(parents=True)

    return report_dir


def profile_function(function_path: str, times_to_run: int, *args, **kwargs) -> None:
    module_name, function_name = function_path.split(".")
    module: types.ModuleType = import_module(module_name)
    fun: Callable = module.__dict__[function_name]

    report_dir: Path = _assure_report_dir(Path(__file__).stem)

    for n in [times_to_run]:
        with cProfile.Profile() as pr:
            for i in range(n):
                fun(*args, **kwargs)

        print(_get_header(function_path, n))

        pr.dump_stats(f"{report_dir}/{function_path}_{n:_}")
        pr.print_stats()
