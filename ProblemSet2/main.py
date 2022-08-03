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


twitter()