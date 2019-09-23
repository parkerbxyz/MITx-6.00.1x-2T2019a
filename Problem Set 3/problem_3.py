from string import ascii_lowercase


def getAvailableLetters(lettersGuessed: list) -> str:
    """
    lettersGuessed: letters that have been guessed so far

    returns: string, comprised of letters that represents
    what letters have not yet been guessed.
    """
    return ''.join(letter if letter not in lettersGuessed
                   else '' for letter in ascii_lowercase)
