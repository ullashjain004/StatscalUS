from Calculator.Division import division
from Calculator.Subtraction import sub

from Statistics.Mean import mean
from Statistics.StandardDeviation import stddev


def Zscore(val):
    m = mean(val)
    z = stddev(val)
    length = len(val)
    score = []
    for p in range(0, length, 1):
        zsc = 0
        zsc = round(float(division(z, sub(m, val[p]))), 3)
        score.append(zsc)
    return score