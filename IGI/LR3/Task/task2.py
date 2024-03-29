from inputfunctions import sequenceUserInput, sequenceRandomInput, inputCheck, TYPES
from decorators import taskName

def SumInList(lst):
    sum = 0
    for i in range(0, len(lst), 2):
        sum += int(lst[i])
    return sum


@taskName
def task2():
    lst = []
    while True:
        choice = inputCheck("please, choose option: 1 - user input, 2 - random input: ", TYPES.INT)

        match choice:
            case 1:
                lst = sequenceUserInput()
                print('Sum:', SumInList(lst))
                return
            case 2:
                lst = sequenceRandomInput()
                print('Sum:', SumInList(lst))
                return
            case _:
                print("incorrect input, please enter one more time: ")