def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """
    return sum(len(value) for value in aDict.values())
