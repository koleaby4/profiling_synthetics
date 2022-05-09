# Types of fake data generated

1. integers
2. strings
3. dates

# Options looked at

1. plain Python ('random' library)
2. [faker](https://faker.readthedocs.io/en/master/)
3. [cython](https://cython.readthedocs.io/en/latest/)
4. [mypyc](https://mypyc.readthedocs.io/en/latest)
5. using [ctypes](https://docs.python.org/3/library/ctypes.html) to run high-performance (c?) fakers

# How do we measure?

We use standard Python [cprofile](https://docs.python.org/3/library/profile.html#module-cProfile) module to measure performance.

# Useful commands

* `python setup.py build_ext --inplace` to build cython code