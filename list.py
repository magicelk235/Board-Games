import random
from default import is_number
from default import contains_number
from default import list_is_number

def listing():
    # create the list that store everything
    list_name = {""}
    # create a list of the actions
    actions = {"add", "list", "remove", "quit", "?"}

    # print the explanations
    print("Explain:\nIf You Want To Add Something Type \"add\"")
    print("If You Want To See The List Type \"list\"")
    print("If You Want To Remove Type \"remove\"")
    print("If You Want To Quit Type \"quit\"")
    print("If You Want To See This Again Type \"?\"")

    while True:

        # ask for an action
        scanner = str.lower(input("Type Action:"))
        # check if you type an action
        while scanner not in actions:
            # print an error message
            print("Error: You Didn't Type an Actions")
            scanner = input("Type Action:")

        # check the action type is add
        if scanner == "add":
            # sak for something to add
            scanner = input("Type Something:")
            list_name.add(scanner)

        # check the action type is list
        elif scanner == "list":
            print(list_name)

        # check the action type is remove
        elif scanner == "remove":
            # ask for something to remove
            scanner = input("Type Something:")
            # check if the input is in the list
            while scanner not in list_name:
                # print an error message
                print(f"Error: {scanner} Isn't In The List")
                scanner = input("Type Something:")
            # Remove it After The Checking
            list_name.remove(scanner)

        # check the action type ?
        elif scanner == "?":
            print("Explain:\nIf You Want To Add Something Type \"add\"")
            print("If You Want To See The List Type \"list\"")
            print("If You Want To Remove Type \"remove\"")
            print("If You Want To Quit Type \"quit\"")
            print("If You Want To See This Again Type \"?\"")

        # check the action type quit
        elif scanner == "quit":
            break