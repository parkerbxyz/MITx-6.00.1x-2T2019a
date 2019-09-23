from problem_1 import isWordGuessed
from problem_2 import getGuessedWord
from problem_3 import getAvailableLetters


def hangman(secretWord: str):
    """
    secretWord: the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses_left = 8
    letters_guessed = []  # type: list
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long"
          .format(len(secretWord)))
    while guesses_left >= 0:
        print("-----------")
        if guesses_left == 0:
            print("Sorry, you ran out of guesses. The word was {}."
                  .format(secretWord))
            break
        if isWordGuessed(secretWord, letters_guessed):
            print("Congratulations, you won!")
            break
        print("You have {} guesses left".format(guesses_left))
        print("Available Letters: {}"
              .format(getAvailableLetters(letters_guessed)))
        guess = input("Please guess a letter: ")
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter: {}"
                  .format(getGuessedWord(secretWord, letters_guessed)))
        else:
            letters_guessed += guess
            if guess in secretWord:
                print("Good guess: {}"
                      .format(getGuessedWord(secretWord, letters_guessed)))
            else:
                letters_guessed += guess
                guesses_left -= 1
                print("Oops! That letter is not in my word: {}"
                      .format(getGuessedWord(secretWord, letters_guessed)))
