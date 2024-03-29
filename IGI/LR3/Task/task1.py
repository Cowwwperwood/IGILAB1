import math
from inputfunctions import inputCheck, TYPES
from decorators import taskName


def exp(x, eps):
    result = 0
    i = 0
    while (math.exp(x) - result > eps and i + 1 < 500):
        result += (x ** i / math.factorial(i))
        i += 1
    return result, i + 1

@taskName
def task1():
    while True:
        x = inputCheck('please, input x: ', TYPES.FLOAT)
        eps = inputCheck('please, input eps: ', TYPES.FLOAT)
        F, n = exp(x, eps)
        print(" x:", x, '\n', "n:", n, '\n', "F(x): ", F, '\n', "Math F(x):", math.exp(x), '\n', "Eps:", eps)
        return