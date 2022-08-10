def whileLoop():
    i = 0
    while i < 5:
        print("meow")
        i += 1


# whileLoop()


def forLoop():
    for _ in range(3):
        print("woof")


forLoop()


def anotherLoop():
    print("quack\n" * 3, end="")


# anotherLoop()


def validateInputLoop():
    while True:
        number = int(input("How many times did the cow moo? "))
        if number > 0:
            break

    moo(number)


def moo(n):
    for _ in range(n):
        print("Moo")


# validateInputLoop()


def loopList():
    names = ["Lee", "Aayza", "Mic"]

    for name in names:
        print(name)

    for i in range(len(names)):
        print(i + 1, names[i])


# loopList()

# Dictionary
def dicList():
    names = {
        "Aayza": "November",
        "Lee": "December",
        "Mic": "December"
    }

    for name in names:
        print(name, names[name], sep=", ")


# dicList()

# List of Dictionaries
def hash():
    names = [
        {"name": "Aayza", "month": "November", "day": "06"},
        {"name": "Lee", "month": "December", "day": "10"},
        {"name": "Mic", "month": "December", "day": "23"},
        {"name": "John", "month": "January", "day": None}
    ]

    for person in names:
        print(person["name"], person["month"], person["day"])


hash()


# Mario

