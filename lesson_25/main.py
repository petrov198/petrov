from classi import Anton, House
import easygui

imya = easygui.enterbox(msg="Как твоё имя?"))
age = easygui.integerbox(msg="Сколько лет?")

helovek = Anton(imya, age)
dom1 = House()
dom15 = House()

print(chelovek.buy_house(dom1))
print(chelovek.buy_house(dom1))