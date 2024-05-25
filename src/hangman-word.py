# imports
from words import words
import hangman as hm  # alias to type hm.evaluate instead of hangman.evaluate
import random  # don't use this except as given

# additional functions for word-based hangman if necessary

if __name__ == "__main__":
    secret = random.choice(words).lower()
    # TODO initialize anything else needed
    # TODO set up game loop
