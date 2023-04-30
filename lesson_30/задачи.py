from tkinter import *
from random import *

root = Tk()
root.geometry("500x500")

# lab1 = Label(root, text="Логин:")
# lab1.grid(column=0, row=0)
# lab2 = Label(root, text="Пароль:")
# lab2.grid(column=0, row=1)
#
# Ent1 = Entry(root)
# Ent1.grid(column=1, row=0)
# Ent2 = Entry(root, show="*")
# Ent2.grid(column=1, row=1)
#
# btn = Button(root, text="Авторизация")
# btn.grid(column=1, row=2, sticky=E)

def fun(pelmeni):
    btn.place(x=randint(0,450), y=randint(0,470))


btn = Button(root, text="Поймай Меня!", bg="red")
btn.place(x=10, y=10)
btn.bind("<Enter>", fun)


root.mainloop()
