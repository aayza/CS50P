def greater():
    x = int(input("what is x: "))
    y = int(input("what is y: "))

    if x > y:
        print("x is greater than y")
    elif x < y:
        print("x is less than y")
    else:
        print("x is equal to y")


# greater()


def equaler():
    x = int(input("what is x: "))
    y = int(input("what is y: "))

    # if x > y or x < y:
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")


# equaler()


def scoreAnd():
    score = int(input("Score: "))

    if score >= 90:
        print("Grade: A")
    elif score >= 0:
        print("Grade8: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    # if 90 <= score <= 100:
    #     print("Grade: A")
    # elif 80 <= score < 90:
    #     print("Grade: B")
    # elif 70 <= score < 80:
    #     print("Grade: C")
    # elif 60 <= score < 60:
    #     print("Grade: D")
    # else:
    #     print("Grade: F")


#  scoreAnd()


def mainEven():
    x = int(input("what is x: "))
    if is_even(x):
        print("Even")
    else:
        print("False")


def is_even(n):
    return n % 2 == 0


mainEven()
