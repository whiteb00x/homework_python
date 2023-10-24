# s = 3                                                              Задача 1
# for i in range(s):
#     m = input('введите музыкальное предпочтение: ')
#     print('предпочтение учтено')
# print('система рекомендаций настроена')

# while True:
#     n = input("введите 'game' для игры в 'угадай число' или 'off' для выхода: ")          Задача 2
#     if n == 'game':
#         answer = 5
#         tr = 3
#         while tr > 0:
#             otvet = int(input("угадайте число от 1 до 10: "))
#             if otvet == answer:
#                 print("вы выиграли билет на концерт")
#                 break
#             else:
#                 tr -= 1
#                 print("неверный ответ. осталось попыток:", tr)
#         if tr == 0:
#             print("у вас закончились попытки")
#     elif n == "off":
#         print("программа завершена.")
#         break
#     else:
#         print("читать умеешь?")

# st = "=?*^$№@_"                                       Задача 3
# login = input("введите логин: ")
# zapret = []
# for s in login:
#     if s in st:
#         zapret.append(s)
# if zapret:
#     print("запрещенные символы, использованные в логине: ", ", ".join(zapret))


# while True:                                           Задача 4
#     n = input('ваш отзыв ')
#     if n != 'off':
#         print('спасибо ваш отзыв принят!!!!!!!!!!')
#     else:
#         print('система предпочтений настроена')
#         break

# while True:                                       Задача 5
#     n = int(input('введите стоимость '))
#     s = 15  # скидка
#     if n != 0:
#         nws = n/100*s
#         print(n - nws)
#     else:
#         break

# n = int(input('введите стоимость покупок '))       Задача 6
# while n!=0:
#     if n%2 == 0:
#         n = n/2
#         print(n)
#     else:
#         break
# print('к оплате: ', n)









