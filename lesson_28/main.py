from tkinter import *

def hell_o(event):
    message = ent.get()
    ent.delete(0, END)
    print(message)

root = Tk() # создание/инициализация
root.geometry("500x400")
root.title("Моё первое окошечко :з")
root["bg"] = "grey71"
lab = Label(root, text="Стендбуль") # надпись
lab.pack() # размещаем элемент(по порядку)

lab["bg"] = "gold4" # ключевое слово
lab["fg"] = "#D370C9" # hex код
#lab["font"] = 20  # 1: размер шрифта
#lab["font"] = "Arial 20 bold" # мультизначение строчкой
lab["font"] = ("Arial", "20", "bold", "italic", "underline") # мультизначение кортежем
lab["height"] = 3
lab["width"] = 15

btn = Button(root, text="Моя первая конопочка", bg="lightblue",font=500)
btn.pack()
btn.bind("<Button-1>", hell_o)
# Button-1 = ЛКМ
# Button-3 = ПКМ
# Double Button-3 = ПКМ

ent = Entry(root, width=20, font=20, bd=50)
ent.pack()

txt = Text(root, width=20, height=5, wrap="word")
txt.pack()







root.mainloop() # отрисовка окна
# НЕ ПИСАТЬ СЮДА
