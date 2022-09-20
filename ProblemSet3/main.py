# Fuel Gauge
def fractionPrompt():
    XY = input("What faction is fuel at? ")
    return XY


def getFraction():
    while True:
        try:
            XY = fractionPrompt()
            XY = XY.split("/")
            x = int(XY[0])
            y = int(XY[1])
        except ValueError:
            pass
            print("Not inputted correctly")
        else:
            giveResult(x, y)
            break


def giveResult(x, y):
    try:
        result = (x / y) * 100
    except ZeroDivisionError:
        pass
        print("Cannot be divided by 0")
    else:
        if result >= 99:
            print("F")
        elif result <= 1:
            print("E")
        else:
            print(f"{result}%")


# getFraction()


# Felipe’s Taqueria

def felipe():
    menu = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }

# while exit not pressed
    while True:
        # get order input from user - make title
        order = input("Place an order ").title()
        # try to get value from hash
        try:
            cost = menu[order]
        except KeyError:
            pass
    # if key not in hash raise error and message (ignore and repeat)
        else:
            print(f"${cost}")



felipe()
# Grocery List


# Outdated
