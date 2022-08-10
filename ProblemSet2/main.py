# camelCase
def camelCase():
    variable = input("camelCase: ")
    # For each char in variable
    result = ""
    for i in variable:
        # check if upper
        if i.isupper():
            # add _ just before upper and make upper lower
            i = "_{0}".format(i)
            i = i.lower()
        # combine all char in list into str
        result = result + i
        # return str as snake
    print("snake_case: " + result)


# camelCase()

# Coke Machine
def coke_machine():
    print("Only 25p, 10p and 5p accepted")
    cost = 50
    # until cost is fulfilled
    while cost > 0:
        print("Amount Due: " + str(cost))
        coin = input("Insert Coin: ")
        match coin:
            case "25" | "10" | "5":
                cost = cost - int(coin)

    if cost < 0:
        cost = -cost
    print("Change owed: " + str(cost))


# coke_machine()


# Twttr
def twitter():
    text = input("Input: ")
    result = ""
    for vowel in text:
        match vowel.casefold():
            case "a" | "i" | "e" | "o" | "u":
                vowel = ""

        result = result + vowel
    print("Output: " + result)


# twitter()


# Vanity Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 < len(s) < 6 and s[0:2].isalpha() and s.isalnum():
        length = len(s)
        firstDigit = None
        for char in range(len(s)):
            if s[char].isdigit() and char < length - 1:
                if firstDigit is None:
                    firstDigit = s[char]
                    if firstDigit == '0':
                        return False
                if s[char + 1].isalpha():
                    return False
        return True
    else:
        return False

# main()

# Nutrition Facts

def checkFruit():

    fruits = {
        "Apple": "130",
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50"
    }

    variable = input("Fruit: ").title()
    if variable in fruits:
        for cals in fruits:
            if cals == variable:
                print("calories: ", fruits[cals])


checkFruit()