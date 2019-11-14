from Calculator.Addition import addition
from Calculator.Division import division


def mean(numbers):
    length = len(numbers)
    t = 0
    for x in range(0, length, 1):
        t = float(addition(t, numbers[x]))
    z = float(division(length, t))
    return z