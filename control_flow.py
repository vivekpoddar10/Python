"""
    If, elif, else
    for, while loop
        break, continue, pass
    match statement
"""


def findLarges(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximum")
    elif a < b and a > c:
        print(f"{b} is max")
    elif a > b and a < c:
        print(f"{c} is max")


lists = [1, 2, 3, 4, 5]
for item in lists:
    if item == 3:
        continue
    elif item == 4:
        break
    print(item, end=" ")


def greet(day):
    match day:
        case "monday":
            print("Hola it's monday")
        case "tuesday":
            print("oh it's tuesday")
        case _:
            print("it's other day")


greet(1)
