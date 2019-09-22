# testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def plus_one(number):
    return number + 1


applyToEach(testList, plus_one)
