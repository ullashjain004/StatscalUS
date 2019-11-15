from Statistics.Proportion import prop
from Statistics.variance import variance
from Calculator.Subtraction import sub
from Calculator.Multiplication import multiply
from Calculator.Division import division


def var_of_pop_prop(numbers):
    length = len(numbers)
    prop_1 = prop(numbers)
    prop_2 = sub(prop_1, 1)
    x = multiply(prop_1, prop_2)
    var_of_Pop = division(x, length)
    return var_of_Pop