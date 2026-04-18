from default import is_number
from default import contains_number
from default import list_is_number
from bingo import bingo
from calculator import calculator
from list import listing
from hangman import hangman
from tik_tac_toe import tik_tac_toe
from checkers import checkers
from chess import chess
from backgammon import backgammon
if __name__ == '__main__':
  while True:
    print("Calculator(1)", "List(2)", "Tik Tac Toe(3)", "Bingo(4)", "Hangman(5)", "Checkers(6)", "Chess(7)")
    scanner = input("What App Do You Want To Use:")
    if is_number(scanner):
      scanner = int(scanner)
    if scanner == "quit":
      break
    if scanner == 1:
      calculator()
    elif scanner == 2:
      listing()
    elif scanner == 3:
      tik_tac_toe()
    elif scanner == 4:
      bingo()
    elif scanner == 5:
      hangman()
    elif scanner == 6:
      checkers()
    elif scanner == 7:
      chess()
    elif scanner == 8:
      backgammon()