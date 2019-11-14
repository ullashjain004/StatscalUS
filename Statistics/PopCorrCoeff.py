from Statistics.Zscore import Zscore

def pop_corr_coef(val, val1):
    x1 = Zscore(val)
    x2 = Zscore(val1)
    x1_x2 = list(map(lambda x, y: x * y, x1, x2))
    y = sum(x1_x2) / len(x1_x2)
    return y