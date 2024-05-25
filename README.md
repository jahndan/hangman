# Terminal-based Hangman

A quick project to make the game Hangman playable within the terminal. Since this is displayed in the terminal, there will be no graphic of a man being hung. (Not to mention that it's a pretty morbid visual for a children's game anyway.)

This project has no dependencies, and as such does not actually need `pipenv`.
It can be run simply with `python` in the command line. (Depending on your system, you may need to use `python3` instead of `python`.)

```
python src/hangman-word.py
```

```
python src/hangman-phrase.py
```

Hangman can be played with words or phrases, and this project provides lists of both for convenience. The words chosen are relatively difficult hangman words, and as such the player is given 10 lives by default—phrases usually are not, so the player gets 5 lives by default.

This branch `template` is intended as a starter template for programmers unfamiliar with python to get acquainted with python and its built-in data structures. **A playable version of this based on my solution is available on the other branch** `solution`**.**

For those aiming to do this project themselves, `hangman-word` and `hangman-phrase` should only hold helper functions specific to dealing with words/phrases. Of course, `words.py` and `phrases.py` contain the lists of words and phrases (along with comments at the top explaining some assumptions you can make about the data), and `hangman.py` is where library functions meant to be reusable should go.

For those that need a little more direction, here are the functions in that I recommend implementing in `hangman.py` (and would actively test if this was a graded assignment):

**I will leave it up to you to decide how you want to represent/store the data from the player's guesses. I've left more on that in the header comment in hangman.py**

```py
"""This should output a summary of previous guess data.
See below for sample game to match the formatting"""
def display_guesses(
    past_guesses: any,
    secret: str
) -> None:

"""This should output the player's lives.
See below for sample game to match the formatting"""
def display_lives(
    lives: int
) -> None:

"""This should output the guessed letters' places in the secret word.
Do NOT print the secret word itself. Make sure to print punctuation for
free to account for the secret word being a phrase. (Players should not
have to guess punctuation marks.)
See below for sample game to match the formatting"""
def display_partial_word(
    past_guesses: any,
    secret: str
) -> None:

"""This just repeatedly prompts the player for their guess until they
provide a single alphabetical character as input. Past guess data is
only required to prevent players from accidentally making the same
guess twice (definitely do NOT penalize the player for this)."""
def game_prompt(
    past_guesses: any
) -> str:

"""This takes the past guess data, the current number of lives, and the
latest guess to return updated versions of the guess data and lives (i.e.
it adds the latest guess to the past duess data and decreases the current
amount of lives if the latest guess wasn't in the secret word/phrase).
The boolean in the return value should be false if the game has ended (i.e.
the player either guessed the secret word/phrase or ran out of lives)"""
def evaluate(
    past_guesses: any,
    lives: int,
    current_guess: str,
    secret: str
) -> tuple[any, int, bool]:
```
