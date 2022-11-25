import matplotlib.pyplot as plt
import numpy as np
from random import randint


def arr_cr(n, z):
    m = []
    for i in range(n):
        m.append(randint(0, z))
    return m


def num_cou(y, z):
    m = []
    for i in range(z+1):
        m.append(y.count(i))
    return m


def math_w(x, y):
    res = 0
    for i in range(x, y + 1, 1):
        res = res + i * (counted[i] / a)
    return res


def av_sq(x, y):
    res = 0
    for i in range(x, y + 1, 1):
        res = res + (counted[i] * (i - wait) ** 2)
    res = res / a
    return res


def coef(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    return b_0, b_1


def graph(x, y, b):
    sc = plt.scatter(x, y, color="m", marker="o", s=30)
    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


a = int(input("Введите длинну массива: "))
c = int(input("Введите максимальное число, которое может случайным образом оказаться в массиве (от 0 до ???): "))
mas = arr_cr(a, c)
counted = num_cou(mas, c)
maximum = 0
minimum = c
for j in range(len(mas)):
    if mas[j] > maximum:
        maximum = mas[j]
    if mas[j] < minimum:
        minimum = mas[j]
vec_x = []
vec_y = []
for i in range(len(mas)):
    vec_x.append(i + 1)
    vec_y.append(mas[i])
vec_x = np.array(vec_x)
vec_y = np.array(vec_y)
wait = math_w(minimum, maximum)
print("\nМатематическое ожидание =", wait)
print("\nДисперсия:", av_sq(minimum, maximum))
graph(vec_x, vec_y, coef(vec_x, vec_y))
