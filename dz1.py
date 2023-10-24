# a = sum(range(16,25))           #Задача 1
# print(a)

# a, b = int(input()), int(input())            Задача 2
# print(a+b)

# a = int(input())            Задача 3
# print(255-a)

# a, b, c = int(input()), int(input()), int(input())      Задача 4
# print(a + b + c)
# print(max(a,b,c))
# print(min(a, b, c))


# a, b = int(input()), int(input())      Задача 5
# print(abs(a-b))

# rub = float(input())               Задача 6
# doll = float(input())
# euro = ((1/rub)/doll)
# print(round(euro, 2))

# many = int(input()) #1572               Задача 7
# tovar = int(input())
# print(many//tovar)

# abc = int(input())         Задача 8
# a = abc%10
# b = abc//10%10
# c = abc//100
# print(a + b + c )

# abc = int(input())       Задача 9
# a = abc%10
# b = abc//10%10
# c = abc//100
# print(a,b,c, sep = '')


# y = int(input())          Задача 10
# print(round(y/3600/24//365 + 1970)
#
# m, h = int(input()), int(input())         #Задача 11
# h = (h/100)**2
# print(round(m/h, 2))



w = float(input('ширина '))
h = float(input('длина '))
e = int(input('расход '))
v = int(input('объем '))
p = int(input('процент запаса '))
s = round((w * h), 2)
l = (s / e)
lwr = l*(1+p/100)
c = int((lwr//v) +1)
n = (c*v) - lwr
print(s)
print(round(lwr, 2))
print(c)
print(round(n, 2))