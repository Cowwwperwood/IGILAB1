import math
import statistics
import matplotlib.pyplot as plt
import numpy as np


def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


class SeriesPlotBuilder:
    def __init__(self, iterations):
        self._iterations = iterations

    def showPlot(self):
        x = np.linspace(-5, 5, 200)
        y1 = np.exp(x)
        y2 = sum(x ** i / math.factorial(i) for i in range(self._iterations))

        plt.plot(x, y1, label='e^x', color='r')
        plt.plot(x, y2, label='Series', color='g')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Series Convergence for e^x')
        plt.legend()

        plt.grid(True)
        plt.savefig(r'plots.png', dpi=300)
        plt.show()


class Series:
    def __init__(self, x, eps):
        self._x = x
        self._eps = eps

    def calculateSeries(self):
        series = []
        seriesResult = 0.0
        for i in range(500):
            term = self._x ** i / math.factorial(i)
            series.append(term)
            seriesResult += term
            if abs(seriesResult - math.exp(self._x)) <= self._eps:
                print(f"x = {self._x}, n = {i}, F(x) = {round(seriesResult, 10)},"
                      f" Math F(x) = {round(math.exp(self._x), 10)}"
                      f", eps = {self._eps}")

                print(f"Среднее значение элементов ряда: {round(seriesResult/(i + 1), 10)}")
                print(f"Медиана: {statistics.median(series)}")
                print(f"Мода: {statistics.multimode(series)}")
                print(f"Дисперсия: {statistics.variance(series)}")
                print(f"Среднее отклонение: {statistics.stdev(series)}")
                return i

        print("Достигнуто максимальное количество итераций.")
        return -1


def task3():
    while True:
        x = float(input('please, input x: '))
        eps = float(input('please, input eps: '))
        series = Series(x, eps)
        n = series.calculateSeries()
        print(n)
        seriesPlotBuilder = SeriesPlotBuilder(int(input('input n: ')))
        seriesPlotBuilder.showPlot()
        return



