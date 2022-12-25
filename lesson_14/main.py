# Множества
# 1) повторениия исключены
#d1 = {"Антон", "Антон", "Ы"}
# 2) неупорядоченные
#print(d1)
# 3) пустое множество - только set()
# 4) внутри только неизменяемые данные
# пустота
# пустота
# словари
# 1) изменяемый тип данных
# 2) В качестве ключа дпускается любое значение
# x = ("что-то")
# d = {
#     1: 1,
# }
# print(d)
# 3) пустой словарь = dict() или {}
# первый задача
# phrase = "Маша, ты Где? мАШа загОРает.".lower()  # опустили регистр
# print(phrase)
# spisok_nechist = list("!,.?")  # строка -> влада а4 (список)
# phrase_cleared = "" # будущая очищенная фраза
# d = {}
# for tadjikistan in phrase:  # посимвольный перебор
#     if tadjikistan not in spisok_nechist: # если это нормальный символ
#         phrase_cleared += tadjikistan  # добавить символы
# print(phrase_cleared)
# l = phrase_cleared.split(" ")
# print(l)
# for bogdan in l:
#     if bogdan not in d:  # если такого слова ещё не было
#         d[bogdan] = 1  # первое вхождение
#     else:  # если слово уже встречалось
#         d[bogdan] += 1 # прибавляем повторение
# print(d)
#
#
#
#
#
#
# задача второй
# s = 0  # будущая сумма
# d ={"хлеб": 1000, "молоко": 1.5, "Александр": 47, "ёлка": 50}
# for price in d.values():  # перебор по значениям
#     s += price # считаем чек перекус таксиста
# print(s)
# третий задача
# phrase = "Маша, ты Где? мАШа загОРает.".lower()  # опустили регистр
# print(phrase)
# spisok_nechist = list("!,.?")  # строка -> влада а4 (список)
# phrase_cleared = "" # будущая очищенная фраза
# d = {}
# for tadjikistan in phrase:  # посимвольный перебор
#     if tadjikistan not in spisok_nechist: # если это нормальный символ
#         phrase_cleared += tadjikistan  # добавить символы
# print(phrase_cleared)
# l = phrase_cleared.split(" ")
# print(l)
# for bogdan in l:
#     if bogdan not in d:  # если такого слова ещё не было
#         d[bogdan] = 1  # первое вхождение
#     else:  # если слово уже встречалось
#         d[bogdan] += 1 # прибавляем повторение
# print(d)
#
# maxi = max(d.values())   # находим максимальное значение
# for (key, values) in d.items():
#     if values ==maxi:
#         print(f"ключ: {key}, значение:{values}")
#     print(values)
# задача четвёртый

d = {
    3:1,
    9:2,
    1:6,
    "ключ1":2,
    "eee":3,
}
d["eee"], d[3] = d[3], d["eee"]

del d[9]


d["new_key"] = "new_values"
print(d)







