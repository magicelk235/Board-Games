# Board games

A collection of terminal games written in Python. Run them, play with a friend, type "quit" when you're done.

## What's in here

- **Calculator** - Does math. Supports +, -, *, /, %, and ** (exponents). Type "=" to see the result.
- **List** - A basic to-do list. Add items, remove items, view the list.
- **Tic Tac Toe** - Two-player, 3x3 grid. You know the rules.
- **Bingo** - Supports 1-5 players. Each player gets a 4x4 board with random numbers 1-32.
- **Hangman** - Player 1 picks a word, player 2 guesses letters. Ten wrong guesses and you lose.
- **Checkers** - Two-player checkers.
- **Chess** - Two-player chess with Unicode pieces. Moves are entered as coordinates (e.g., "G2" then "G4").

## Running it

```bash
python main.py
```

Pick a game by number:
```
Calculator(1), List(2), Tik Tac Toe(3), Bingo(4), Hangman(5), Checkers(6), Chess(7)
```

Backgammon is option 8 but not listed in the menu.

## How the code is organized

Each game lives in its own file. `main.py` imports them all and runs a loop that asks which one you want. `default.py` has a few helper functions for input validation (`is_number`, `contains_number`, `list_is_number`).

The chess implementation is the most involved - it handles move validation for all piece types. The bingo game does some work to display multiple boards side by side in the terminal.

## Notes

Type "quit" in most games to exit back to the menu.

The calculator uses `eval()` to compute expressions, which works but isn't safe for untrusted input.
