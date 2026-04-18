from default import is_number
from default import contains_number
from default import list_is_number
import random
def backgammon():

    # store the players symbols
    player1 = "●"
    player2 = "○"
    board = [
        ["●", " ", " ", " ", "○", " ", "○", "●", "●", "●", "●", "●"],
        ["●", " ", " ", " ", "○", " ", "○", "●", "●", "●", "●", "●"],
        ["●", " ", " ", " ", "○", " ", "○", " ", " ", " ", " ", " "],
        ["●", " ", " ", " ", " ", " ", "○", " ", " ", " ", " ", " "],
        ["●", " ", " ", " ", " ", " ", "○", " ", " ", " ", " ", " "],
        ["○", " ", " ", " ", " ", " ", "●", " ", " ", " ", " ", " "],
        ["○", " ", " ", " ", " ", " ", "●", " ", " ", " ", " ", " "],
        ["○", " ", " ", " ", "●", " ", "●", " ", " ", " ", " ", " "],
        ["○", " ", " ", " ", "●", " ", "●", " ", " ", " ", " ", "○"],
        ["○", " ", " ", " ", "●", " ", "●", " ", " ", " ", " ", "○"]
        ]

    def numbers_to_dice(dice_in_numbers):
        dice = ["⚀","⚁","⚂","⚃","⚄","⚅"]
        return dice[dice_in_numbers - 1]
    def dice_to_numbers(dice):
        dice = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        n = -1
        for i in dice:
            n += 1
            if dice == i:
                return n

    def display_board(board,dice_in_numbers):
        print("\033[4m │A│B│C│D│E│F│││G│H│I│J│K│L│  \033[0m")
        print(f"1│{board[0][0]}│{board[0][1]}│{board[0][2]}│{board[0][3]}│{board[0][4]}│{board[0][5]}│││{board[0][6]}│{board[0][7]}│{board[0][8]}│{board[0][9]}│{board[0][10]}│{board[0][11]}│1")
        print(f" │{board[1][0]}│{board[1][1]}│{board[1][2]}│{board[1][3]}│{board[1][4]}│{board[1][5]}│││{board[1][6]}│{board[1][7]}│{board[1][8]}│{board[1][9]}│{board[1][10]}│{board[1][11]}│")
        print(f" │{board[2][0]}│{board[2][1]}│{board[2][2]}│{board[2][3]}│{board[2][4]}│{board[2][5]}│││{board[2][6]}│{board[2][7]}│{board[2][8]}│{board[2][9]}│{board[2][10]}│{board[2][11]}│")
        print(f" │{board[3][0]}│{board[3][1]}│{board[3][2]}│{board[3][3]}│{board[3][4]}│{board[3][5]}│││{board[3][6]}│{board[3][7]}│{board[3][8]}│{board[3][9]}│{board[3][10]}│{board[3][11]}│")
        print(f" \033[4m│{board[4][0]}│{board[4][1]}│{board[4][2]}│{board[4][3]}│{board[4][4]}│{board[4][5]}│││{board[4][6]}│{board[4][7]}│{board[4][8]}│{board[4][9]}│{board[4][10]}│{board[4][11]}│\033[0m    {numbers_to_dice(int(dice_in_numbers[0]))}{dice_in_numbers[0]}")
        print(f" │{board[5][0]}│{board[5][1]}│{board[5][2]}│{board[5][3]}│{board[5][4]}│{board[5][5]}│││{board[5][6]}│{board[5][7]}│{board[5][8]}│{board[5][9]}│{board[5][10]}│{board[5][11]}│    {numbers_to_dice(int(dice_in_numbers[1]))}{dice_in_numbers[1]}")
        print(f" │{board[6][0]}│{board[6][1]}│{board[6][2]}│{board[6][3]}│{board[6][4]}│{board[6][5]}│││{board[6][6]}│{board[6][7]}│{board[6][8]}│{board[6][9]}│{board[6][10]}│{board[6][11]}│")
        print(
            f" │{board[7][0]}│{board[7][1]}│{board[7][2]}│{board[7][3]}│{board[7][4]}│{board[7][5]}│││{board[7][6]}│{board[7][7]}│{board[7][8]}│{board[7][9]}│{board[7][10]}│{board[7][11]}│")
        print(
            f" │{board[8][0]}│{board[8][1]}│{board[8][2]}│{board[8][3]}│{board[8][4]}│{board[8][5]}│││{board[8][6]}│{board[8][7]}│{board[8][8]}│{board[8][9]}│{board[8][10]}│{board[8][11]}│")
        print(f"\033[4m2│{board[9][0]}│{board[9][1]}│{board[9][2]}│{board[9][3]}│{board[9][4]}│{board[9][5]}│││{board[9][6]}│{board[9][7]}│{board[9][8]}│{board[9][9]}│{board[9][10]}│{board[9][11]}│2\033[0m")
        print(" │A│B│C│D│E│F│││G│H│I│J│K│L│")

    # create a function to make location in numbers to letters
    def location_to_letters(location_in_numbers):
        # set itself to string, so you can take parts of him
        location_in_numbers = str(location_in_numbers)
        location_in_numbers1 = str(int(f"{location_in_numbers[0]}{location_in_numbers[1]}"))
        location_in_numbers2 = str(int(f"{location_in_numbers[2]}{location_in_numbers[3]}"))
        # create an array of letters
        letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        if int(location_in_numbers1) == 0:
            return f"{letters_list[int(location_in_numbers2)]}{1}"
        else:
            return f"{letters_list[int(location_in_numbers2)]}{2}"

    def location_to_numbers(location_in_letters):
        location_in_letters = str.lower(location_in_letters)
        letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        n = -1
        for i in letters_list:
            n += 1
            if location_in_letters[0] == i:
                if n > 10:
                    if location_in_letters[1] == "1":
                        return f"{'00'}{f'{n}'}"
                    else:
                        return f"{'09'}{f'{n}'}"
                else:
                    if location_in_letters[1] == "1":
                        return f"{'00'}{f'0{n}'}"
                    else:
                        return f"{'09'}{f'0{n}'}"

    def stack_check(color,location_in_numbers, board, every_stack):

        if location_in_numbers[1] == "9":
            c = 0
            while color == board[int(f"{location_in_numbers[0]}{location_in_numbers[1]}")][int(f"{location_in_numbers[2]}{location_in_numbers[3]}")] and c != 5:
                if int(f"{location_in_numbers[0]}{location_in_numbers[1]}") < 10:
                    location_in_numbers = f"0{int(location_in_numbers) - 100}"
                    c += 1
                else:
                    location_in_numbers = f"{int(location_in_numbers) - 100}"
                    c += 1
            if not every_stack:
                if int(f"{location_in_numbers[0]}{location_in_numbers[1]}") < 10:
                    location_in_numbers = f"0{int(location_in_numbers) + 100}"
                else:
                    location_in_numbers = f"{int(location_in_numbers) + 100}"
        if location_in_numbers[1] == "0":
            c = 0
            while color == board[int(f"{location_in_numbers[0]}{location_in_numbers[1]}")][int(f"{location_in_numbers[2]}{location_in_numbers[3]}")] and c != 5:
                if int(f"{location_in_numbers[0]}{location_in_numbers[1]}") < 10:
                    location_in_numbers = f"0{int(location_in_numbers) + 100}"
                    c += 1
                else:
                    location_in_numbers = f"{int(location_in_numbers) + 100}"
                    c += 1
            if not every_stack:
                if int(f"{location_in_numbers[0]}{location_in_numbers[1]}") < 10:
                    location_in_numbers = f"0{int(location_in_numbers) - 100}"
                else:
                    location_in_numbers = f"{int(location_in_numbers) - 100}"

            if len(location_in_numbers) == 2:
                location_in_numbers = f"00{location_in_numbers}"
        return location_in_numbers

    def pawns_move(move1,move2, color, board, location_in_letters, enemy_color, enemy_ate):
        location_in_numbers1 = location_to_numbers(location_in_letters)
        location_in_numbers2 = location_to_numbers(location_in_letters)
        location_in_letters1 = location_in_letters
        location_in_letters2 = location_in_letters
        returner = ""
        if color == "●":
            if location_in_letters1[1] == "1":
                if (int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")) - move1 < 0:
                    move1 = int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") - (int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") - move1) - 1
                    location_in_letters1 = f"{location_in_letters1[0]}2"
                    location_in_numbers1 = location_to_numbers(location_in_letters1)
                else:
                    if int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') - move1 > 9:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') - move1}"
                    else:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}0{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') - move1}"
                    if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color,location_in_numbers1,board,False) == location_in_numbers1:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == color:
                        if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") - 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"

            if location_in_letters1[1] == "2":
                if not (int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")) + move1 > 9:
                    if int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') + move1 > 9:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') + move1}"
                    else:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}0{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') + move1}"
                    if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color,location_in_numbers1,board,False) == location_in_numbers1:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == color:
                        if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") + 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"

            if location_in_letters2[1] == "1":
                if (int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")) - move2 < 0:
                    move2 = int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") - (int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") - move2) - 1
                    location_in_letters2 = f"{location_in_letters2[0]}2"
                    location_in_numbers2 = location_to_numbers(location_in_letters2)
                else:
                    if int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') - move2 > 9:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') - move2}"
                    else:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}0{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') - move2}"
                    if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color,location_in_numbers2,board,False) == location_in_numbers2:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == color:
                        if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") - 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"

            if location_in_letters2[1] == "2":
                if not (int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")) + move2 > 11:
                    if int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') + move2 > 9:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') + move2}"
                    else:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}0{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') + move2}"
                    if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color,location_in_numbers2,board,False) == location_in_numbers2:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == color:
                        if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") + 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"
        if color == "○":
            if location_in_letters1[1] == "1":
                if (int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")) + move1 > 9:
                    move1 = int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") - (int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") - move1) - 1
                    location_in_letters1 = f"{location_in_letters1[0]}2"
                    location_in_numbers1 = location_to_numbers(location_in_letters1)
                else:
                    if int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') + move1 >= 10:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') + move1}"
                    else:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}0{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') + move1}"
                    if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color, location_in_numbers1, board,False) == location_in_numbers1:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == color:
                        if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") - 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"

            if location_in_letters1[1] == "2":
                if not (int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")) - move1 < 0:
                    if int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') - move1 >= 10:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') - move1}"
                    else:
                        location_in_numbers1 = f"{location_in_numbers1[0]}{location_in_numbers1[1]}0{int(f'{location_in_numbers1[2]}{location_in_numbers1[3]}') - move1}"
                    if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color, location_in_numbers1, board,False) == location_in_numbers1:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers1)}"
                    elif board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}")] == color:
                        if board[int(f"{location_in_numbers1[0]}{location_in_numbers1[1]}")][int(f"{location_in_numbers1[2]}{location_in_numbers1[3]}") + 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers1)}"

            if location_in_letters2[1] == "1":
                if (int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")) + move2 > 11:
                    move2 = int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") - (int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") - move2) - 1
                    location_in_letters2 = f"{location_in_letters2[0]}2"
                    location_in_numbers2 = location_to_numbers(location_in_letters2)
                else:
                    if int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') + move2 >= 10:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') + move2}"
                    else:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}0{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') + move2}"
                    if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color, location_in_numbers2, board,False) == location_in_numbers2:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == color:
                        if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") - 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"
            if location_in_letters2[1] == "2":
                if not (int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")) - move2 < 0:
                    if int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') - move2 >= 10:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') - move2}"
                    else:
                        location_in_numbers2 = f"{location_in_numbers2[0]}{location_in_numbers2[1]}0{int(f'{location_in_numbers2[2]}{location_in_numbers2[3]}') - move2}"
                    if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == enemy_color and not enemy_ate:
                        if stack_check(enemy_color, location_in_numbers2, board,False) == location_in_numbers2:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][
                        int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == " ":
                        returner = f"{returner} {location_to_letters(location_in_numbers2)}"
                    elif board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}")] == color:
                        if board[int(f"{location_in_numbers2[0]}{location_in_numbers2[1]}")][int(f"{location_in_numbers2[2]}{location_in_numbers2[3]}") - 4] != color:
                            returner = f"{returner} {location_to_letters(location_in_numbers2)}"
        returner = returner.upper()
        # check if returner is empty
        if returner == "":
            # return false if so
            return False
        # return returner without white spaces
        return returner.lstrip()
    def move_check(move1, move2, color, board, location_in_letters):
        location_in_numbers = location_to_numbers(location_in_letters)
        if len(location_in_letters) != 2:
            return False
        if board[int(f"{location_in_numbers[0]}{location_in_numbers[1]}")][int(f"{location_in_numbers[2]}{location_in_numbers[3]}")] != color:
            return False

    def move(board, current_player, player_color, enemy_color,enemy_ate):
        ate = False
        move1 = str(random.randint(1,6))
        move2 = str(random.randint(1,6))
        while move2 == move1:
            move1 = str(random.randint(1, 6))
            move2 = str(random.randint(1, 6))
        available_move = {move2,move1}
        display_board(board,f"{move1}{move2}")
        scanner = input(f"{current_player}, Which Pawn Do You Want To Move:")
        while pawns_move(int(move1),int(move2),player_color,board,scanner,enemy_color,enemy_ate) == False:
            print("You Didn't Type an Available Pawn")
            scanner = input(f"{current_player}, Which Pawn Do You Want To Move:")
        moves = str.lstrip(str.lower(pawns_move(int(move1), int(move2), player_color, board, scanner, enemy_color,enemy_ate)))
        current_location_in_numbers = stack_check(player_color, location_to_numbers(scanner), board,False)
        print(f"The Available Moves Are:", end="")
        print(str.upper(moves))
        selected_pawn = scanner
        scanner = str.lower(input(f"Where Do You Want {str.upper(selected_pawn)} To Move:"))
        while scanner not in moves:
            print("You Didn't Type an Available Move")
            scanner = str.lower(input(f"Where Do You Want {str.upper(selected_pawn)} To Move:"))
        next_move_in_numbers = location_to_numbers(scanner)
        if board[int(f"{next_move_in_numbers[0]}{next_move_in_numbers[1]}")][int(f"{next_move_in_numbers[2]}{next_move_in_numbers[3]}")] == " ":
            board[int(f"{next_move_in_numbers[0]}{next_move_in_numbers[1]}")][int(f"{next_move_in_numbers[2]}{next_move_in_numbers[3]}")] = player_color
            board[int(f"{current_location_in_numbers[0]}{current_location_in_numbers[1]}")][int(f"{current_location_in_numbers[2]}{current_location_in_numbers[3]}")] = " "
        elif board[int(f"{next_move_in_numbers[0]}{next_move_in_numbers[1]}")][int(f"{next_move_in_numbers[2]}{next_move_in_numbers[3]}")] == player_color:
            board[int(f"{current_location_in_numbers[0]}{current_location_in_numbers[1]}")][int(f"{current_location_in_numbers[2]}{current_location_in_numbers[3]}")] = " "
            next_move_in_numbers = stack_check(player_color,next_move_in_numbers,board,True)
            board[int(f"{next_move_in_numbers[0]}{next_move_in_numbers[1]}")][int(f"{next_move_in_numbers[2]}{next_move_in_numbers[3]}")] = player_color
        return ate

    game = True
    turn = True
    white_ate = False
    black_ate = False
    while game:
        if turn:
            if not white_ate:
                black_ate = move(board, "Player 1", player1, player2, black_ate)
            turn = not turn
        else:
            if not black_ate:
                white_ate = move(board, "Player 2", player2, player1, white_ate)
            turn = not turn
