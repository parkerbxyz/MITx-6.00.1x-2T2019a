from math import tan, pi


def polysum(n: int, s: int) -> float:
    """
    n: number of sides,
    s: length of sides

    Return the sum of the area and square of the perimeter
    of the regular polygon, rounded to 4 decimal places.
    """
    area = (0.25 * n * s**2)/(tan(pi/n))
    perimeter = n * s
    return round(area + perimeter**2, 4)
