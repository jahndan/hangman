# imports
from phrases import phrases
import random

# additional functions for phrase-based hangman if necessary

if __name__ == "__main__":
    secret = random.choice(phrases).lower()
    # print stuff to play game
