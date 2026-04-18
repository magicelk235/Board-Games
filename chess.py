from default import is_number
from default import contains_number
from default import list_is_number

def chess():
    black = ["♙", "♖", "♗", "♘", "♕", "♔"]
    white = ["♟", "♜", "♝", "♞", "♛", "♚"]
    board = [
        ["♖", "♘", "♗", "♔", "♕", "♗", "♘", "♖"],
        ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
        ["ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ"],
        ["ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ"],
        ["ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ"],
        ["ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ", "ㅤ"],
        ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
        ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
    ]
    # create a function that checks if someone won
    def win_check(board):
        black = False
        white = False
        for i in range(8):
            for m in range(8):
                if board[i][m] == "♔":
                    black = True
                if board[i][m] == "♚":
                    white = True
        if black and white:
            return False
        else:
            return True

    # create a function that checks who won
    def player_win_check(board):
        black = False
        white = False
        for i in range(8):
            for m in range(8):
                if board[i][m] == "♔":
                    black = True
                if board[i][m] == "♚":
                    white = True
        if black:
            return "Player 1"
        else:
            return "Player 2"

    # create a function display the board
    def display_board(board):
        print("\033[4m │Ⅰ│Ⅱ│Ⅲ│Ⅳ│Ⅴ│Ⅵ│Ⅶ│Ⅷ│  \033[0m")
        print(f"\033[4mA│{board[0][0]}│{board[0][1]}│{board[0][2]}│{board[0][3]}│{board[0][4]}│{board[0][5]}│{board[0][6]}│{board[0][7]}│A\033[0m")
        print(f"\033[4mB│{board[1][0]}│{board[1][1]}│{board[1][2]}│{board[1][3]}│{board[1][4]}│{board[1][5]}│{board[1][6]}│{board[1][7]}│B\033[0m")
        print(f"\033[4mC│{board[2][0]}│{board[2][1]}│{board[2][2]}│{board[2][3]}│{board[2][4]}│{board[2][5]}│{board[2][6]}│{board[2][7]}│C\033[0m")
        print(f"\033[4mD│{board[3][0]}│{board[3][1]}│{board[3][2]}│{board[3][3]}│{board[3][4]}│{board[3][5]}│{board[3][6]}│{board[3][7]}│D\033[0m")
        print(f"\033[4mE│{board[4][0]}│{board[4][1]}│{board[4][2]}│{board[4][3]}│{board[4][4]}│{board[4][5]}│{board[4][6]}│{board[4][7]}│E\033[0m")
        print(f"\033[4mF│{board[5][0]}│{board[5][1]}│{board[5][2]}│{board[5][3]}│{board[5][4]}│{board[5][5]}│{board[5][6]}│{board[5][7]}│F\033[0m")
        print(f"\033[4mG│{board[6][0]}│{board[6][1]}│{board[6][2]}│{board[6][3]}│{board[6][4]}│{board[6][5]}│{board[6][6]}│{board[6][7]}│G\033[0m")
        print(f"\033[4mH│{board[7][0]}│{board[7][1]}│{board[7][2]}│{board[7][3]}│{board[7][4]}│{board[7][5]}│{board[7][6]}│{board[7][7]}│H\033[0m")
        print(" │Ⅰ│Ⅱ│Ⅲ│Ⅳ│Ⅴ│Ⅵ│Ⅶ│Ⅷ│")

    def corner_check(location_in_letters):
        if top_end_check(location_in_letters):
            return True
        if bottom_end_check(location_in_letters):
            return True
        if left_corner_check(location_in_letters):
            return True
        if right_corner_check(location_in_letters):
            return True
        return False

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

    # check if there is an available move for pawns
    def pawns_location_check(location_in_letters, color, board, ops, color_name):
        # create a returner for later
        returner = ""
        # create location in numbers
        location_in_numbers = location_to_numbers(location_in_letters)


        # if color white
        if color_name == "white":
            # check if location is top end
            if not top_end_check(location_in_letters):
                # create new location in numbers
                location_in_numbers1 = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1])}"
                # check if next location is empty
                if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == "ㅤ":
                    # add to the returner
                    returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"
                    # check if the pawns are in the start
                    if location_in_numbers[0] == "6":
                        # move one more
                        location_in_numbers1 = f"{int(location_in_numbers1[0]) - 1}{int(location_in_numbers1[1])}"
                        # checks if empty
                        if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == "ㅤ":
                            # add to the returner
                            returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"
            # create a loop of the length ops
            for i in range(len(ops)):
                if not right_corner_check(location_in_letters):
                    # create location in numbers1
                    location_in_numbers1 = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) - 1}"
                    # checks if the location in numbers1 is in ops
                    if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == ops[i]:
                        # add it to the returner if so
                        returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"

                if not left_corner_check(location_in_letters):
                    # create location in numbers1
                    location_in_numbers1 = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) + 1}"
                    # checks if the location in numbers1 is in ops
                    if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == ops[i]:
                        # add it to the returner if so
                        returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"
        # if color black
        if color_name == "black":
            # check if location is bottom end
            if not bottom_end_check(location_in_letters):
                # create new location in numbers
                location_in_numbers1 = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1])}"
                # check if next location is empty
                if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == "ㅤ":
                    # add to the returner
                    returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"
                    # check if the pawns are in the start
                    if location_in_numbers[0] == "1":
                        # move one more
                        location_in_numbers1 = f"{int(location_in_numbers1[0]) + 1}{int(location_in_numbers1[1])}"
                        # checks if empty
                        if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == "ㅤ":
                            # add to the returner
                            returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"
            # create a loop of the length ops
            for i in range(len(ops)):
                # check if 
                if not right_corner_check(location_in_letters):
                    # create location in numbers1
                    location_in_numbers1 = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) - 1}"
                    # checks if the location in numbers1 is in ops
                    if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == ops[i]:
                        # add it to the returner if so
                        returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"

                if not left_corner_check(location_in_letters):
                    # create location in numbers1
                    location_in_numbers1 = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) + 1}"
                    # checks if the location in numbers1 is in ops
                    if board[int(location_in_numbers1[0])][int(location_in_numbers1[1])] == ops[i]:
                        # add it to the returner if so
                        returner = f"{returner} {str.upper(location_to_letters(location_in_numbers1))}"
        # check if returner is empty
        if returner == "":
            # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()

    # check if there is an available move for rocks
    def rook_location_check(location_in_letters, color, board, ops):
        # make location in letters to numbers
        location_in_numbers = location_to_numbers(location_in_letters)
        # set returner
        returner = ""

        # checks if the location is in left corner
        if not left_corner_check(location_in_letters):
            # create a new location at the left
            left_location_in_numbers = f"{location_in_numbers[0]}{int(location_in_numbers[1]) + 1}"
            # create a loop
            while True:
                # checks if there are pieces from the same group
                if board[int(left_location_in_numbers[0])][int(left_location_in_numbers[1])] in color:
                    # break if so
                    break
                # return the location
                returner = f"{returner} {str.upper(location_to_letters(left_location_in_numbers))}"
                # check if there are ops pieces
                if board[int(left_location_in_numbers[0])][int(left_location_in_numbers[1])] in ops:
                    # break if so
                    break
                # checks if the location is cornered
                if left_corner_check(location_to_letters(left_location_in_numbers)):
                    # break if so
                    break
                # move the left to the left
                left_location_in_numbers = f"{left_location_in_numbers[0]}{int(left_location_in_numbers[1]) + 1}"

        # checks if the location is in right corner
        if not right_corner_check(location_in_letters):
            # create a new location at the right
            right_location_in_numbers = f"{location_in_numbers[0]}{int(location_in_numbers[1]) - 1}"
            # create a loop
            while True:
                # checks if there are pieces from the same group
                if board[int(right_location_in_numbers[0])][int(right_location_in_numbers[1])] in color:
                    # break if so
                    break
                # return the location
                returner = f"{returner} {str.upper(location_to_letters(right_location_in_numbers))}"
                # check if there are ops pieces
                if board[int(right_location_in_numbers[0])][int(right_location_in_numbers[1])] in ops:
                    # break if so
                    break
                # checks if the location is cornered
                if right_corner_check(location_to_letters(right_location_in_numbers)):
                    # break if so
                    break
                # move the right to the right
                right_location_in_numbers = f"{right_location_in_numbers[0]}{int(right_location_in_numbers[1]) - 1}"

        # checks if the location is in up corner
        if not top_end_check(location_in_letters):
            # create a new location at the up
            top_location_in_numbers = f"{int(location_in_numbers[0]) - 1}{location_in_numbers[1]}"
            # create a loop
            while True:
                # checks if there are pieces from the same group
                if board[int(top_location_in_numbers[0])][int(top_location_in_numbers[1])] in color:
                    # break if so
                    break
                # return the location
                returner = f"{returner} {str.upper(location_to_letters(top_location_in_numbers))}"
                # check if there are ops pieces
                if board[int(top_location_in_numbers[0])][int(top_location_in_numbers[1])] in ops:
                    # break if so
                    break
                # checks if the location is cornered
                if top_end_check(location_to_letters(top_location_in_numbers)):
                    # break if so
                    break
                # move the up to the up
                top_location_in_numbers = f"{int(top_location_in_numbers[0]) - 1}{int(top_location_in_numbers[1])}"

        # checks if the location is in up bottom
        if not bottom_end_check(location_in_letters):
            # create a new location at the bottom
            bottom_location_in_numbers = f"{int(location_in_numbers[0]) + 1}{location_in_numbers[1]}"
            # create a loop
            while True:
                # checks if there are pieces from the same group
                if board[int(bottom_location_in_numbers[0])][int(bottom_location_in_numbers[1])] in color:
                    # break if so
                    break
                returner = f"{returner} {str.upper(location_to_letters(bottom_location_in_numbers))}"
                # checks if the location is cornered
                if board[int(bottom_location_in_numbers[0])][int(bottom_location_in_numbers[1])] in ops:
                    # break if so
                    break
                if bottom_end_check(location_to_letters(bottom_location_in_numbers)):
                    # break if so
                    break
                # move the bottom to the bottom
                bottom_location_in_numbers = f"{int(bottom_location_in_numbers[0]) + 1}{int(bottom_location_in_numbers[1])}"

        # check if returner is empty
        if returner == "":
            # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()

    def bishop_location_check(location_in_letters, color, board, ops):
        location_in_numbers = location_to_numbers(location_in_letters)
        returner = ""

        if not left_corner_check(location_in_letters):
            if not top_end_check(location_in_letters):
                top_left_location_in_numbers = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) + 1}"
                while True:
                    if int(top_left_location_in_numbers) > 63 or int(top_left_location_in_numbers) < 0:
                        break
                    if board[int(top_left_location_in_numbers[0])][int(top_left_location_in_numbers[1])] in color:
                        break
                    returner = f"{returner} {str.upper(location_to_letters(top_left_location_in_numbers))}"
                    if board[int(top_left_location_in_numbers[0])][int(top_left_location_in_numbers[1])] in ops:
                        break
                    if left_corner_check(location_to_letters(top_left_location_in_numbers)):
                        break
                    if top_end_check(location_to_letters(top_left_location_in_numbers)):
                        break
                    top_left_location_in_numbers = f"{int(top_left_location_in_numbers[0]) - 1}{int(top_left_location_in_numbers[1]) + 1}"

        if not right_corner_check(location_in_letters):
            if top_end_check(location_in_letters):
                top_right_location_in_numbers = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) - 1}"
                while True:
                    if int(top_right_location_in_numbers) > 63 or int(top_right_location_in_numbers) < 0:
                        break
                    print(top_right_location_in_numbers)
                    if board[int(top_right_location_in_numbers[0])][int(top_right_location_in_numbers[1])] in color:
                        break
                    returner = f"{returner} {str.upper(location_to_letters(top_right_location_in_numbers))}"
                    if board[int(top_right_location_in_numbers[0])][int(top_right_location_in_numbers[1])] in ops:
                        break
                    if right_corner_check(location_to_letters(top_right_location_in_numbers)):
                        break
                    if top_end_check(location_to_letters(top_right_location_in_numbers)):
                        break

                    top_right_location_in_numbers = f"{int(top_right_location_in_numbers[0]) - 1}{int(top_right_location_in_numbers[1]) - 1}"

        if not left_corner_check(location_in_letters):
            if not bottom_end_check(location_in_letters):
                bottom_left_location_in_numbers = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) + 1}"
                while True:
                    if int(bottom_left_location_in_numbers) > 63 or int(bottom_left_location_in_numbers) < 0:
                        break
                    if board[int(bottom_left_location_in_numbers[0])][int(bottom_left_location_in_numbers[1])] in color:
                        break
                    returner = f"{returner} {str.upper(location_to_letters(bottom_left_location_in_numbers))}"
                    if board[int(bottom_left_location_in_numbers[0])][int(bottom_left_location_in_numbers[1])] in ops:
                        break
                    if left_corner_check(location_to_letters(bottom_left_location_in_numbers)):
                        break
                    if bottom_end_check(location_to_letters(bottom_left_location_in_numbers)):
                        break
                    bottom_left_location_in_numbers = f"{int(bottom_left_location_in_numbers[0]) + 1}{int(bottom_left_location_in_numbers[1]) + 1}"

        if not right_corner_check(location_in_letters):
            if not bottom_end_check(location_in_letters):
                bottom_right_location_in_numbers = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) - 1}"
                while True:
                    if int(bottom_right_location_in_numbers) > 63 or int(bottom_right_location_in_numbers) < 0:
                        break
                    if board[int(bottom_right_location_in_numbers[0])][int(bottom_right_location_in_numbers[1])] in color:
                        break
                    returner = f"{returner} {str.upper(location_to_letters(bottom_right_location_in_numbers))}"
                    if board[int(bottom_right_location_in_numbers[0])][int(bottom_right_location_in_numbers[1])] in ops:
                        break
                    if right_corner_check(location_to_letters(bottom_right_location_in_numbers)):
                        break
                    if bottom_end_check(location_to_letters(bottom_right_location_in_numbers)):
                        break
                    bottom_right_location_in_numbers = f"{int(bottom_right_location_in_numbers[0]) + 1}{int(bottom_right_location_in_numbers[1]) - 1}"

        # check if returner is empty
        if returner == "":
            # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()

    def knight_location_check(location_in_letters, color, board, ops):
        returner = ""
        location_in_numbers = location_to_numbers(location_in_letters)


        if not right_corner_check(location_in_letters):
            if not top_end_check(location_in_letters):
                up_right = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) - 1}"
                if not right_corner_check(location_to_letters(up_right)):
                    if not top_end_check(location_to_letters(up_right)):
                        if board[int(up_right[0])][int(up_right[1]) - 1] not in color:
                            returner = f"{returner} {location_to_letters(str(int(up_right[0])) + str(int(up_right[1]) - 1))}"
                        if board[int(up_right[0]) - 1][int(up_right[1])] not in color:
                            returner = f"{returner} {location_to_letters(str(int(up_right[0]) - 1) + str(int(up_right[1])))}"

        if not left_corner_check(location_in_letters):
            if not top_end_check(location_in_letters):
                up_left = f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) + 1}"
                if not left_corner_check(location_to_letters(up_left)):
                    if not top_end_check(location_to_letters(up_left)):
                        if board[int(up_left[0])][int(up_left[1]) + 1] not in color:
                            returner = f"{returner} {location_to_letters(str(int(up_left[0])) + str(int(up_left[1]) + 1))}"
                        if board[int(up_left[0]) - 1][int(up_left[1])] not in color:
                            returner = f"{returner} {location_to_letters(str(int(up_left[0]) - 1) + str(int(up_left[1])))}"

        if not right_corner_check(location_in_letters):
            if not bottom_end_check(location_in_letters):
                down_right = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) - 1}"
                if not right_corner_check(location_to_letters(down_right)):
                    if not bottom_end_check(location_to_letters(down_right)):
                        if board[int(down_right[0])][int(down_right[1]) - 1] not in color:
                            returner = f"{returner} {location_to_letters(str(int(down_right[0])) + str(int(down_right[1]) - 1))}"
                        if board[int(down_right[0]) + 1][int(down_right[1])] not in color:
                            returner = f"{returner} {location_to_letters(str(int(down_right[0]) + 1) + str(int(down_right[1])))}"

        if not left_corner_check(location_in_letters):
            if not bottom_end_check(location_in_letters):
                down_left = f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) + 1}"
                if not left_corner_check(location_to_letters(down_left)):
                    if not bottom_end_check(location_to_letters(down_left)):
                        if board[int(down_left[0])][int(down_left[1]) + 1] not in color:
                            returner = f"{returner} {location_to_letters(str(int(down_left[0])) + str(int(down_left[1]) + 1))}"
                        if board[int(down_left[0]) + 1][int(down_left[1])] not in color:
                            returner = f"{returner} {location_to_letters(str(int(down_left[0]) + 1) + str(int(down_left[1])))}"

        returner = returner.upper()
        # check if returner is empty
        if returner == "":
        # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()

    def queen_location_check(location_in_letters, color, board, ops):
        returner = ""
        if rook_location_check(location_in_letters, color, board, ops) != False:
            returner = f"{returner} {rook_location_check(location_in_letters, color, board, ops)}"
        if bishop_location_check(location_in_letters, color, board, ops) != False:
            returner = f"{returner} {bishop_location_check(location_in_letters, color, board, ops)}"

        # check if returner is empty
        if returner == "":
            # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()

    def king_location_check(location_in_letters, color, board, ops):
        location_in_numbers = location_to_numbers(location_in_letters)
        returner = ""

        if not top_end_check(location_in_letters):
            if board[int(location_in_numbers[0]) - 1][int(location_in_numbers[1])] not in color:
                returner = returner + " " + location_to_letters(f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1])}")

        if not bottom_end_check(location_in_letters):
            if board[int(location_in_numbers[0]) + 1][int(location_in_numbers[1])] not in color:
                returner = returner + " " + location_to_letters(f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1])}")

        if not left_corner_check(location_in_letters):
            if board[int(location_in_numbers[0])][int(location_in_numbers[1]) + 1] not in color:
                returner = returner + " " + location_to_letters(f"{int(location_in_numbers[0])}{int(location_in_numbers[1]) + 1}")

        if not right_corner_check(location_in_letters):
            if board[int(location_in_numbers[0])][int(location_in_numbers[1]) - 1] not in color:
                returner = returner + " " + location_to_letters(
                    f"{int(location_in_numbers[0])}{int(location_in_numbers[1]) - 1}")

        if not left_corner_check(location_in_letters):
            if not top_end_check(location_in_letters):
                if board[int(location_in_numbers[0]) - 1][int(location_in_numbers[1]) + 1] not in color:
                    returner = returner + " " + location_to_letters(f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) + 1}")

        if not right_corner_check(location_in_letters):
            if not top_end_check(location_in_letters):
                if board[int(location_in_numbers[0]) - 1][int(location_in_numbers[1]) - 1] not in color:
                    returner = returner + " " + location_to_letters(f"{int(location_in_numbers[0]) - 1}{int(location_in_numbers[1]) - 1}")

        if not left_corner_check(location_in_letters):
            if not bottom_end_check(location_in_letters):
                if board[int(location_in_numbers[0]) + 1][int(location_in_numbers[1]) + 1] not in color:
                    returner = returner + " " + location_to_letters(f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) + 1}")

        if not right_corner_check(location_in_letters):
            if not bottom_end_check(location_in_letters):
                if board[int(location_in_numbers[0]) + 1][int(location_in_numbers[1]) - 1] not in color:
                    returner = returner + " " + location_to_letters(f"{int(location_in_numbers[0]) + 1}{int(location_in_numbers[1]) - 1}")

        returner = returner.upper()
        # check if returner is empty
        if returner == "":
            # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()

    # create a function to check if the given pawns can move to the given location
    def location_check(location_in_letters, color, board, ops, color_name):

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
        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] not in color:
            return False

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[0]:
            if pawns_location_check(location_in_letters, color, board, ops, color_name) == False:
                return False

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[1]:
            if rook_location_check(location_in_letters, color, board, ops) == False:
                return False

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[2]:
            if bishop_location_check(location_in_letters, color, board, ops) == False:
                return False

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[3]:
            if knight_location_check(location_in_letters, color, board, ops) == False:
                return False

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[4]:
            if queen_location_check(location_in_letters, color, board, ops) == False:
                return False

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[5]:
            if king_location_check(location_in_letters, color, board, ops) == False:
                return False
        return True

    # create a function for the gameplay
    def moves(color, board, ops, player_name, color_name):
        # print the board
        display_board(board)
        # ask the player which piece
        scanner = input(f"{player_name} Which Piece Do You Want To Move: ")
        # check if the entered location is valid
        while not location_check(scanner, color, board, ops, color_name):
            print("You Didn't Type an Available Move")
            scanner = input(f"{player_name} Which Piece Do You Want To Move: ")

        location_in_numbers = location_to_numbers(scanner)
        temp_moves = ""
        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[0]:
            temp_moves = pawns_location_check(scanner, color, board, ops, color_name)

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[1]:
            temp_moves = rook_location_check(scanner, color, board, ops)

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[2]:
            temp_moves = bishop_location_check(scanner, color, board, ops)

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[3]:
            temp_moves = knight_location_check(scanner, color, board, ops)

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[4]:
            temp_moves = queen_location_check(scanner, color, board, ops)

        if board[int(location_in_numbers[0])][int(location_in_numbers[1])] == color[5]:
            temp_moves = king_location_check(scanner, color, board, ops)
        print(temp_moves)
        temp_moves = temp_moves.replace(" ", "")

        moves = {""}
        moves.remove("")
        for i in range(int(len(temp_moves) / 2)):
            moves.add(f"{temp_moves[i * 2]}{temp_moves[1 + i * 2]}")
        temp_location_name = scanner.upper()
        scanner = str.upper(input(f"Where Do You Want {temp_location_name} To Move:"))
        while scanner not in moves:
            print("You Didn't Type an Available Move")
            scanner = str.upper(input(f"Where Do You Want {temp_location_name} To Move:"))
        new_location_in_numbers = location_to_numbers(scanner)
        board[int(new_location_in_numbers[0])][int(new_location_in_numbers[1])] = board[int(location_in_numbers[0])][int(location_in_numbers[1])]
        board[int(location_in_numbers[0])][int(location_in_numbers[1])] = "ㅤ"


    current_player = True
    while not win_check(board):
        if current_player == True:
            moves(white, board, black, "Player 1", "white")
            current_player = False
        else:
            moves(black, board, white, "Player 2", "black")
            current_player = True
