import random
# class Person:
#     def __init__(self, imya, vozrast):  # магический метод (инициализации)
#         self.name = imya
#         self.age = vozrast
#     def __str__(self):
#          return f"Я {self.name} и мне {self.age} лет"
#
#
# chelovek = Person("Данис", 29)  # создание объекта класса Person
# chelovek1 = Person("Денил", 4)  # создание объекта класса Person
#
# print(chelovek.name)
# print(chelovek1.name)
# # print(chelovek)
#
# print(str(chelovek))
#задача 1
# class Person:
#     def __init__(self, imya, familia, vozrast):
#         self.name = imya
#         self.femilia = familia
#         self.age = vozrast
#     def __str__(self):
#         return f"возраст: {self.age}\nфамилия:{self.femilia}\nимя: {self.name}\n"
#     def greet(self):
#         return f"привет, меня зовут{self.name}, мне{self.age} лет."
#
# chelovek = Person("вилина", "огузкова", 100)
# # chelovek1 = Person("elina", "pan", 76)
#
# print(chelovek.greet())
#задача 2
# list = []
# for i in range(random.randint(5,10)):
#     list.append(random.randint(2, 5))

# nums = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
# print(nums)

class Person:
    def __init__(self, imya, familia, vozrast):
         self.name = imya
         self.femilia = familia
         self.age = vozrast
         self.grades = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
         self.srbal = sum(self.grades)/len(self.grades)
    def __str__(self):
         return f"возраст: {self.age}\nфамилия:{self.femilia}\nимя: {self.name}\n"
    def greet(self):
         return f"привет, меня зовут{self.name}, мне{self.age} лет."

chelovek = Person("Володя", "огузков", 100)
chelovek1 = Person("павел", "кошмаров", 13)
print(chelovek.grades, chelovek.srbal)


