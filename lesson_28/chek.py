# # задача 1
# from tkinter import *

# okno = Tk()
# okno.geometry("400x500")
# lab = Label(okno, text="голубой")
# lab.pack()
# ent = Entry(okno,width=20)
# ent.pack()
# btn1 = Button(okno,width=20, bg="red").pack()
# btn2 = Button(okno,width=20, bg="orange").pack()
# btn3 = Button(okno,width=20, bg="yellow").pack()
# btn4 = Button(okno,width=20, bg="green").pack()
# btn5 = Button(okno,width=20, bg="cyan").pack()
# btn6 = Button(okno,width=20, bg="blue").pack()
# btn7 = Button(okno,width=20, bg="purple").pack()
#
#








# okno.mainloop()

# from tkinter import *
#
# def gentelmen():
#     message = ent.get()
#     ent.delete(0, END)
#     message1 = txt.get(0.0, END)
#     txt.delete(0.0, END)
#     print(message, message1)
# root = Tk()
# root.geometry("300x300")
#
# lab = Label(root, text="ваш адрес:", bg="#CDCD66", bd="10")
# lab.pack()
#
# ent = Entry(root, width=10, bd="5", bg="gold")
# ent.pack()
#
# lab2 = Label(root, text="коментарий")
# lab2.pack()
#
# txt = Text(root, width=15, height=10)
# txt.pack()
#
# btn = Button(root, text="отправить", width=15, bg="lightblue", command=gentelmen)
# btn.pack()
#
#
#
#
#
#
#
#
#
#
# root.mainloop()

from tkinter import *
def bold(one):
    lab["font"] = lab['font'].replace(' italic', "")
    lab["font"] += " italic"
def italic(two):
    lab["font"] = lab['font'].replace(' bold', "")
    lab["font"] += " bold"
def base(three):
    lab['font'] = lab['font'].replace('bold', "").replace(' italic', "")

root = Tk()
lab = Label(root, text="хэллоу")
lab.pack()

lab["font"] = "Arial 15"

km = lab.bind("<Button-1>",bold )
pkm = lab.bind("<Button-3>", italic)
km2 = lab.bind("<Double Button-1>", base)












root.mainloop()