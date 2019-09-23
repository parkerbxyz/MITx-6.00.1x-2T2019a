# -----------------------------------
# Helper code

import random

from typing import List
from problem_4 import hangman

WORDLIST_FILENAME = 'words.txt'


def loadWords() -> List[str]:
    """
    Returns a list of valid words.
    Words are strings of lowercase letters.

    Depending on the size of the word list,
    this function may take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist: List[str]) -> str:
    """
    wordlist: a list of words

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

# Pick a secret word for the player to guess
secretWord = chooseWord(wordlist).lower()

# Run the game
hangman(secretWord)
