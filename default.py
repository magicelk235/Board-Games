def is_number(inputs):
    try:
        # try to make the input float
        float(inputs)
        # return true if he made the input float
        return True
    # check to see if there are any errors and if so he returns false
    except:
        return False

def contains_number(inputs):
    # create a loop of the length of the input
    for i in range(len(inputs)):
        # check if the letter in place "i" is a number
        if is_number(inputs[i]):
            return True
    # if nothing is a number he returns false
    return False

def list_is_number(inputs):
    # create a loop of the list's length
    for i in range(len(inputs)):
        # check if the letter in place "i" is a number(and remove spaces because the main use is in bingo)
        if is_number(str(inputs[i]).replace(" ", "")):
            return True
    # if nothing is a number he returns false
    return False