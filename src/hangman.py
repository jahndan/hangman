######                       some notes                       ######
### the type of guesses will depend on your implementation (there're
# multiple valid ways to implement this where some will be more code
# efficient and others will be more memory efficient) - I strongly
# suggest using immutable data structures (sets, tuples) over lists
### obviously, you can update the type annotation on guesses for the
# functions to match whatever implementation you end up with
### you can add as many optional parameters onto the function signa-
# -tures as you want, so long as it still works as expected when I
# run my tests without specifying those optional parameters
### you may create a shared game_loop function since the main loop
# for both versions (word and phrase) are likely to share much code
### you may alsocreate helper functions as needed


def display_guesses(guesses: any, secret: str, indent: int = 1) -> None:
    pass  # TODO implement


def display_lives(lives: int, indent: int = 1) -> None:
    pass  # TODO implement


def display_partial_word(guesses: any, secret: str) -> None:
    pass  # TODO implement


def game_prompt(guesses: any) -> str:
    pass  # TODO implement


def evaluate(
    guesses: any, lives: int, guess: str, secret: str
) -> tuple[any, int, bool]:
    pass  # TODO implement
