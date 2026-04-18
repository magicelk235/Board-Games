import random
from default import is_number
from default import contains_number
from default import list_is_number

def checkers():

    # store the players symbols
    player1 = "●"
    player2 = "○"
    pawns_white = {"●","◆"}
    pawns_black = {"○","◇"}
    # create the board
    board = [
        [" ", "○", " ", "○", " ", "○", " ", "○"],
        ["○", " ", "○", " ", "○", " ", "○", " "],
        [" ", "○", " ", "○", " ", "○", " ", "○"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["●", " ", "●", " ", "●", " ", "●", " "],
        [" ", "●", " ", "●", " ", "●", " ", "●"],
        ["●", " ", "●", " ", "●", " ", "●", " "]
        ]

    # create a function that checks if someone won
    def win_check(board):
        pawns_white = {"●", "◆"}
        pawns_black = {"○", "◇"}
        black = False
        white = False
        for i in range(8):
            for m in range(8):
                if board[i][m] in pawns_black:
                    black = True
                if board[i][m] in pawns_white:
                    white = True
        if black and white:
            return False
        else:
            return True

    # create a function that checks who won
    def player_win_check(board):
        pawns_white = {"●", "◆"}
        pawns_black = {"○", "◇"}
        black = False
        white = False
        for i in range(8):
            for m in range(8):
                if board[i][m] in pawns_black:
                    black = True
                if board[i][m] in pawns_white:
                    white = True
        if black:
            return "Player 1"
        else:
            return "Player 2"

    # create a function to check if the given location is in the top end
    def top_end_check(location_in_letters):
        # check if the first letter in location is "a"
        if location_in_letters[0] == "a":
            return True
        return False

    # create a function to check if the given location is in the bottom end
    def bottom_end_check(location_in_letters):
        # check if the first letter in location is "h"
        if location_in_letters[0] == "h":
            return True
        return False

    # create a function to check if the location in letters is in the right corner
    def right_corner_check(location_in_letters):
        # check if the second letter in the location is 1 (location is letter example: h1 ,e3 ,r4)
        if location_in_letters[1] == "1":
            # if so return true
            return True
        return False

    # create a function to check if the location in letters is in the left corner
    def left_corner_check(location_in_letters):
        # check if the second letter in the location is 1 (location is letter example: h8 ,e3 ,r4)
        if location_in_letters[1] == "8":
            # if so return true
            return True
        return False

    # create a function to make location in numbers to letters
    def location_to_letters(location_in_numbers):
        # set itself to string, so you can take parts of him
        location_in_numbers = str(location_in_numbers)
        # create an array of letters
        letters_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        # create a loop of 8
        for i in range(8):
            # check if i = to location_in_numbers[0]
            if int(location_in_numbers[0]) == i:
                # return the letter i and location_in_numbers[1] + 1

                return f"{letters_list[i]}{int(location_in_numbers[1]) + 1}"

    # create a function to get the location in numbers
    def location_to_numbers(location_in_letters):
        # makes itself lower string
        location_in_letters = str.lower(location_in_letters)
        # create an array of letters
        letters_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        # create a loop of 8
        for i in range(8):
            # check if letters_list[i] is equal to location_in_letters[0]
            if location_in_letters[0] == letters_list[i]:
                # return string of i
                return f"{i}{int(location_in_letters[1]) - 1}"

    # return the available moves of the given location of king
    def king_move_check(location_in_letters, board, pawns, ops):

        # create the returner for later
        returner = ""
        # makes location in letters to numbers
        location_in_numbers = location_to_numbers(location_in_letters)

        # check if the location isn't in corner and end
        if not top_end_check(location_in_letters) and not right_corner_check(location_in_letters):
            # create a variable of up_right
            up_right = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) - 1}"
            # create a loop
            while True:
                # check if up right location isn't empty and isn't ops
                if not board[int(up_right[0])][int(up_right[1])] == " " and not board[int(up_right[0])][int(up_right[1])] in ops:
                    # break if so
                    break
                # add the location to the returner
                returner = f"{returner} {location_to_letters(up_right)}"
                # check if up right location is ops
                if board[int(up_right[0])][int(up_right[1])] in ops:
                    # break if so
                    break
                # check if up right is end
                if top_end_check(location_to_letters(up_right)):
                    # break if so
                    break
                # check if up right is corner
                if right_corner_check(location_to_letters(up_right)):
                    break
                # move up right to up right
                up_right = f"{int(up_right[0]) - 1}{int(up_right[1]) - 1}"

        # check if the location isn't in corner and end
        if not bottom_end_check(location_in_letters) and not right_corner_check(location_in_letters):
            # create a variable of down_right
            down_right = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) - 1}"
            # create a loop
            while True:
                # check if up right location isn't empty and isn't ops
                if not board[int(down_right[0])][int(down_right[1])] == " " and not board[int(down_right[0])][int(down_right[1])] in ops:
                    # break if so
                    break
                # add the location to the returner
                returner = f"{returner} {location_to_letters(down_right)}"
                # check if down right location is ops
                if board[int(down_right[0])][int(down_right[1])] in ops:
                    # break if so
                    break
                # check if down right is end
                if bottom_end_check(location_to_letters(down_right)):
                    # break if so
                    break
                # check if down right is corner
                if right_corner_check(location_to_letters(down_right)):
                    break
                # move down right to down right
                down_right = f"{int(down_right[0]) + 1}{int(down_right[1]) - 1}"

        # check if the location isn't in corner and end
        if not top_end_check(location_in_letters) and not left_corner_check(location_in_letters):
            # create a variable of up left
            up_left = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) + 1}"
            # create a loop
            while True:
               # check if up right location isn't empty and isn't ops
               if not board[int(up_left[0])][int(up_left[1])] == " " and not board[int(up_left[0])][int(up_left[1])] in ops:
                    # break if so
                    break
               # add the location to the returner
               returner = f"{returner} {location_to_letters(up_left)}"
               # check if up left location is ops
               if board[int(up_left[0])][int(up_left[1])] in ops:
                   # break if so
                   break
               # check if up left is end
               if top_end_check(location_to_letters(up_left)):
               # break if so
                   break
                # check if up left is corner
               if right_corner_check(location_to_letters(up_left)):
                  break
               # move down right to up left
               up_left = f"{int(up_left[0]) - 1}{int(up_left[1]) + 1}"

        # check if the location isn't in corner and end
        if not bottom_end_check(location_in_letters) and not left_corner_check(location_in_letters):
            # create a variable of down left
            down_left = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) + 1}"
            # create a loop
            while True:
                # check if up right location isn't empty and isn't ops
                if not board[int(down_left[0])][int(down_left[1])] == " " and not board[int(down_left[0])][int(down_left[1])] in ops:
                    # break if so
                    break
                # add the location to the returner
                returner = f"{returner} {location_to_letters(down_left)}"
                # check if down left location is ops
                if board[int(down_left[0])][int(down_left[1])] in ops:
                    # break if so
                    break
                # check if down left is end
                if bottom_end_check(location_to_letters(down_left)):
                    # break if so
                    break
                # check if down left is corner
                if right_corner_check(location_to_letters(down_left)):
                    break
                # move down right to down right
                down_left = f"{int(down_left[0]) + 1}{int(down_left[1]) + 1}"

        # check if returner is empty
        if returner == "":
            # return false if so
            return False

        return str.upper(returner.lstrip())

    def eat_check(location_in_letters,board,pawns,ops):
        location_in_numbers = location_to_numbers(location_in_letters)
        returner = ""
        if pawns == "●":
            right_move = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) - 1}"
            left_move = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) + 1}"
            # check if location in letters is left corner
            if not left_corner_check(location_in_letters):
                # check if location in letters is bottom end
                if not top_end_check(location_in_letters):
                    # checks if left move location in board is the ops
                        if board[int(left_move[0])][int(left_move[1])] in ops:
                            # check if location in letters is left corner
                            if not left_corner_check(location_to_letters(left_move)):
                                # check if location in letters is bottom end
                                if not top_end_check(location_to_letters(left_move)):
                                    left_move = f"{int(left_move[0]) - 1}{int(left_move[1]) + 1}"
                                    # checks if left move location in board is the empty
                                    if board[int(left_move[0])][int(left_move[1])] == " ":
                                        # add itself to the returner
                                        returner = f"{returner} {str.upper(location_to_letters(left_move))}"

            # check if location in letters is right corner
            if not right_corner_check(location_in_letters):
                # check if location in letters is bottom end
                if not top_end_check(location_in_letters):
                    # checks if right move location in board is the ops
                    if board[int(right_move[0])][int(right_move[1])] in ops:
                        # check if location in letters is right corner
                        if not right_corner_check(location_to_letters(right_move)):
                            # check if location in letters is bottom end
                            if not top_end_check(location_to_letters(right_move)):
                                right_move = f"{int(right_move[0]) - 1}{int(right_move[1]) - 1}"
                                # checks if right move location in board is the empty
                                if board[int(right_move[0])][int(right_move[1])] == " ":
                                    # add itself to the returner
                                    returner = f"{returner} {str.upper(location_to_letters(right_move))}"
        if pawns == "○":
            right_move = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) - 1}"
            left_move = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) + 1}"
            # check if location in letters is left corner
            if not left_corner_check(location_in_letters):
                # check if location in letters is top end
                if not bottom_end_check(location_in_letters):
                    # checks if left move location in board is the ops
                    if board[int(left_move[0])][int(left_move[1])] in ops:
                        # check if location in letters is left corner
                        if not left_corner_check(location_to_letters(left_move)):
                            # check if location in letters is top end
                            if not bottom_end_check(location_to_letters(left_move)):
                                left_move = f"{int(left_move[0]) + 1}{int(left_move[1]) + 1}"
                                # checks if left move location in board is the empty
                                if board[int(left_move[0])][int(left_move[1])] == " ":
                                    # add itself to the returner
                                    returner = f"{returner} {str.upper(location_to_letters(left_move))}"

            # check if location in letters is right corner
            if not right_corner_check(location_in_letters):
                # check if location in letters is top end
                if not bottom_end_check(location_in_letters):
                    # checks if right move location in board is the ops
                    if board[int(right_move[0])][int(right_move[1])] in ops:
                        # check if location in letters is right corner
                        if not right_corner_check(location_to_letters(right_move)):
                            # check if location in letters is top end
                            if not bottom_end_check(location_to_letters(right_move)):
                                right_move = f"{int(right_move[0]) + 1}{int(right_move[1]) - 1}"
                                # checks if right move location in board is the empty
                                if board[int(right_move[0])][int(right_move[1])] == " ":
                                    # add itself to the returner
                                    returner = f"{returner} {str.upper(location_to_letters(right_move))}"
        if returner == "":
            return False
        else:
            return returner

    # return the available moves of the given location
    def default_move_check(location_in_letters, board, pawns, ops):
        # create the returner for later
        returner = ""
        eat_move = eat_check(location_in_letters,board,pawns,ops)
        if eat_move == False:
            # check if the pawns is white
            if pawns == "●":
                # create a variable of location in numbers
                location_in_numbers = location_to_numbers(location_in_letters)
                # create a variable of shift right of location in numbers
                right_move = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) - 1}"
                # check if location in letters is right corner
                if not right_corner_check(location_in_letters):
                    # check if location in letters is bottom end
                    if not top_end_check(location_in_letters):
                        # checks if right move location in board is empty
                        if board[int(right_move[0])][int(right_move[1])] == " ":
                            # add itself to the returner
                            returner = f"{returner} {str.upper(location_to_letters(right_move))}"

                # create a variable of shift left of location in numbers
                left_move = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) + 1}"
                # check if location in letters is left corner
                if not left_corner_check(location_in_letters):
                    # check if location in letters is bottom end
                    if not top_end_check(location_in_letters):
                        # checks if left move location in board is empty
                        if board[int(left_move[0])][int(left_move[1])] == " ":
                            # add itself to the returner
                            returner = f"{returner} {str.upper(location_to_letters(left_move))}"
            # check if the pawns is black
            if pawns == "○":
                # create a variable of location in numbers
                location_in_numbers = location_to_numbers(location_in_letters)
                # create a variable of shift right of location in numbers
                right_move = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) - 1}"
                # create a variable of shift left of location in numbers
                left_move = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) + 1}"
                # check if location in letters is right corner
                if not right_corner_check(location_in_letters):
                    # checks if right move location in board is empty
                    if board[int(right_move[0])][int(right_move[1])] == " ":
                        # add itself to the returner
                        returner = f"{returner} {str.upper(location_to_letters(right_move))}"
            # check if location in letters is left corner
                if not left_corner_check(location_in_letters):
                    # checks if left move location in board is empty
                    if board[int(left_move[0])][int(left_move[1])] == " ":
                        # add itself to the returner
                        returner = f"{returner} {str.upper(location_to_letters(left_move))}"
        else:
            returner = eat_move
        # check if returner is empty
        if returner == "":
            # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()

    # create a function to if the given location is king
    def king_check(location_in_letters, pawns, board, ops):
        # check if the pawns is black
        if pawns == "○":
            # create a variable that store the king symbol
            king_pawns = "◇"
            # check if the location of the pawns is legit
            if location_check(location_in_letters, king_pawns, board, ops):
                # check if there is an available move
                king_move_check(location_in_letters, board, pawns, "●")
                # return true if so
                return True
        
        # check if the pawns is white
        if pawns == "●":
            # create a variable that store the king symbol
            king_pawns = "◆"
            # check if the location of the pawns is legit
            if location_check(location_in_letters, king_pawns, board, ops):
                # check if there is an available move
                king_move_check(location_in_letters, board, pawns, "○")
                # return true if so
                return True
            return False

    # create a function to check if the given pawns can move to the given location
    def location_check(location_in_letters, pawns, board, ops):

        # create a list of letters
        letter_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        # set itself to lower string
        location_in_letters = str.lower(location_in_letters)


        # check if the input's length isn't 2
        if not len(location_in_letters) == 2:
            return False

        # check if location_in_letters[1] isn't number
        if not is_number(location_in_letters[1]):
            return False

        # check if location_in_letters[1] isn't between 1-8
        if int(location_in_letters[1]) > 8 or int(location_in_letters[1]) < 1:
            return False

        # the main use is to check if there is a letter from the letters list:

        # create a variably named letter check
        letter_check = False
        # create a loop of 8
        for i in range(8):
            # check if location_in_letters[0] is equal to letter_list[i]
            if location_in_letters[0] == letter_list[i]:
                # set letter_check to true
                letter_check = True
                break
        # check if not letter check
        if not letter_check:
            return False

        # create a variable of location in numbers
        location_in_numbers = location_to_numbers(location_in_letters)
        # check if the location in board isn't equal to the pawns
        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] != pawns:
            return False
        # check if there are available moves
        if default_move_check(location_in_letters, board, pawns, ops) != False:
            return True
        else:
            return False

    # create a function display the board
    def display_board(board):
        print("\033[4m │1│2│3│4│5│6│7│8│ \033[0m")
        print(f"\033[4mA│{board[0][0]}│{board[0][1]}│{board[0][2]}│{board[0][3]}│{board[0][4]}│{board[0][5]}│{board[0][6]}│{board[0][7]}│A\033[0m")
        print(f"\033[4mB│{board[1][0]}│{board[1][1]}│{board[1][2]}│{board[1][3]}│{board[1][4]}│{board[1][5]}│{board[1][6]}│{board[1][7]}│B\033[0m")
        print(f"\033[4mC│{board[2][0]}│{board[2][1]}│{board[2][2]}│{board[2][3]}│{board[2][4]}│{board[2][5]}│{board[2][6]}│{board[2][7]}│C\033[0m")
        print(f"\033[4mD│{board[3][0]}│{board[3][1]}│{board[3][2]}│{board[3][3]}│{board[3][4]}│{board[3][5]}│{board[3][6]}│{board[3][7]}│D\033[0m")
        print(f"\033[4mE│{board[4][0]}│{board[4][1]}│{board[4][2]}│{board[4][3]}│{board[4][4]}│{board[4][5]}│{board[4][6]}│{board[4][7]}│E\033[0m")
        print(f"\033[4mF│{board[5][0]}│{board[5][1]}│{board[5][2]}│{board[5][3]}│{board[5][4]}│{board[5][5]}│{board[5][6]}│{board[5][7]}│F\033[0m")
        print(f"\033[4mG│{board[6][0]}│{board[6][1]}│{board[6][2]}│{board[6][3]}│{board[6][4]}│{board[6][5]}│{board[6][6]}│{board[6][7]}│G\033[0m")
        print(f"\033[4mH│{board[7][0]}│{board[7][1]}│{board[7][2]}│{board[7][3]}│{board[7][4]}│{board[7][5]}│{board[7][6]}│{board[7][7]}│H\033[0m")
        print(" │1│2│3│4│5│6│7│8│")
    
    # create a function for the gameplay
    def moves(player, pawns, board, ops,eated):
        king = False
        if eated == None:
            # ask for a location in letters
            scanner = (input(f"{player}({pawns}) What Pawn Do You Want To Move: "))
            # check if the given location is king
            if king_check(scanner, pawns, board, ops):
                king = True
            else:
                king = False

            # check the location
            while not location_check(scanner, pawns, board, ops):
                # break if king
                if king:
                    break
                # print an error message
                print("You Didn't Type An Available Move")
                # ask for a location in letters
                scanner = input(f"{player}({pawns}) What Pawn Do You Want To Move: ")
                # check if the given location is king
                if king_check(scanner, pawns, board, ops):
                    king = True
                else:
                    king = False

            # store the location
            location_in_letters = scanner
        else:
            print(1)
            location_in_letters = eated

        # if not king
        if not king:
            # print the available moves
            print("The Available Moves Are: ", end="")
            print(default_move_check(location_in_letters, board, pawns, ops))
            # create a temp variable for the pawns move
            temp_pawns_move = str.lower(default_move_check(location_in_letters, board, pawns, ops))
            # remove spaces
            temp_pawns_move = temp_pawns_move.replace(" ", "")
            # create a list of the pawns moves
            pawns_move = {""}
            pawns_move.remove("")
            # create a loop half the length of temp pawns move
            for i in range(int(len(temp_pawns_move) / 2)):
                # add the moves to the list
                pawns_move.add(f"{temp_pawns_move[i * 2]}{temp_pawns_move[1 + i * 2]}")
            # ask the player where he wants to move the pawn
            scanner = str.lower(input(f"Where Do You Want {str.upper(location_in_letters)} To Move: "))
            # check if the entered move is in list
            while scanner not in pawns_move:
                print("You Didn't Type an Available Move")
                scanner = str.lower(input(f"Where Do You Want {str.upper(location_in_letters)} To Move: "))
            # create a location in letters to the typed move
            location_in_letters1 = scanner
            # create a location in numbers of the typed move
            location_in_numbers1 = location_to_numbers(location_in_letters1)
            # create a location in numbers
            location_in_numbers = location_to_numbers(location_in_letters)
            # if white
            if pawns == "●":
                # check if the move is eating move or normal
                if int(location_in_numbers[0]) - int(location_in_numbers1[0]) == 2:
                    # check if the eating move is right or left
                    if int(location_in_numbers[1]) > int(location_in_numbers1[1]):
                        # set the past location to null
                        board[int(location_in_numbers[0])][int(location_in_numbers[1])] = " "
                        # set the one you ate to null
                        board[int(location_in_numbers[0]) - 1][int(location_in_numbers[1]) - 1] = " "
                        # check if to make the player king
                        if top_end_check(location_in_letters1):
                            # make the player king if so
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "◆"
                        # make the player normal
                        else:
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "●"
                        if eat_check(location_to_letters(location_in_numbers1),board,pawns,ops) != False:
                            return location_to_letters(location_in_numbers1)
                    # right eating move
                    else:
                        # set the past location to null
                        board[int(location_in_numbers[0])][int(location_in_numbers[1])] = " "
                        # set the one you ate to null
                        board[int(location_in_numbers[0]) - 1][int(location_in_numbers[1]) + 1] = " "
                        # check if to make the player king
                        if top_end_check(location_in_letters1):
                            # make the player king if so
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "◆"
                        # make the player normal
                        else:
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "●"
                        if eat_check(location_to_letters(location_in_numbers1),board,pawns,ops) != False:
                            return location_to_letters(location_in_numbers1)
                # normal move
                else:
                    # set the past location to null
                    board[int(location_in_numbers[0])][int(location_in_numbers[1])] = " "
                    # check if to make the player king
                    if top_end_check(location_in_letters1):
                        # make the player king if so
                        board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "◆"
                    # make the player normal
                    else:
                        board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "●"
            # if black
            if pawns == "○":
                # check if the move is eating move or normal
                if int(location_in_numbers1[0]) - int(location_in_numbers[0]) == 2:
                    # check if the eating move is right or left
                    if int(location_in_numbers[1]) > int(location_in_numbers1[1]):
                        # set the past location to null
                        board[int(location_in_numbers[0])][int(location_in_numbers[1])] = " "
                        # set the one you ate to null
                        board[int(location_in_numbers[0]) + 1][int(location_in_numbers[1]) - 1] = " "
                        # check if to make the player king
                        if bottom_end_check(location_in_letters1):
                            # make the player king if so
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "◇"
                        # make the player normal
                        else:
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "○"
                        if eat_check(location_to_letters(location_in_numbers1),board,pawns,ops) != False:
                            return location_to_letters(location_in_numbers1)
                    # right eating move
                    else:
                        # set the past location to null
                        board[int(location_in_numbers[0])][int(location_in_numbers[1])] = " "
                        # set the one you ate to null
                        board[int(location_in_numbers[0]) + 1][int(location_in_numbers[1]) + 1] = " "
                        # check if to make the player king
                        if bottom_end_check(location_in_letters1):
                            # make the player king if so
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "◇"
                        # make the player normal
                        else:
                            board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "○"
                        if eat_check(location_to_letters(location_in_numbers1),board,pawns,ops) != False:
                            return location_to_letters(location_in_numbers1)
                # normal move
                else:
                    # set the past location to null
                    board[int(location_in_numbers[0])][int(location_in_numbers[1])] = " "
                    # check if to make the player king
                    if bottom_end_check(location_in_letters1):
                        # make the player king if so
                        board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "◇"
                    # make the player normal
                    else:
                        board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] = "○"

        # if king
        if king:
            print("The Available Moves Are: ", end="")
            # print the available king moves
            print(king_move_check(location_in_letters, board, pawns, ops))

            # create temp variable of the available moves of th king
            temp_king_move = str.lower(king_move_check(location_in_letters, board, pawns, ops))
            # remove spaces
            temp_king_move = temp_king_move.replace(" ", "")
            # create a list of king moves
            king_moves = {""}
            king_moves.remove("")
            # create a loop of half the length of temp king move
            for i in range(int(len(temp_king_move) / 2)):
                # add the locations from temp king to king moves list
                king_moves.add(f"{temp_king_move[i * 2]}{temp_king_move[1 + i * 2]}")
            # ask the player to enter where to move the king
            scanner = str.lower(input(f"Where Do You Want {str.upper(location_in_letters)} To Move: "))
            # check if the entered move is king move
            while scanner not in king_moves:
                print("You Didn't Type an Available Move")
                scanner = str.lower(input(f"Where Do You Want {str.upper(location_in_letters)} To Move: "))
            # set the scanner location to numbers
            scanner = location_to_numbers(scanner)
            # create location in numbers
            location_in_numbers = location_to_numbers(location_in_letters)
            # set the pawn to the new location
            board[int(scanner[0])][int(scanner[1])] = board[int(location_in_numbers[0])][int(location_in_numbers[1])]
            # remove it from the old location
            board[int(location_in_numbers[0])][int(location_in_numbers[1])] = " "
        return None

    current_player = "1"
    eated = None
    while not win_check(board):
        # swapping the turns
        if current_player == "1":
            display_board(board)
            eated = moves("Player-1", player1, board, pawns_black,eated)
            if eated == None:
                current_player = "2"
        else:
            display_board(board)
            eated = moves("Player-2", player2, board, pawns_white,eated)
            if eated == None:
                current_player = "1"
    print(f"The Winner Is {player_win_check(board)}")