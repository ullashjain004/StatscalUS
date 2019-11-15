from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import sub
from Calculator.Square import square
from Calculator.sqroot import sqroot
from Statistics.Sample import sample
from Statistics.Mean import mean
import random
from Statistics.StandardDeviation import stddev


def sample_std_dev(val):
    ssd = random.randint(1, len(val))
    val_new = sample(val, ssd)



    p = 0
    q = 0
    length = len(val_new)
    for i in range(0, length, 1):
        p = sub(val_new[i], mean(val_new))
        q = addition(square(p), q)
    x = division(sub(1, length), q)
    true_sd = stddev(val_new)
    return sqroot(x), true_sd