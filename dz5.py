# gamelist = []                 Задача 1
# while True:
#     game = input('введите игру ')
#     if game != '0':
#         if game not in gamelist:
#             gamelist.append(game)
#             print(gamelist)
#         else:
#             print('эта игра уже записана')
#     else:
#         gamelist.sort()
#         print('ваш отсортированный список: ', gamelist)
#         break

# progress = [5, 3, 2, 4]               Задача 2
# s3 = progress.count(3)
# s4 = progress.count(4)
# s5 = progress.count(5)
# ss = len(progress)
# pr = (s3+s4+s5)/ss*100
# print(f'{pr}\n{progress}\n{ss}')

# pr = input()                          Задача 3
# progress = pr.split()
# p5 = progress.count('5')
# p = len(progress)
# x = ((100*p5)/p)
# print(x,'%')


# teach_info = []        Задача 4
# while True:
#
#     lastname = input("введите фамилию преподователя: ")
#     if lastname.lower() == '0':
#         break
#
#     job = input("введите должность преподователя: ")
#     students = input("введите кол-во студентов во всех группах (разделяя группы запятыми ','): ")
#
#     teacher_info = {
#         'фамилия: ': lastname,
#         'должность: ': job,
#         'количество студентов в группах: ': students
#
#     }
#     teach_info.append(teacher_info)
#
# print(f"информация о преподавателях: \n")
# for teacher in teach_info:
#     print(f'фамилия преподователя: {teacher["фамилия: "]}')
#     print(f'должность преподователя: {teacher["должность: "]}')
#     print(f'количество студентов в группах: {teacher["количество студентов в группах: "]} \n')


# num = input()           Задача 5
# str_list = num.split()
# num_list = []
# for i in str_list:
#      number = int(i)
#      num_list.append(number)
# if len(num_list) <= 1:
#      print('no')
#
# for n in range(1, len(num_list)):
#      if num_list[n] != num_list[n - 1] + 1:
#           print("no")
#           break
# else:
#      print('yes')




















