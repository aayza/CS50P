# Deep Thought
def mainThought():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    if check(answer):
        print("Yes")
    else:
        print("No")


def check(answer):
    match answer:
        case "42" | "fourty-two" | "fourty two":
            return True
        case _:
            return False


# mainThought()

# Home Federal Savings Bank
def mainBank():
    greeting = input("Greeting: ").casefold()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


# mainBank()

# File Extensions
def mainFile():
    file = input("File name: ")
    file, ext = file.split(".")
    checkType(ext)


def checkType(file):
    match file:
        case "gif" | "jpg" | "jpeg" | "png":
            print("image/" + file)
        case "pdf" | "zip":
            print("application/" + file)
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


# mainFile()

# Math Interpreter
def calculator():
    math = input("Expression: ")
    result = float(evaluate(math))
    print(result)


def evaluate(math):
    x, y, z = math.split(" ")
    x = int(x)
    z = int(z)
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z


# calculator()


# Meal Time
def main():
    time = input("What time is it? ")
    result = convert(time)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")
    else:
        print("no meal")



def convert(time):
    hour, minute = time.split(":")
    minute = int(minute)/60
    result = int(hour) + int(minute)
    return float(result)

main()
