def isWordGuessed(secretWord: str, lettersGuessed: list) -> bool:
    """
    secretWord: the word the user is guessing.

    lettersGuessed: letters that have been guessed so far

    returns: True if all the letters of secretWord are in
    lettersGuessed; False otherwise.
    """
    return set(lettersGuessed).issuperset(secretWord)
