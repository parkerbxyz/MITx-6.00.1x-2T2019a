def getGuessedWord(secretWord: str, lettersGuessed: list) -> str:
    """
    secretWord: the word the user is guessing

    lettersGuessed: letters that have been guessed so far

    returns: string, comprised of letters and underscores that
    represents what letters in secretWord have been guessed so far.
    """
    return ' '.join(letter if letter in lettersGuessed else '_'
                    for letter in secretWord)
