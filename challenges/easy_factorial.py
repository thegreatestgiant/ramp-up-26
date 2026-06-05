def fact(x):
    total = 1
    for i in range(x, 0, -1):
        total *= i
    return total
