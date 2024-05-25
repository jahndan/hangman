def display_guesses(guesses: set, secret: str, indent: int = 1) -> None:
    tab = " " * indent
    correct = str().join(sorted(guesses & set(secret)))
    incorrect = str().join(sorted(guesses - set(secret)))
    print(tab, "Correct guesses:    ", "[{}]".format(correct), sep=str())
    print(tab, "Incorrect guesses:  ", "[{}]".format(incorrect), sep=str())
    return


def display_lives(lives: int, LIVES: int, indent: int = 1) -> None:
    tab = " " * indent
    print(tab, "Lives left:         ", "{}/{}".format(lives, LIVES), sep=str())
    print(tab, "♥" * lives, "♡" * (LIVES - lives), sep=str())
    return


def display_partial_word(guesses: set, secret: str) -> None:
    for char in secret:
        if char in guesses or char in " ',;:.":
            print(char, end=str())
        else:
            print("_", end=str())
    print()
    return


def game_prompt(guesses: set) -> str:
    text = "()"
    while len(text) > 1 or not text.isalpha():
        text = str(input("Your guess? ")).lower()  # get input and lowercase it
    if text in guesses:
        return game_prompt(guesses)  # probably shouldn't use recursion
    else:
        return text


def evaluate(
    guesses: set, lives: int, guess: str, secret: str
) -> tuple[set, int, bool]:
    bad_guess: bool = set(guess).isdisjoint(secret)
    if bad_guess:
        lives = lives - 1
    guesses |= set(guess)
    return guesses, lives, not (guesses.issuperset(secret) or lives <= 0)
