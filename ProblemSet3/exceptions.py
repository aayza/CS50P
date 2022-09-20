def number():
    x = getInt("whats x? ")
    print(f"x is {x}")


def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            print("x is not an integer")


number()
