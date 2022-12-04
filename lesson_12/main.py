# мутабельность
# мутабельные - изменяемые
# немутабельные - неизменяемые
# x = "mavavi"
# x[1] = "o"   # так нельзя
# x = "movavi"
# списки []
# lst = ["один", "два", "попит"]
# lst.append("спинер")  # .append() - добавить
# lst.pop(0)  # .pop() - удалить по индексу
# lst.remove("two")  # .remove() - удалить по значению

# lst = [0, 3, 5, -2, 1]
# lst.reverse()
# print(lst)

# lst1 = [0, 1, 2]
# lst2 = [3, 4, 5]
# lst1.extend(lst2) # .extend() - расширить
# pirnt(lst1)
# lst = [1, 2] # [1, 2] -> [1, 1.5, 2]
# lst.insert(1, 1.5) # .insert() - вставить по индексу
#
# lst = ["не пустота"] # ["не пустота"] -> []
# lst.clear()  # .clear() - очистка
#
# lst = [0, 4, 2, -5, 1]
# lst.sort()  # .sort() - сортировка
# lst.sort(reverse=True)  # .reverse=True - от меньшего к большему
# print(lst)

# кортеж
# tup = (1, 2, 3)
# # tup = 1, 2, 3
# # tup = 1,
# print(max(tup))
# print(min(tup))
#
# list1 = ["A", "B", "C"]
# list2 = ["0", "1", "2"]
# couple = zip(list1, list2)  # zip - функция склеивания по индексу
# print(couple)
#
# for bogdan in couple:
#     print(bogdan)

from collections import namedtuple

citizen = namedtuple("житель", "имя возраст статус")
alex = citizen(имя="Лёха Алексеев", возраст="27", статус="предприниматель")

print(alex.имя)
print(alex.статус)
print(alex.возраст)

print(alex)