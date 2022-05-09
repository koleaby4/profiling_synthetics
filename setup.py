from setuptools import setup
from Cython.Build import cythonize


setup(
    name='cythonized functions',
    ext_modules=cythonize("fun_cython.pyx"),
    zip_safe=False,
)