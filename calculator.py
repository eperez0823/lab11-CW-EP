# https://github.com/eperez0823/lab11-CW-EP
# Partner 1: Christopher Wilches
# Partner 2: Esteban Perez

import math


def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)
    except ValueError:
        raise


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (TypeError, ValueError):
        raise

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm")
    return math.log(b, a)


def exp(a, b):
    return a ** b
