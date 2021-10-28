import math


def area(r):
    a = math.pi * r ** 2
    return a


print(area(2))


# Task 4
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


print(compare(12, 12))


# Task 5
def test_is_valid(test):
    if isinstance(test, int):
        if test > 1 & test < 10:
            return "true"
        else:
            return "false"
    else:
        print("Enter a valid number!")


print(test_is_valid(9.1))
