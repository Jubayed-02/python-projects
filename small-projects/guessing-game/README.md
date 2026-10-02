# Number Guessing Game

A command-line game where the player tries to guess a randomly
generated number within a limited number of attempts.

## Requirements

- Python 3.x

## How to Play

1. Enter your name when prompted.
2. Guess a number between 1 and 10.
3. You have 3 chances — invalid input still uses up a chance.

## Features

- Generate random number between 1 and 10
- Input validation (rejects non-integers and out-of-range values)
- Graceful handling of `Ctrl+C` (KeyboardInterrupt)

## Modules used

- random
- sys

## How to Run

```bash
python main.py
```
