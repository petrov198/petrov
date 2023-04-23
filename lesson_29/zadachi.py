from tkinter import *


# def hopka(event):
#     message = ent.get()
#     lab["text"] = message
# root = Tk()
# root.geometry("400x200")
# root["bg"] = "green"
#
# lab = Label(root, text="...")
# lab.pack()
#
# ent = Entry(root)
# ent.bind("<Button-3>", hopka)
# ent.insert(0, "впиши и ПКМ")
# ent.pack()
# def hel_lo():
#     user_choose = rb_val.get()
#     if user_choose == 1:
#         lab["text"] = "Hello " + rb1["text"]
#     else:
#         lab["text"] = "Hello " + rb2["text"]
# root = Tk()
# root.geometry("300x200")
# lab = Label(root, text="Hello")
# lab.pack()
#
# rb_val = IntVar()
#
# rb1 = Radiobutton(root,text="World", variable=rb_val, value=1, command=hel_lo)
# rb1.pack()
#
# rb2 = Radiobutton(root,text="Python", variable=rb_val, value=2, command=hel_lo)
# rb2.pack()
def action():
    if cb_val.get() == True:
        b["text"] = "Активна"
        b["state"] = "normal"
    else:
        b["text"] = "Не Активна"
        b["state"] = "disabled"
root = Tk()

cb_val = BooleanVar()
cb = Checkbutton(root, text="Активатор", variable=cb_val, onvalue=True, offvalue=False, command=action)

b = Button(root, text="Не активна", state="disabled")
cb.pack()
b.pack()
root.mainloop()