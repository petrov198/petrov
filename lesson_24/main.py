# class Human:
#     def __init__(self): # инициализация (мегический метод)
#         self.height = 993 # public данные
#         self.__money = 0.3 # private данные
#         def zdarova(self): # обычный метод
#             return "усиленно приветствую"
#         def ipotek(self):
#             if self.__money > 50 and self.__normal_height():  # юзаем private (внутри класса)
#                 return True
#             else:
#                 return "Попрошу у мамы или у людей на Маркса"
#         def __normal_height(self): # private метод
#             if 100 < self.height < 200:
#                 return True
#
#
# chelovek = Human()
# # print(chelovek.height)  # вызов атрибута
# # print(chelovek.zdarova())  # вызов метод
#
# print(chelovek.height) # public можно выводить
# chelovek.height += 7  # public можно менять
#
# #print(chelovek.__money) # private нельзя выводить
# # chelovek.__money = 5  # private(public) можно менять??
# # chelovek.__money = chelovek.__money + 5  # private НЕ можно менять
# # print(chelovek.__money)
#
# chelovek._Human__money += 5  # всё-таки можно менять(но осторожно)
# class Car:
#     def __init__(self):
#         self.status = False
#     def zavesti(self):
#         if not self.status:
#             return "машина завелась"
#      else:
#          return"так она и так"
#     def zagloxla(self):
#         return "машина заглохла"
#     def dalee(self,year):
#         self.dalee = year
#     def cled(self,type):
#         self.cled = type
#     def sda(self,color):
#         self.sda = color
#
# nissan = Car()
# print(nissan.zavesti())
# print(nissan.zagloxla())
#
# nissan.sda("чёрный(синий)")
# nissan.dalee(1900)
#
# print(nissan.sda)
# print(nissan.dalee)
# 2 задача
# import string
# class Alphabet:
#     def __init__(self,):
#         self.__lang = "eng"
#         self.__letters = string.ascii_lowercase
#
#     def print(self):
#         return self.__letters
#     def letters_num(self):
#         return len(self.__letters)
#
# a = Alphabet()
# print(a.print())
# print(a.__letters.num())
# задача 3
import datetime
class Overwatch:
    def __init__(self):
        self.__h, self.__m, self.__s = datetime.datetime.now().strftime("%H:%M:%S").split(":")
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
    def chas(self):
        self.__h += 1

    def vevod(self):
        return F"{str(self.__h).rjust(2,'0')}:{str(self.__m).rjust(2,'0')}:{str(self.__s).rjust(2,'0')}"
    def minuta(self):
        self.__m += 1
    def sekunda(self):
        self.__s += 1
tome = Overwatch()
tome.chas()
print(tome.vevod())




