import random as r

import numpy as np


def alpha(num):
    count = 1
    while count < num:
        print(count)
        count += 1


def bravo():
    total = 0
    for i in range(1, 10 + 1):
        total += i
    return total


def charlie(x):
    for s in x:
        print(np.cbrt(s))


def delta():
    while True:
        age = int(input("What's you age?"))
        if not (age < 0 or age > 100):
            break
        print("use a valid age please")
    return age


def echo():
    with open("theFile.txt", "w") as file:
        for x in [r.randint(1, 40) for _ in range(20)]:
            file.write(x)


def foxtrot(number):
    return number * 2


def fav_color():
    color = input("What's your favorate color?")
    color = color.tolower()
    if color == "blue":
        print("Great choice.")
    elif color == "red":
        print("Poor choice.")
    elif color == "green":
        print("Not a bad choice.")
    else:
        print("Sorry, that's not a primary color.")


def fav_color2():
    color = input("What's your favorate color?")
    match color.tolower():
        case "blue":
            print("Great choice.")
        case "red":
            print("Poor choice.")
        case "green":
            print("Not a bad choice.")
        case _:
            print("Sorry, that's not a primary color.")


def rand():
    num = r.randint(1, 101)
    if num < 50:
        print("You chose a number less than 50.")
    else:
        print("You chose a number more than 50.")


def golf():
    return r.randint(1, 6)


def hotel():
    d1, d2 = 1, 3
    total = 0
    while d1 != d2:
        d1, d2 = golf(), golf()
        total += 1
    print(f"It took {total} rolls")
    return total


def india(x):
    for i in x:
        if x % 2 == 0:
            print(0)
        else:
            print(1)


def juliett(x):
    if x % 2 == 0:
        return True
    return False


def kilo(x):
    with open("theFile.txt", "w") as file:
        for i in x:
            file.write(i / 2)


def pay():
    PAY_RATE = 50
    HOURS_WORKED = int(input("How many hourse did you work?"))
    output = (PAY_RATE * HOURS_WORKED) if HOURS_WORKED > 10 else 0
    print(output)


def lima(name, age):
    count = 0
    while count < 3:
        name = input("WHat's your name?")
        age = int(input("What's your age"))
        if age >= 0 or age <= 100:
            return
    age = 0


def conv():
    for i in range(-20, 20):
        print("C is", i)
        print("F is", (9 / 5) * i + 32)


def fib():
    f1, f2 = 1, 1
    print(f1)
    print(f2)
    for _ in range(18):
        f1, f2 = f2, f1 + f2
        print(f2)


def mike(number):
    if number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


def november(grade):
    if grade < 70:
        print("You did not pass")
    elif grade < 80:
        print("You got a C")
    elif grade < 90:
        print("You got a B")
    elif grade <= 100:
        print("You got a C")


def main():
    age = delta()
    prev = 1
    for _ in range(11):
        print(prev)
        prev = foxtrot(prev)
