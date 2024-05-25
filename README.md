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

This branch `solution` contains a playable version of this. **A starter template for programmers unfamiliar with python to acquaint themselves with the built-in data structures is available on the other branch** `template`**.**
