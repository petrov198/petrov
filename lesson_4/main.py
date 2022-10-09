#alphabet = "ФБВГДЕЕЖЗИКЛМНОПРСТ"
#
#print(alphabet[::-2])  # вывод в обратном порядке
# [start:end:step]
#pharse = "антон"
#






#familiya = input("Фамилия: ").capitalize()
#imya = input("Имя: ").capitalize()
#otchestvo = input("Отчество: ").capitalize()
#print(familiya)
#print(f"{familiya} {imya[0]}. {otchestvo[0]}.")

#x = input()
#print(x.lower().count('a'))  # кол-во маленьких "а"
#print(x.lower().count('a'))  # кол-во всех букв "a"

#x = input("введите фразу, разделяя слова запятыми: ")
#lst = x.split(",")
#print(x.split(","))  # split - разделить, рас

#phrase = input("введте фразу: ")
#find = input("что меняем: ")
#replace = input("на что меняем: ")
#
#print(phrase.replace(find, replace))


#phrase = input ("введите фразу: ")
#print(phrase.replace("ё", "е"))

##rus = ""
#for bukva in x:
#    rus = rus + alphabet[bukva]
#print(rus)

email = input("Введите почту:")
print(email.split("@"))
login = email.split("@")
domain = email.split("@")[-1]
print("Логин:", login)
print("Домэн:", domain)