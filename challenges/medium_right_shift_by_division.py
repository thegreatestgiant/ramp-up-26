def shift(x, y):
    if y == 0:
        return x
    else:
        return shift(x // 2, y - 1)
