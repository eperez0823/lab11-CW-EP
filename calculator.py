
# https://github.com/eperez0823/lab11-EP-CW.git
# Partner 1: Esteban Perez
# Partner 2: Christopher

import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)


def exponent(a, b):
    return a ** b


print(add(2, 3))
print(subtract(10, 4))
print(multiply(3, 5))
print(divide(2, 10))
print(logarithm(2, 8))
print(exponent(2, 3))
print(square_root(25))
print(hypotenuse(3, 4))
print(square_root(-1))