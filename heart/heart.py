import math
from turtle import *


def Y(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


def X(k):
    return 15 * math.sin(k) ** 3


speed(0)
bgcolor("black")

for i in range(10000):
    x = X(i) * 20
    y = Y(i) * 20

    goto(x, y)
    color("#f73487")

    goto(0, 0)

done()
