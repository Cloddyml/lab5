from random import randint


def cr_arr(a):
    m = []
    for i in range(a):
        m.append(randint(0, 1))
    return m
