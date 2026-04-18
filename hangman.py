import random
from default import is_number
from default import contains_number
from default import list_is_number

def hangman():
    # makes left_guess global
    global left_guess

    # create a function for printing the board
    def board(word):
        # creating a loop of the length of the word
        for i in range(len(word)):
            # print every right guess the player has done
            print(array_word[i], end="")
        print("")
        # print a "board" for the letters
        print("-" * len(word))

    # create a function to check if someone won
    def win_check(word):
        # create a loop of the length of the word
        for i in range(len(word)):
            # check if the player guessed all the letters
            if not array_word[i] == word[i]:
                return False
        return True

    # create a function to check who won
    def player_win_check(word):
        # create a loop of the length of the word
        for i in range(len(word)):
            # check if the player guessed all the letters
            if not array_word[i] == word[i]:
                return "Player 1"
        return "Player 2"

    # check if the guessed letter is in the word
    def letter_check(word, letter):
        # create a loop of the length of the word
        for i in range(len(word)):
            # check if the letter is anywhere in word
            if word[i] == letter:
                return True
        return False

    # set the letter into right guess if the letter is in word
    def number_letter_get(word, letter):
        # create a loop of the length of the word
        for i in range(len(word)):
            # check if the guess letter is in word
            if word[i] == letter:
                # set the letter into right guess
                array_word[i] = letter

    # keep the game until someone type quit
    while True:
        # ask player 1 for a word
        scanner = input("Player 1 Type a Word: ")
        # quit check for admin
        if scanner == "quit":
            break
        # check if the word is containing numbers
        while contains_number(scanner):
            # print a error message
            print("You Didn't Type a Word")
            scanner = input("Player 1 Type a Word: ")
        # creating the right guess array
        array_word = [" " for i in range(len(scanner))]
        # make the word lower
        word = str.lower(scanner)
        # print a lot of spaces
        for i in range(10000):
            print("")
        # set the left guess
        left_guess = 10
        # create an array with 10 left guess
        guess_letters = ["" for i in range(10)]
        # keep the game while noone win
        while not win_check(word):
            # print the board
            board(word)
            # print the player data
            print(f"You Have {left_guess} Left Guess")
            print(f"The Guessed Letters Are:")
            for i in range(len(guess_letters)):
                print(f"{guess_letters[i]} ", end="")
            print("")
            # ask player 2 for a letter
            scanner = input("Player 2 Type a Letter: ")
            # check if you type a letter
            while contains_number(scanner) or len(scanner) > 1 or len(scanner) < 1 or scanner in guess_letters:
                # print an error message
                print("Error: You Didn't Type A letter")
                scanner = input("Player 2 Type a Letter: ")
            # check if the letter is in word
            if letter_check(word, scanner):
                # set the letter ti right guess
                number_letter_get(word, scanner)
            # if letter not in word
            else:
                # remove one from the left guess
                left_guess -= 1
                # add the letter to guess letters
                guess_letters[9 - left_guess] = scanner
            # check if left guess is 0
            if left_guess == 0:
                # end the game if so
                break
        print("")
        # print the full board
        board(word)
        # print the winner
        print(f"The Winner Is {player_win_check(word)}")
