import random
from default import is_number
from default import contains_number
from default import list_is_number

def calculator():

    # list of math_operation
    math_operation_list = {"-", "+", "*", "/", "%", "**"}
    # create the solver for later
    solver = ""

    # print explanation
    print("Explain:")
    print("Type \"=\" To See The Result ")
    print("Type \"?\" To See What You Already Written")
    print()

    # create an endless loop
    while True:

        # ask for a number as an input
        scanner = input("Type a Number: ")
        # check if one of the action were called
        if scanner == "?":
            print(solver.lstrip())
        if scanner == "=":
            break
        # check if a number
        while not is_number(scanner):
            # print an error message
            print("You Didn't Type a Number")
            scanner = input("Type a Number: ")
            # check if one of the action were called
            if scanner == "?":
                print(solver.lstrip())
            if scanner == "=":
                break
        # store the number for later
        solver = f"{solver} {scanner}"

        # ask for math operation
        math_operation = input("Type a Math Operation: ")
        # check if one of the action were called
        if math_operation == "?":
            print(solver.lstrip())
        if math_operation == "=":
            break
        # check if the input is a math operation
        while math_operation not in math_operation_list:
            # print an Error message
            print("You Didn't Type a Math Operation(-, +, *, /, %, **)")
            math_operation = input("Type a Math Operation: ")
            # check if one of the action were called
            if math_operation == "?":
                print(solver.lstrip())
            if math_operation == "=":
                break
        # store the math operation for later
        solver = f"{solver} {math_operation}"

    # check if there is something to solve
    if solver != "":
        # print the resolute
        try:
            print(f"{solver.lstrip()} = {eval(solver.lstrip())}")
        except:
            print("Math Error")