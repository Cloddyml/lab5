from random import randint


def num_cou(y, z):
    m = []
    temp_m = list(set(y))
    for i in range(len(y)):
        if i < z:
            if y[i] != 0 and i >= minimum and i in temp_m:
                m.append(y.count(i))
                temp_m.remove(i)
        else:
            if y[len(mas) - 1] != 0 and i >= minimum and i in temp_m:
                m.append(y.count(i))
                temp_m.remove(i)
    return m


def math_ex_y(m):
    res = 0
    m = sorted(m)
    for i in range(len(counted)):
        if counted[i] != 0:
            res += (counted[i] / len(m)) * (i + minimum)
    return res


def math_ex_x(m):
    res = 0
    for i in range(len(m)):
        res += (1 / len(m)) * i
    return res


def read_f(f, m):
    m = f.read().splitlines()
    for i in range(len(m)):
        m[i] = m[i].strip()
        m[i] = float(m[i])
    return m


def vinz(m):
    for i in range(1, len(m) - 1, 2):
        m[i] = 0
    print(*m)
    for i in range(1, len(m) - 1, 2):
        if i < len(m):
            m[i] = m[i + 1]
        else:
            m[i] = m[i - 1]


def lean(m):
    temp = 0
    for i in range(len(m)):
        if m[i] == 0 and i != 0 and i != len(m) - 1:
            for j in range(i, len(m), 1):
                if m[i] != m[j]:
                    temp = j
                    break
            sx1 = i - 1
            sy1 = m[i - 1]
            sx2 = temp
            sy2 = m[temp]
            s_k = int((sy1 - sy2) / (sx1 - sx2) + 0.5)
            s_b = sy1 - s_k * sx1
            for j in range(i, j, 1):
                m[j] = s_k * j + s_b
            i += temp
    return m


def corr(m):
    sum_1 = 0
    sum_2 = 0
    for i in range(len(m)):
        sum_1 += (i - temp_x) * (m[i] - temp_y)
        sum_2 += (i - temp_x) * (i - temp_x) * (m[i] - temp_y) * (m[i] - temp_y)
    sum_2 = sum_2 ** (1 / 2)
    r = sum_1 / sum_2
    return r


mas = []
f1 = open("Visa.txt", "r")
f2 = open("MasterCard.txt", "r")
a = int(input("Введите число файла, с которым необходимо работать (1 - Visa, 2 - MasterCard): "))
if a == 1:
    mas = read_f(f1, mas)
else:
    mas = read_f(f2, mas)
a = int(input("Ввеедите номер метода (1 - винзорирование, 2 - линеаризация, 3 - корреляция): "))
for i in range(len(mas)):
    mas[i] = int(mas[i] + 0.5)
if a == 1:
    print(*mas)
    vinz(mas)
    print(*mas)
elif a == 2:
    for j in range(int(len(mas) / 4)):
        mas[randint(0, len(mas) - 1)] = 0
    print(*mas)
    print(*lean(mas))
else:
    for i in range(int(len(mas) / 4)):
        mas[randint(0, len(mas) - 1)] = 0
    minimum = min(mas)
    maximum = max(mas)
    counted = num_cou(mas, maximum)
    temp_y = math_ex_y(mas)
    temp_x = math_ex_x(mas)
    print(corr(mas))