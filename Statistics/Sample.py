import random

def Sample(data, ss):
    random_val = random.choices(data, k=ss - 1)
    return random_val