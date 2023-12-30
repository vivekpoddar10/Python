from calculator import square
import random

"""
    using pytest package for testing this code
        syntax: python -m pytest .\test_calculator.py

    using black package for formatting this code
        syntax: python -m black .\test_calculator.py
"""


def test_zero():
    assert square(0) == 0


def test_square():
    n = random.randint(-10, 10)
    # if n * n == square(n):
    #     print(f'output match for {n}')
    # elif n * n != square(n):
    #     print(f'output don\'t match for {n}')
    assert square(n) == n * n
