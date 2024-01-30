
# 1 Напишите программу печатающую бейджики учеников.

def printb():
    print('-' * 20)
    print('"Колледж Сириус"', '\nимя:', '_' * 4, '\nгроуп:', '_' * 4)

count = int(input('количество учеников: '))
for i in range(count):
    printb()

print('-' * 20, '\nГотово! Заберите бейджики.')


# 2 Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.

def discount(point):
    if point <= 49:
        return "10%"
    elif point <= 99:
        return "15%"
    elif point >= 100:
        return "20%"

print(discount(101))



# 3 Напишите программу определяющую допуск ученика к зачету.

students = int(input("количество студентов: "))
def isAccepted(points):
    if points > 50:
        return True
    else:
        return False
for i in range(students):
    print(isAccepted(int(input("балл: "))))



# 4 Напишите программу считающую и обрабатывающую индекс массы тела.

def IMT(weight, height):
    index = weight / ((height ** 2) / 10000)
    return index

def result(weight, height):
    imt = IMT(weight, height)
    if imt < 18.5:
        return "недостаточный вес"
    elif 18.5 < imt < 25:
        return "ИМТ в норме"
    elif imt > 25:
        return "избыточный вес"

print(result(int(input("Вес: ")), int(input("Рост: "))))


# 5 Каждый стажёр мог выбрать любое число предметов для изучения.
# По каждому предмету он мог набрать от 0 до 50 баллов.

# Программа должна:
# Пока пользователь не введет "стоп"":
# 1. Запрашивать имя студента и число предметов.
# 2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
# 3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
# - баллов больше 80 — «Наградить дипломом.»;
# - баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
# - остальные случаи — «Выдать грамоту об участии.».
# """

def s():
    sum = 0
    while True:
        name = input("имя студента: ")
        subjects = int(input("кол-во предметов: "))
        if name.lower() == 'стоп':
            break
        for i in range(subjects):
            point = int(input("Введите баллы: "))
            sum += point
        print(f'итог: {sum}')
        if sum >= 80:
            return 'наградить дипломом.'
        elif sum >= 50 and sum < 80:
            return 'наградить похвальной грамотой.'
        else:
            return 'выдать грамоту об участии.'

result = s()
print(result)
