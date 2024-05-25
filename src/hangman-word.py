# imports
from words import words
import hangman as hm
import random

# additional functions for word-based hangman if necessary

if __name__ == "__main__":
    secret = random.choice(words).lower()
    playing = True
    lives = LIVES = 10
    guesses = set()

    WIDTH = 50
    while playing:
        print()  # prints blank line
        print("=" * WIDTH)
        hm.display_guesses(guesses, secret)  # default indent size is already 1
        hm.display_lives(lives, LIVES)  # default indent size is already 1
        print("=" * WIDTH)
        print()
        hm.display_partial_word(guesses, secret)
        print()
        guess = hm.game_prompt(guesses)  # prompt for a guess and add it to the set
        # classic pattern for dealing with immutable things
        # note: only guesses and lives depend on their previous values
        guesses, lives, playing = hm.evaluate(guesses, lives, guess, secret)
    hm.display_partial_word(guesses, secret)
    if lives > 0:
        print("You won with {} lives!".format(lives))
    else:
        print("You lost! The answer was: {}.".format(secret))
