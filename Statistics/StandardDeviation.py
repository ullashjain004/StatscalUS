from Calculator.Addition import addition
from Calculator.Subtraction import sub
from Calculator.Square import square
from Calculator.sqroot import sqroot
from Calculator.Division import division


from Statistics.Mean import mean


def stddev(numbers):
    length = len(numbers)
    y = 0
    n = 0
    for p in range(0, length, 1):
        y = sub(mean(numbers), numbers[p])
        n = addition(square(y), n)
    x = division((length - 1), n)
    return sqroot(x)
