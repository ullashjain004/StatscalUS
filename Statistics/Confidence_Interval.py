from Statistics.Mean import mean
from Statistics.StandardDeviation import stddev
from Calculator.sqroot import sqroot
from Calculator.Multiplication import multiply
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import sub


def confi_int(val):
    x = mean(val)
    confidence_level = 0.95
    y = (1-confidence_level) / 2
    std = stddev(val)
    n = sqroot(len(val))
    return [sub(multiply(division(n, std), y), x), addition(multiply(division(n, std), y), x)]
