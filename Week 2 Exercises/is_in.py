def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) <= 1:
        return char == aStr
    middle_index = len(aStr) // 2
    middle_char = aStr[middle_index]
    if char == middle_char:
        return True
    elif char < middle_char:
        return isIn(char, aStr[:middle_index])
    else:
        return isIn(char, aStr[middle_index:])
