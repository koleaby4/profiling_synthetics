from dataclasses import dataclass
from pathlib import Path
from importlib import import_module
import cProfile
import pandas as pd

from typing import Callable, Any
import types
import pstats


@dataclass
class CoreStats:
    func_info: str
    total_calls: int
    total_time: float
    cumulative_time: float


def _get_header(function_name: str, calls_count: int) -> str:
    header = f"{function_name} : {calls_count:_}"
    delimiter = '-' * len(header)
    return f"{delimiter}\n{header}\n{delimiter}"


def _ensure_report_dir(dir_name: str) -> Path:
    report_dir = Path("reports") / dir_name

    if not report_dir.exists():
        report_dir.mkdir(parents=True)

    return report_dir


def profile_function(func_path: str, times_to_run: int, *args, **kwargs) -> tuple[list[Any], pstats.Stats]:
    module_name, function_name = func_path.split(".")
    module: types.ModuleType = import_module(module_name)
    fun: Callable = module.__dict__[function_name]

    report_dir: Path = _ensure_report_dir(Path(__file__).stem)
    results = []
    with cProfile.Profile() as pr:
        for i in range(times_to_run):
            results.append(fun(*args, **kwargs))

    print(_get_header(func_path, times_to_run))

    pr.dump_stats(f"{report_dir}/{func_path}_{times_to_run:_}")
    pr.print_stats()

    return results, pstats.Stats(pr).strip_dirs().sort_stats(-1)


def get_core_stats(func_path: str, ps_stats: pstats.Stats) -> CoreStats:
    module_name, func_name = func_path.split(".")
    for func_info, stats in ps_stats.stats.items():

        if func_name not in func_info[-1]:
            continue

        if module_name in func_info[0] + func_info[-1]:
            return CoreStats(func_path, stats[0], stats[2], stats[3])

    available_stats = [f"{st[0]} {st[1]} {st[2]}" for st in ps_stats.stats]
    raise ValueError(f"could not find stats for {func_path} in {available_stats}")


def render_stats(focused_stats: list[CoreStats]) -> None:
    import plotly.express as px
    func_info = []
    total_calls = []
    total_time = []
    cumulative_time = []

    for entry in focused_stats:
        func_info.append(entry.func_info)
        total_calls.append(entry.total_calls)
        total_time.append(entry.total_time)
        cumulative_time.append(entry.cumulative_time)

    data = {
        "func_info": func_info,
        "total_calls": total_calls,
        "total_time": total_time,
        "cumulative_time": cumulative_time
    }
    df = pd.DataFrame.from_dict(data)
    fig = px.line(df, x='total_calls', y='cumulative_time', color='func_info', markers=True)
    fig.show()


def profile_all_from_config(times_to_run: int, growth_rate: int, laps: int, config: dict[str, dict]) -> tuple[list[Any], list[CoreStats]]:
    core_stats = []
    results = []
    for _ in range(laps):
        times_to_run *= growth_rate
        for func_path, kwargs in config.items():
            result, ps_stats = profile_function(func_path, times_to_run, **kwargs)

            stats = get_core_stats(func_path, ps_stats)
            if max_workers := kwargs.get("max_workers"):
                stats.func_info += f"_{max_workers=}"

            core_stats.append(stats)
            results.append(result)

    return results, core_stats
