# f = open("8 класс сегодня дежурный.txt", "w", encoding="utf-8")  # создаст если нет, презапищет если есть
# f.write("Hellow orld\n")
# f.write("я славянин")
# f.close()

# f = open("8 класс сегодня дежурный.txt", "r", encoding="utf-8")
# # считываем содержимое файла и помещаем в content
# #content = f.read() # либо так
# content = f.readlines() #либо так
# print(content)
# for i in content:
#     print(i.rstrip())
# f.close()

# a = input("название файла:")
# f = open(a + ".txt", "w", encoding="uft-8")
# g = input("содержимое:")
# while g != "":
# f.write(g)
# f.close()

# задача 2
# a = input("Введите имя файла: ")
# f = open(a, 'r')
# content = f.readlines()
# v = len(content)
# for i in range(v):
#     print(f"{i})",content[i].rstrip())
#
# задача 3
f = open("zxc.txt", "r", encoding="utf-8")
text = f.readlines()
f.close()
print(text)
count = 0
while text != []:
    elements = text[:3]
    for i in elements:
        count += 1
        f = open(count + ".txt", "r", encoding="utf-8")
        print(i)
        f.write(i)
    del text[:3]