# Types of fake data generated

1. integers
2. strings
3. dates

# Options looked at

1. plain Python ('random' library)
2. [faker](https://faker.readthedocs.io/en/master/)
3. [mimesis](https://mimesis.name/en/master/)
4. [cython](https://cython.readthedocs.io/en/latest/)
5. [mypyc](https://mypyc.readthedocs.io/en/latest)
6. using [ctypes](https://docs.python.org/3/library/ctypes.html) to run high-performance (c?) fakers

# How do we measure?

We use standard Python [cprofile](https://docs.python.org/3/library/profile.html#module-cProfile) module to measure performance.

# Useful commands

* `pip install -r requirements.txt` to install dependencies 
* to profile various generation methods:
  * `python driver_numbers.py` 
  * `python driver_dates.py` 