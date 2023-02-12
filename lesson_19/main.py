alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_ru2 = alphabet_ru[::-1]
alphabet2 = alphabet[::-1]
phrase = input("введи сообщение на английсском, а я зашифрую на шифр атбаша")
abdul = ''
for i in phrase:
    if i.upper() in alphabet_ru:
        if i.isupper():
            a = alphabet_ru.index(i)
            brah = alphabet_ru2[a]
            abdul = abdul + brah
        else:
            a = alphabet_ru.index(i.upper())
            brah = alphabet_ru2[a].lower()
        abdul = abdul + brah
    elif i not in alphabet:
        abdul += i
    elif i.upper() in alphabet:
        a = alphabet.index(i)
        brah = alphabet2[a]
        abdul = abdul + brah
print(abdul)

