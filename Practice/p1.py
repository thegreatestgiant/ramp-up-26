# interest rate, principal, and number of year's
def compound_interest():
    ir = int(input("What is the interest rate? "))
    principle = int(input("What is the initial principle? "))
    time = int(input("How many years is this for? "))
    amount = principle * (1 + ir) ^ time
    print(amount)


# It asked for both at the same time.
def name_age_validater():
    counter = 0
    good = False
    while counter < 3:
        name = input("What is your name")
        ageStr = input("What is your age")
        age = int(ageStr)
        if name.isalpha() and ageStr.isnumeric() and (age > 0 and age <= 100):
            good = True
            print("Acceptable")
    if not good:
        print("Unacceptable")


def password():
    while True:
        password = input(
            "Give me a valid password. Length of at least 8, with a special, number, upper, and lower: "
        )
        bad = False
        if len(password) < 8:
            bad = True
            print("Must be at least 8 characters long")
        if not password.isalnum():
            bad = True
            print("Must contain a special character")
        if any(char.islower() for char in password):
            bad = True
            print("Must contain a lower case character")
        if any(char.isupper() for char in password):
            bad = True
            print("Must contain a upper case character")
        if any(char.isnumeric() for char in password):
            bad = True
            print("Must contain a number")
        if not bad:
            break
        print("You're getting another attempt because you failed")


def digit3():
    for i in range(1, 1_001):
        num = str(i)
        if "3" in num:
            print(i, end=" | ")


def even_back():
    for i in range(100, 0, -1):
        if i % 2 == 0:
            print(i)


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primeNums():
    for i in range(100, 1001):
        if isPrime(i):
            print(i, end=" | ")
