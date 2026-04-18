import random
from default import is_number
from default import contains_number
from default import list_is_number

def bingo():
    # make the players numbers board
    global player1
    global player2
    global player3
    global player4
    global player5

    # check if the random number is in the numbers
    def random_number_check(player_number, player_board, random_number):
        # create a loop of the length of the player_board
        for i in range(len(player_board)):
            # checking if it isn't empty
            if is_number(player_board[i]):
                # checking if it's equal to random number
                if int(player_board[i]) == random_number:
                    # if so it's removing the number
                    player_board[i] = "  "
                    # print the name of the player
                    print(f' {players_name[player_number - 1].replace(" ", "")}', end="")

    # create a function for setting the name and the random numbers
    def player_create(player_number, player_board):

        # ask the player for a name
        players_name[player_number - 1] = input(f"What Is Player's {player_number} Name:")

        # checking the name isn't too long or too short
        while len(players_name[player_number - 1]) > 10 or len(players_name[player_number - 1]) < 1:
            # print an error if the name is too long or too short
            print("Error: The Name You Entered Is Too Short Or Too Long")
            # ask for the player name
            players_name[player_number - 1] = input(f"What Is Player's {player_number} Name:")
        # add to the player name spaces for the interface look
        players_name[player_number - 1] = players_name[player_number - 1] + " " * (14 - len(players_name[player_number - 1]))

        # create a list for used numbers so no double numbers
        used_numbers = {""}
        # create a loop of 16
        for i in range(16):
            # set random number from 1-32
            random_number = int(random.randint(1, 32))
            # checking if the random number is used
            while random_number in used_numbers:
                # set random number from 1-32
                random_number = int(random.randint(1, 32))
            # add the used numbers
            used_numbers.add(random_number)
            # set the player board to the random number
            player_board[i] = random_number
        # create a loop of the length of player board
        for i in range(len(player_board)):
            # checking if the number is less than 10
            if int(player_board[i]) < 10:
                # add white space if so
                player_board[i] = f"{player_board[i]} "
    # create a function to check if someone won
    def win_check():
        # if players is 1
        if players == 1:
            # check if the player board is with numbers
            if list_is_number(player1):
                # if so not everything is empty so false
                return False
            else:
                return True

        if players == 2:
            # check if the player board is with numbers
            if list_is_number(player1) and list_is_number(player2):
                # if so not everything is empty so false
                return False
            else:
                return True
        if players == 3:
            # check if the player board is with numbers
            if list_is_number(player1) and list_is_number(player2) and list_is_number(player3):
                # if so not everything is empty so false
                return False
            else:
                return True
        if players == 4:
            # check if the player board is with numbers
            if list_is_number(player1) and list_is_number(player2) and list_is_number(player3) and list_is_number(
                    player4):
                # if so not everything is empty so false
                return False
            else:
                return True
        if players == 5:
            # check if the player board is with numbers
            if list_is_number(player1) and list_is_number(player2) and list_is_number(player3) and list_is_number(
                    player4) and list_is_number(player5):
                # if so not everything is empty so false
                return False
            else:
                return True
    # check if someone won
    def player_win_check():
        if players > 0:
            # check if there aren't any numbers in player board
            if not list_is_number(player1):
                # return the player name
                return players_name[0].replace(" ", "")
        if players > 1:
            # check if there aren't any numbers in player board
            if not list_is_number(player2):
                # return the player name
                return players_name[1].replace(" ", "")
        if players > 2:
            # check if there aren't any numbers in player board
            if not list_is_number(player3):
                # return the player name
                return players_name[2].replace(" ", "")
        if players > 3:
            # check if there aren't any numbers in player board
            if not list_is_number(player4):
                # return the player name
                return players_name[3].replace(" ", "")
        if players > 4:
            # check if there aren't any numbers in player board
            if not list_is_number(player5):
                # return the player name
                return players_name[4].replace(" ", "")
        return True

    # create a function for printing the board
    def board():
        if players == 1:
            print(players_name[0])
            print(f"{player1[0]}│{player1[1]}│{player1[2]}│{player1[3]}")
            print(f"━━│━━│━━│━━")
            print(f"{player1[4]}│{player1[5]}│{player1[6]}│{player1[7]}")
            print(f"━━│━━│━━│━━")
            print(f"{player1[8]}│{player1[9]}│{player1[10]}│{player1[11]}")
            print(f"━━│━━│━━│━━")
            print(f"{player1[12]}│{player1[13]}│{player1[14]}│{player1[15]}")
        if players == 2:
            print(players_name[0], players_name[1])
            print(
                f"{player1[0]}│{player1[1]}│{player1[2]}│{player1[3]}    {player2[0]}│{player2[1]}│{player2[2]}│{player2[3]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━ ")
            print(
                f"{player1[4]}│{player1[5]}│{player1[6]}│{player1[7]}    {player2[4]}│{player2[5]}│{player2[6]}│{player2[7]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━ ")
            print(
                f"{player1[8]}│{player1[9]}│{player1[10]}│{player1[11]}    {player2[8]}│{player2[9]}│{player2[10]}│{player2[11]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━ ")
            print(
                f"{player1[12]}│{player1[13]}│{player1[14]}│{player1[15]}    {player2[12]}│{player2[13]}│{player2[14]}│{player2[15]}")
        if players == 3:
            print(players_name[0], players_name[1], players_name[2])
            print(
                f"{player1[0]}│{player1[1]}│{player1[2]}│{player1[3]}    {player2[0]}│{player2[1]}│{player2[2]}│{player2[3]}    {player3[0]}│{player3[1]}│{player3[2]}│{player3[3]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━ ")
            print(
                f"{player1[4]}│{player1[5]}│{player1[6]}│{player1[7]}    {player2[4]}│{player2[5]}│{player2[6]}│{player2[7]}    {player3[4]}│{player3[5]}│{player3[6]}│{player3[7]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━ ")
            print(
                f"{player1[8]}│{player1[9]}│{player1[10]}│{player1[11]}    {player2[8]}│{player2[9]}│{player2[10]}│{player2[11]}    {player3[8]}│{player3[9]}│{player3[10]}│{player3[11]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━ ")
            print(
                f"{player1[12]}│{player1[13]}│{player1[14]}│{player1[15]}    {player2[12]}│{player2[13]}│{player2[14]}│{player2[15]}    {player3[12]}│{player3[13]}│{player3[14]}│{player3[15]}")
        if players == 4:
            print(players_name[0], players_name[1], players_name[2], players_name[3])
            print(
                f"{player1[0]}│{player1[1]}│{player1[2]}│{player1[3]}    {player2[0]}│{player2[1]}│{player2[2]}│{player2[3]}    {player3[0]}│{player3[1]}│{player3[2]}│{player3[3]}    {player4[0]}│{player4[1]}│{player4[2]}│{player4[3]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━")
            print(
                f"{player1[4]}│{player1[5]}│{player1[6]}│{player1[7]}    {player2[4]}│{player2[5]}│{player2[6]}│{player2[7]}    {player3[4]}│{player3[5]}│{player3[6]}│{player3[7]}    {player4[4]}│{player4[5]}│{player4[6]}│{player4[7]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━")
            print(
                f"{player1[8]}│{player1[9]}│{player1[10]}│{player1[11]}    {player2[8]}│{player2[9]}│{player2[10]}│{player2[11]}    {player3[8]}│{player3[9]}│{player3[10]}│{player3[11]}    {player4[8]}│{player4[9]}│{player4[10]}│{player4[11]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━")
            print(
                f"{player1[12]}│{player1[13]}│{player1[14]}│{player1[15]}    {player2[12]}│{player2[13]}│{player2[14]}│{player2[15]}    {player3[12]}│{player3[13]}│{player3[14]}│{player3[15]}    {player4[12]}│{player4[13]}│{player4[14]}│{player4[15]}")
        if players == 5:
            print(players_name[0], players_name[1], players_name[2], players_name[3], players_name[4])
            print(
                f"{player1[0]}│{player1[1]}│{player1[2]}│{player1[3]}    {player2[0]}│{player2[1]}│{player2[2]}│{player2[3]}    {player3[0]}│{player3[1]}│{player3[2]}│{player3[3]}    {player4[0]}│{player4[1]}│{player4[2]}│{player4[3]}    {player5[0]}│{player5[1]}│{player5[2]}│{player5[3]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━")
            print(
                f"{player1[4]}│{player1[5]}│{player1[6]}│{player1[7]}    {player2[4]}│{player2[5]}│{player2[6]}│{player2[7]}    {player3[4]}│{player3[5]}│{player3[6]}│{player3[7]}    {player4[4]}│{player4[5]}│{player4[6]}│{player4[7]}    {player5[4]}│{player5[5]}│{player5[6]}│{player5[7]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━")
            print(
                f"{player1[8]}│{player1[9]}│{player1[10]}│{player1[11]}    {player2[8]}│{player2[9]}│{player2[10]}│{player2[11]}    {player3[8]}│{player3[9]}│{player3[10]}│{player3[11]}    {player4[8]}│{player4[9]}│{player4[10]}│{player4[11]}    {player5[8]}│{player5[9]}│{player5[10]}│{player5[11]}")
            print(f"━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━    ━━│━━│━━│━━")
            print(
                f"{player1[12]}│{player1[13]}│{player1[14]}│{player1[15]}    {player2[12]}│{player2[13]}│{player2[14]}│{player2[15]}    {player3[12]}│{player3[13]}│{player3[14]}│{player3[15]}    {player4[12]}│{player4[13]}│{player4[14]}│{player4[15]}    {player5[12]}│{player5[13]}│{player5[14]}│{player5[15]}")
    while True:
        # ask the player a number between 1-5
        scanner = input("How much Players Will Be(1-5)?")
        # quit check for admin
        if scanner == "quit":
            break
        # check if the input is a number and 1-5
        while not is_number(scanner) or 1 > int(scanner) or int(scanner) > 5:
            # print an error message
            print("Error: The Number You Entered Is Not 1-5 Or a Number")
            # ask the player a number between 1-5
            scanner = input("how much players will be(1-5)?")
            # quit check for admin
            if scanner == "quit":
                break
        # set the player count to the input
        players = int(scanner)
        # create an array for the names
        players_name = ["", "", "", "", ""]


        # no need to check because it will always be greater than 1

        # create the player board
        player1 = ["" for I in range(16)]
        # call the function player create
        player_create(1, player1)
        # check if there will be more the 1 player
        if players > 1:
            # create the player board
            player2 = ["" for I in range(16)]
            # call the function player create
            player_create(2, player2)
        # check if there will be more the 2 players
        if players > 2:
            # create the player board
            player3 = ["" for I in range(16)]
            # call the function player create
            player_create(3, player3)
        # check if there will be more the 3 players
        if players > 3:
            # create the player board
            player4 = ["" for I in range(16)]
            # call the function player create
            player_create(4, player4)
        # check if there will be more the 4 players
        if players > 4:
            # create the player board
            player5 = ["" for I in range(16)]
            # call the function player create
            player_create(5, player5)

        # keeps the game running
        while not win_check():
            # print the board
            board()
            input("Are You Ready?")
            # create a random number between 1-32
            random_number = int(random.randint(1, 32))
            # print the random number
            print(f"The Players That Have {random_number} Are:", end="")

            # check the random numbers in player1's board
            random_number_check(1, player1, random_number)
            # check if there is more players than 1
            if players > 1:
                # check the random numbers in player2's board
                random_number_check(2, player2, random_number)
            # check if there is more players than 2
            if players > 2:
                # check the random numbers in player3's board
                random_number_check(3, player3, random_number)
            # check if there is more players than 3
            if players > 3:
                # check the random numbers in player4's board
                random_number_check(4, player4, random_number)
            # check if there is more players than 4
            if players > 4:
                # check the random numbers in player5's board
                random_number_check(5, player5, random_number)
            print("")
        # print the board
        board()
        # print the winner
        print(f"\nThe Winner Is {player_win_check()}")