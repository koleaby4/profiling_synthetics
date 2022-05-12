from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello fun cython',
    ext_modules=cythonize("fun_cython.pyx"),
    zip_safe=False,
)
