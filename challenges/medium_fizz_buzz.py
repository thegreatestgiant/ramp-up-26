def fizzbuzz(x):
    m3 = x % 3 == 0
    m5 = x % 5 == 0
    f = "Fizz"
    b = "Buzz"
    if m3 and m5:
        return f + b
    if m3:
        return f
    if m5:
        return b
    return str(x)
