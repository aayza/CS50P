# Indoor Voice
def indoor():
    lower = input("Enter some text here ").lower()
    print(lower)


# indoor()


# Playback Speed
def playback():
    slow = input("Enter some text here ").replace(" ", "...")
    print(slow)


# playback()


# Making Faces
def convert(text):
    text = text.replace(":)", '🙂')
    text = text.replace(":(", '🙁')
    return text


def mainFaces():
    # get input
    face = input("Enter some text here :) ")
    # call convert method
    result = convert(face)
    # print result
    print(result)


# mainFaces()


# Einstein

def calculate(m):
    c = pow(300000000, 2)
    energy = m * c
    return energy


def mainEinstein():
    print("Calculate Energy:")
    mass = int(input("Mass: "))
    result = calculate(mass)
    print(f'Energy: {result}')


# mainEinstein()


# Tip Calculator

def mainTip():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip().replace("$", "")
    d = float(d)
    return d


def percent_to_float(p):
    p = p.strip().replace("%", "")
    p = float(p) / 100
    return p


mainTip()

