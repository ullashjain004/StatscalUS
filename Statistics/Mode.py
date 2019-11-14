def mode(numbers):
    length = len(numbers)
    modelst = []
    for q in range(0, length, 1):
        modelst.append(numbers.count(numbers[q]))
    p = max(modelst)
    for x in numbers:
        if numbers.count(x) == p:
            return x