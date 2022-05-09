import pyximport; pyximport.install()
from pathlib import Path
from faker import Faker


def rename_files(dirPath):
    for f in dirPath.iterdir():
        if f.is_file() and f.suffix == ".py":
            print(f"{f=}, {f.name=}, {f.stem=} -> ", end=" ")
            f.rename(f.parent / f"{f.stem}.pyx")
            print(f"{f=}, {f.name=}, {f.stem=}")
        elif f.is_dir():
            rename_files(f)

# root = Path(r"C:\sourse\cython_playground\venv\Lib\site-packages\cfaker")
# rename_files(root)
# print("done.")


if __name__ == '__main__':
    pass