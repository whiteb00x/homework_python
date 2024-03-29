# 1. Создайте словарь, в котором ключами будут числа от 1 до 10,
# а значениями эти же числа, возведенные в куб

numbers = range(1, 11)
k = []
for i in numbers:
    k.append(i**3)
dictt  = dict(zip(numbers, k))
print(dictt)

# 2. Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
# а в качестве значения количество этих цифр в строке

s = input()
dictt = {}
for i in s:
    if i in dictt:
        dictt[i] += 1
    else:
        dictt [i] = 1
print (dictt)

# 3 Напишите программу принимающую ввод информации о треке(место в чарте, исполнитель, название)
# пока пользователь не введет "off".
# Программа должна вывести всю информацию в виде словаря вида:
# {(место, испонитель): название трека}

 m = {}
while True:
     place = input('место: ')
     if place == 'off':
         break
     singer = input('исполнитель: ')
     title = input('название: ')
     m[(place, singer)] = title
 print(m)


# 4 Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же
# (имел тот же адрес в памяти).


dictt = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
    "k5": "v5",
}
dictt ['k1'], dictt['k5'] = dictt['k5'], dictt['k1']
del dictt['k2']
dictt['new_key'] = 'new_value'
print(dictt)


# 5 Дан словарь email-адресов студентов, в качестве ключа используется домен,
# а в качестве значения список имен.
# Необходимо вывести все email-адреса в формате Имя@домен.

emails =  {"mail.ru": ["даша", "эрика", "артем"],
    "gmail.com": ["жаклин", "настя крутая"],
    "yandex.ru": ["сновдаша", "даша лучшая", "ааааа"]
           }

for domain, names in emails.items():
    for name in names:
        print(f'{name}@{domain}')


