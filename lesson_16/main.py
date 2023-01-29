# primer1 = lambda a, b: a + b + 1  # лямбда функцию поместили в переменную
#
# print(primer1(5, 10))  # вызов функции не отличается
#
# answer = "Д"
# exit_triger = lambda yn: True if yn == "Д" else False
# print(exit_triger(answer))

# генератор списка (list comphrension)
# lst = []
# for i in range(1, 6):
#     lst.append()
# print(lst)
#
# lst2 = [i for i in range(1, 6)]
# # 1. всегда в []
# # 2. for i in ... -> сколько элементов в списке
# # 3. всё что перед for -> сам элемент списка
#
# # задача 1
# c2f = lambda c: 9/5 * c + 32
# f2c = lambda f: (F - 32)* 5/9
# c2k = lambda c: 273.15 + c
# k2c = lambda k: k - 273.15
# f2k = lambda F: c2k(f2c(f))
# degree = 203
# print(f2k(degree))  # обращение к лямбда функции

# задача 2
# import random
# exit_vihot = lambda yn: True if yn == "Д" else False
# while True: # бусконечный цикл
#     kolvokub = int (input("сколько бросаем?"))
#     dices = [random.randint(1, 6) for i in range(kolvokub)]
#     print(dices)
#     igrok = input("хочешь ли ты выйти? да - Д | нет - н")
#     print(exit_vihot(igrok))
#     if exit_vihot(igrok) == True:
#         break
# задача 3
# from  random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
#
# lst = []
# for i in range(6):
#     lst.append( choice(choice(chars))) # случайный элемнет в список добавили
# code = "".join(lst)
# silka = "httрs://www.google.com" "MOVAVI"
# d = {}
# #d = {"httрs://www.google.com": "MOVAVI"  "mart"}
# if silka in d:
#     print("эта ссылка уже есть в базе вот её код ->", d[silka])
# else:
#     d[silka] = code
#     print("ссылка добавлена вот её код ->", d[silka])

# задача 4
# import math
# a = 10
# b = 5
# y1 = lambda a, b : b - a
# print(y1(a, b))
#
# y2 = lambda a, b : b + a
#
# y3 = lambda a, b : b * a
#
# y4 = lambda a, b : b / a
#
# y5 = lambda a,b: a / b
#
# mod = lambda print(logarifm(b, a))x : -x if x<0 else x
# print(mod(-5))
#
# logarifm = lambda a, b : math.log(b, a)
