from Calculator.Addition import addition
from Calculator.Division import division


def median(numbers):
    length = len(numbers)
    numbers.sort()
    if length % 2 == 0:
        med_1st = numbers[int(division(2, length))]
        med_2nd = numbers[len(numbers) // 2 - 1]
        mid = division(2, addition(med_1st, med_2nd))
    else:
        mid = numbers[division(2, length)]
    return mid
