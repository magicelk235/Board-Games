import random
from default import is_number
from default import contains_number
from default import list_is_number

def tik_tac_toe():
    # create the list for the board
    display = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # create a function to display the board
    def display_board():
        print(f"{display[0]} │ {display[1]} │{display[2]} ")
        print("━━│━━━│━━")
        print(f"{display[3]} │ {display[4]} │{display[5]} ")
        print("━━│━━━│━━")
        print(f"{display[6]} │ {display[7]} │{display[8]}")

    # create a function to return who won
    def player_win_check():
        # create a loop for checking rows and columns
        for i in range(3):
            # checking if the row "i" is all equal
            if display[i*3] == display[3*i+1] == display[3*i+2]:
                # if they are all the same you need to return just one
                return display[i*3]
            # checking if the column "i" us all equal
            if display[i] == display[i+3] == display[i+6]:
                # if they are all the same you need to return just one
                return display[i]
        # checking if the right slant is equal or the left slant
        if display[0] == display[4] == display[8] or display[2] == display[4] == display[6]:
            # return display[4] because he's the middle
            return display[4]
    # create a function to check if someone won(true or false)
    def win_check():
        for i in range(3):
            # checking if the row "i" is all equal and not spaces
            if display[3*i] == display[3*i+1] == display[3*i+2] != " ":
                return True
            # checking if the column "i" us all equal and not spaces
            if display[i] == display[i+3] == display[i+6] != " ":
                return True
        # checking if the right slant is equal or the left slant and not spaces
        if display[0] == display[4] == display[8] != " " or display[2] == display[4] == display[6] != " ":
            return True
        else:
           return False

    # create a function for the gameplay
    def moves(player_name):
        # ask for number between 1-9
        scanner = input(f"player {player_name} Type Your Move(1-9):")
        # quit check for admin
        if scanner == "quit":
            return False
        # check if the input is a number and between 9-1 and the place in board is empty
        while not is_number(scanner) or 9 < int(scanner) or 1 > int(scanner) or display[int(scanner) - 1] != " ":
            # print an error message
            print("You Didn't Type an Available Move Try Again")
            # ask again for number between 1-9
            scanner = input(f"player {player_name} Type Your Move(1-9):")
            # quit check for admin
            if scanner == "quit":
                return False
        # quit check for admin
        if scanner == "quit":
            return False
        # set X or O to display
        display[int(scanner) - 1] = player_name
        # calls the board function to print the board
        display_board()
        # quit check for admin
        return True

    # set the starter player
    current_player = "X"
    # print the board
    display_board()
    # create a loop until someone win
    while not win_check():
        # quit check for admin
        quit_check = moves(current_player)
        # swapping the turns
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        # checking if it's a tie
        if " " not in display:
            print("It's a Tie")
            break
        # quit check for admin
        if not quit_check:
            break
    # check if isn't a tie
    if win_check():
        # print the winner
        print(f"The Winner Is {player_win_check()}")