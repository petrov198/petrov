from tkinter import *

win = Tk()
win.geometry("400x200")
win["bg"] = "pink"

#ондострочный
# lab = Label(win, text="Чтобы было")
# lab.pack()
# lab["bg"] = "lightblue"
# lab["fg"] = "gold4"

# надпись
# ent = Entry(win, width=10, bd=15, font="bold 20")
# ent.pack()

# многострочный
# txt = Text(win, width=20, height=3, wrap="word")
# txt.pack()

# кнопка
# def actino():
#     print("Принт")
# btn = Button(win, command=actino)
# btn["text"] = "Я кнопка"
# btn.pack()

# Checkbutton
# def get_cb():
#     print(cb_val.get())
#
# cb_val = BooleanVar()
# cb = Checkbutton(win, text="GGGGGG", command=get_cb,variable=cb_val,onvalue=True,offvalue=False)
# cb.pack()
# cb.select() # ставит галочку по умолчанию
# cb.deselect() # убирает галочку по умолчанию
# Radiobutton
# def get_rb():
#     print(rb_val.get())
# rb_val = IntVar()
# rb1 = Radiobutton(win,text="Текст по просьбе Арсения",
#                   variable=rb_val,
#                   value=421,
#                   command=get_rb)
# rb1.pack()
# rb2 = Radiobutton(win,text="Текст по просьбе Арсения",
#                   variable=rb_val,
#                   value=23,
#                   command=get_rb)
# rb2.pack()
# scale
# def get_scala(val):
#     print(scala.get())
# scala = Scale(win,
#               from_=50,
#               to=120,
#               orient=HORIZONTAL,
#               length=300,
#               tickinterval=10,
#               resolution=10,
#               command=get_scala)
# scala.pack()
# PhotoImage
# img = PhotoImage(file="free-png.ru-90.png")
# img_small = img.subsample(3, 3)
# img_big = img.zoom(3, 3)
# img_poltora = img.subsample(3, 3).zoom(2, 2)
# lab = Label(win, image=img_poltora)
# lab.pack()
# отступы
# Label(win, text="кис-кис", bg="gold").pack()
# Label(win, text="чик-чик", bg="lightblue").pack(pady=15, ipady=20)







win.mainloop()