def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    result = min(a, b)
    while result > 1:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result
