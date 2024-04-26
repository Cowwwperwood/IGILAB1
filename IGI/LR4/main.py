from inputfunctions import inputCheck, TYPES
from task1.task1 import task1
from task2.task2 import task2
from task3.task3 import task3
from task4.task4 import task4
from task5.task5 import task5



while True:
    choice = int(input("please, enter the number of task or '0' for end: "))

    match choice:
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()
        case 5:
            task5()
        case 0:
            break
        case _:
            print("incorrect input.")

