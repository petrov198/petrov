# def hello(x):   # обьявили функцию + ждём аргумент x
#     return "hello" + x  # возвращаемое значение
#
# print(hello("Антон"))  # вызов функции
#
#
# l = lambda x, b: "hello" + b + x
# print(l("Антон", "Гермес"))  # вызов лямбда функции
#
# # генератор списка(list comprehension)
# l = [i for i in range(1, 6)]
# print(l)
import random
количество = int(input("напишите сколько костей бросам:"))
slovar = {}
for i in range(количество, количество * 6 + 1):
    slovar[i] = 0

print(slovar)