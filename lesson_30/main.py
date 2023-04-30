from tkinter import *
# from tkinter import messagebox

root = Tk()
root.geometry("500x500")
# -------- listbox --------
# lst = ["Первый", "Второй", "Пятнадцать"]
# lstbox = Listbox(root)
# lstbox.pack()
#
# # 1 способ: через цикл и вставку
# for elem in lst:
#     lstbox.insert(END, elem)

# 2 способ через переменную (StringVar)
# lst = ["Первый", "Второй", "Пятнадцать"]
# lst_tk = StringVar(value=lst)  # получаем кортеж
# print(lst_tk.get())
# lstbox = Listbox(root, listvariable=lst_tk, selectmode=EXTENDED)
# lstbox.pack()
#
# def fun(pelmeni):
#     for ind in lstbox.curselection(): # current = текущий
#         print((lst[ind]))
#
# lstbox.bind('<<ListboxSelect>>', fun)


# btn = Button(root, text="вывести", command=fun)
# btn.pack()
# -------- messagebox --------
# def info():
#     messagebox.showinfo("Я информационный", "Синий цвет")
# def error():
#     messagebox.showerror("Я ошибочный", "Красный цвет")
# def warning():
#     messagebox.showwarning("Я предупреждающий", "Желтый цвет")
#
#-------- .pack() --------
# btn = Button(root, text="Text")
# #btn.pack(anchor=SW, expand=True)
# btn.pack(fill=BOTH, expand=True)
# btn1 = Button(root, text="Text")
# btn1.pack(pady=50)
# btn2 = Button(root, text="Text")
# btn2.pack(pady=50)
# -------- .grid() --------
# btn1 = Button(root, text="Text1")
# btn1.grid(column=0, row=0)
# btn2 = Button(root, text="Text2")
# btn2.grid(column=1, row=0)
# btn3 = Button(root, text="Text3")
# btn3.grid(column=2, row=0, rowspan=2,sticky=NS)
# btn4 = Button(root, text="Text4")
# btn4.grid(column=0, row=1, columnspan=2, sticky=EW)
#-------- .place() --------
# btn1 = Button(root, text="text1")
# btn1.place(x=10, y=10)
#-------- .after(ms, func) --------
# from time import sleep
# def fun():
#     print("print")
#     root.after(1000, fun)
#
#
# root.after(3000, fun)
# -------- .bind() --------
# def fun(pelmeni):
#      print("print")
#
# btn1 = Button(root, text="text1")
# btn1.pack()
# #btn1.bind("<Enter>", fun)
# #btn1.bind("<MouseWheel>", fun)
# #btn1.bind("<FocusIn>", fun)
# btn1.focus_set()
# btn1.bind("<Return>", fun)
# -------- .set() --------
# rb_val = IntVar()
# print(rb_val.get())
# rb_val.set(5)
# print(rb_val.get())
# -------- .show --------
# Entry(root, show="*").pack()



root.mainloop()