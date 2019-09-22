def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    return max(aDict.keys(), key=max)
