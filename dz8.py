# 1 Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
# но только в том случае если они не равны None.

def test (a=None, b=None, c=None):
    if a:
        print('1st:', a)
    if b:
        print('2nd:', b)
    if c:
        print('3rd:', c)

test(input(), input(), input())

# 2 Напишите функцию, принимающую в качестве единственного параметра
# расстояние поездки в километрах и возвращающую итоговую сумму опла-
# ты такси

def taxi(s):
    n = s * 1000 // 140
    print('итог:', 4.00 + 0.25 * n)

taxi(float(input('расстояние поездки: ')))

# 3 Напишите программу, которая будет складывать числа, введенные поль-
# зователем.

def s(n):
    summ = 0.0
    if n == '':
        return summ
    else:
        summ += int(n)
        return summ + s(input())

print(s(input()))

# 4 Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.
def cacluate(*args):
    avg = sum(args)/len(args)
    arr = []
    for i in args:
        if i > avg:
            arr.append(i)
    return avg, arr
print(cacluate(14,2,32,40,5,17,))