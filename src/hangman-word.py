# imports
from words import words
import random

# additional functions for phrase-based hangman if necessary

if __name__ == "__main__":
    secret = random.choice(words).lower()
    # print stuff to play game
