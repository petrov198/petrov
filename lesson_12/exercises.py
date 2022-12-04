# x = input("ввод: ")
# lst = x.split(" ")
# print(lst)
# lst.reverse()
# print(lst)

# number = ""
# chet = 0
# nechet = 0
# lst = []
#
# while number != "end":
#     number = input("число: ")
#     if number.lstrip("-").isdigit():
#         # .lstrip("-") - удалить "-" слева
#         number = int(number)
#         lst.append(number)
#     elif number == "end":
#         break # выход из цикла
#     else:
#         print("число, пожалуйста!")
#         continue #перезапускает цикл
#
#     if number % 2 == 0:
#         chet += 1
#     else:
#         number += 1
#
# print(lst)
# print(f"четные: {chet}шт.")
# print(f"нечетные: {nechet}шт.")

lst = [-5, -8, 2, 14, 1]
mini = min(lst)
maxi = max(lst)

lst[lst.index(mini)]
lst[lst.index(maxi)]
# lst.index(mini) - индекс значения
# lst[] - само значение


lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)], lst[lst.index(mini)]
print(lst)