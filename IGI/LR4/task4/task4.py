from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
import numpy as np


class MyMixin:
    def log(self):
        print("Mixin func activated")


class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class FigureColor(MyMixin):
    def __init__(self, color):
        self._color = color
        self.log()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


class Triangle(GeometricFigure):
    def __init__(self, side_a, side_b, angle_c, color, name):
        super().__init__()
        self._side_a = side_a
        self._side_b = side_b
        self._angle_c = angle_c
        self._color = FigureColor(color)
        self._name = name

    def calculate_area(self):
        radian_c = math.radians(self._angle_c)
        return 0.5 * self._side_a * self._side_b * math.sin(radian_c)

    def __str__(self):
        return "Треугольник {0} цвета, сторона a: {1}, сторона b: {2}, угол C: {3} градусов, площадь: {4}".format(
            self._color.color, self._side_a, self._side_b, self._angle_c, self.calculate_area()
        )


class TriangleDrawer:
    def __init__(self, triangle):
        self._triangle = triangle

    def draw(self):
        x = [0, self._triangle._side_a, self._triangle._side_b * np.cos(np.radians(self._triangle._angle_c))]
        y = [0, 0, self._triangle._side_b * np.sin(np.radians(self._triangle._angle_c))]

        plt.figure()
        plt.plot(x + [0], y + [0])
        plt.fill(x, y, color=self._triangle._color.color)

        plt.axis('equal')
        plt.xlim(0, max(x) * 1.1)
        plt.ylim(0, max(y) * 1.1)
        plt.title(self._triangle._name)
        plt.savefig(r'triangle.png', dpi=300)
        plt.show()


def task4():
    name = input("Введите имя треугольника: ")
    side_a = float(input("Введите сторону a треугольника: "))
    side_b = float(input("Введите сторону b треугольника: "))
    angle_c = float(input("Введите угол C треугольника в градусах: "))
    color = input("Введите цвет треугольника: ")

    triangle = Triangle(side_a, side_b, angle_c, color, name)
    print(triangle)

    drawer = TriangleDrawer(triangle)
    drawer.draw()