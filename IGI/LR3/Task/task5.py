from inputfunctions import listInput
from decorators import taskName


def calculateSumBetweenFirstAndLastPositiveElement(lst):
    l = None
    r = None
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > 0:
            r = i
            break

    for i in range(len(lst)):
        if lst[i] > 0:
            l = i + 1
            break

    sum = 0

    for i in range(l, r):
        sum += lst[i]
    return sum

@taskName
def task5():
    lst = listInput()
    print("Minimal modulus element:", min(lst, key=lambda x: abs(x)))
    print(calculateSumBetweenFirstAndLastPositiveElement(lst))