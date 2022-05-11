# Types of fake data generated

1. integers
2. strings
3. dates

# Options looked at

1. plain Python ('random' library and custom Python functions)
2. [faker](https://faker.readthedocs.io/en/master/) - widely used Faker library
3. [mimesis](https://mimesis.name/en/master/) - performance optimised Faker library
4. [cython](https://cython.readthedocs.io/en/latest/) - creating C extensions from Python code  
5. [mypyc](https://mypyc.readthedocs.io/en/latest) - leveraging type hints for compiling Python code to C extensions 
6. using [ctypes](https://docs.python.org/3/library/ctypes.html) to run high-performance (c?) fakers

# How do we measure?

We use standard Python [cprofile](https://docs.python.org/3/library/profile.html#module-cProfile) module to measure performance.

# Useful commands

* `pip install -r requirements.txt` to install dependencies 
* to profile various generation methods:
  * `python driver_numbers.py` 
  * `python driver_dates.py` 
* to run using `mypyc` optimisations:
  1. `mypyc driver_numbers.py`
  1. `python -d "import driver_numbers; driver_numbers.main()"`