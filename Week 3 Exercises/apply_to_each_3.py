# testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def squared(number):
    return number * number


applyToEach(testList, squared)
