# def obama():   # объявление функции
#     print("hello_world")
#
# hello_world()  # вызов функции

# def plus(number1, chislo2):
#     result = number1 + chislo2
#     return result # то что вернёт функция
#
# x = plus(5, 3)   # вызов функции с аргументом. результат записан в переменную
# plus(chislo2=3, number1=23)  # указывание конкретных аргументов

# def is_anton(name):
#     if name == "Антон":
#         return True
#
# if is_anton("Богдан")    # если функция вернёт True
#     print("это Антон")
# else:
#     print("это не антон")
# list = input()
# def check(list):
#     sort = sorted(list) # сортироовка списка
#     if list == sort: # если list отсортирован
#         return True
#
# list = [1, 3, 5, 7, 9]
# if check(list) == True:
#     print("список отсортирован ро возрастанию")
# else:
#     print("список не отсортирован")
# задача 2
# def find_longest(list):
#     spos = []
#     for i in list:
#         spos2.append(len(i))
#    maxy = max(spos2)
#    ind = spos2.index(maxy)
# spos = ["Бараны", "Дом", "Дед", "Диван", "Танго"]
#    return list[ind],spos2[ind]
#
# print(find_longest(spos))

# def min_max(chisla):
#     mini = chisla[0]
#     maxi = chisla[0]
#     for i in chisla:
#         if i > maxi:
#             maxi = i
#         elif i < mini:
#             mini = i
#     return maxi,mini
# chisla = [1.2,2,3,4.5,8]
# print(min_max(chisla))
# 5 задача
# def is_prime(vnutr):
#     for i in range(2,vnutr+1):
#         if i == vnutr:
#             return True
#         if vnutr % i == 0:
#             break
#
#
# if is_prime(528):
#     print("da")
# else:
#     print("net")
# def join(spisock:list, razdelitel:str)->str:
#     resick = ""
#     for i in spisock:
#         resick += i +razdelitel
#     return resick
#
# listick = ["da", "net", "omlet"]
# print(join(listick, ">"))
def factorial(chislo):
    x = 1
    for i in range(2,chislo+1):
        x *= i # произвеление всех i
    return x

print(factorial(15))



