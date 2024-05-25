# imports
from phrases import phrases
import hangman as hm  # alias to type hm.evaluate instead of hangman.evaluate
import random  # don't use this except as given

# additional functions for phrase-based hangman if necessary

if __name__ == "__main__":
    secret = random.choice(phrases).lower()
    # TODO initialize anything else needed
    # TODO set up game loop
