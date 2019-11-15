from Calculator.Division import division
from Calculator.Addition import addition


def prop(val):
    q = 0

    for p in val:
        if (p % 2) == 0:
            q = addition(q, 1)
        Prop_ans = division(len(val),q)
    return Prop_ans
