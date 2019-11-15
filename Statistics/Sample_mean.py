from Statistics.Mean import mean
from Statistics.Sample import sample

import random
import statistics


def sample_mean(val):
    ms = random.randint(1, len(val))
    val_new = sample(val, ms)
    p = round(mean(val_new), 2)
    true_mean = round(statistics.mean(val_new), 2)
    return p, true_mean