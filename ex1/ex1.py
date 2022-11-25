import func


def check(m):
    for i in range(len(m)):
        k = 0
        checker = i
        while m[checker] == m[i] and checker >= 0:
            k += 1
            checker -= 1
        if m[i] == 0:
            for f in range(k):
                zeroes[f] += 1
        else:
            for f in range(k):
                ones[f] += 1


n = int(input("Введите размер массива: "))
mas = func.cr_arr(n)
print(*mas)
zeroes = [0 for i in range(mas.count(0))]
ones = [0 for k in range(mas.count(1))]
print("Процентное соотношение нулей и единиц: ", mas.count(0)*100/n, "%:", mas.count(1)*100/n, "%.")
check(mas)
print(*zeroes)
print(*ones)
print("\nНули:")
for j in range(len(zeroes)):
    if zeroes[j] != 0:
        print('0' * (j+1), " --- ", zeroes[j], "раз", " --- ", zeroes[j]*(j+1)*100/len(mas), '%')
print("\n\n\nЕдиницы:")
for j in range(len(ones)):
    if ones[j] != 0:
        print('1' * (j+1), " --- ", ones[j], "раз", " --- ", ones[j]*(j+1)*100/len(mas), '%')
