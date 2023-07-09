"""
#1 флажки
from tkinter import *

win = Tk()
win.title("Флажки")

sale1 = BooleanVar()
c1 = Checkbutton(text="Скидка - 100 рублей", variable=sale1)

c1.pack()

sale2 = BooleanVar()
c2 = Checkbutton(text="Скидка - 200 рублей", variable=sale2)

c2.pack()

sale3 = BooleanVar()
c3 = Checkbutton(text="Скидка - 500 рублей", variable=sale3)

c3.pack()

l1 = Label(textvariable=sale1)
l1.pack()

l2 = Label(textvariable=sale2)
l2.pack()

l3 = Label(textvariable=sale3)
l3.pack()

win.mainloop()
"""

#2 переключатели
"""
from tkinter import *

win = Tk()
win.title("Переключатели")

language = IntVar()

r1 = Radiobutton(text="С++", variable=language, value=1, state=DISABLED)
r1.pack()

r2 = Radiobutton(text="Python", variable=language, value=2)
r2.pack()
r2.select()

r3 = Radiobutton(text="Java", variable=language, value=3)
r3.pack()

Label(textvariable=language).pack()

win.mainloop()
"""
#3 переключатели и выравнивание
"""
from tkinter import *

win = Tk()
win.title("Переключатели")

language = IntVar()

r1 = Radiobutton(text="С++", variable=language, value=1, state=DISABLED)
r1.pack(side=LEFT)

r2 = Radiobutton(text="Python", variable=language, value=2)
r2.pack(side=RIGHT)
r2.select()

r3 = Radiobutton(text="Java", variable=language, value=3)
r3.pack(side=TOP)

r4 = Radiobutton(text="C#", variable=language, value=4)
r4.pack(side=BOTTOM)

win.mainloop()
"""

#4 поле ввода и новый распаковщик

from tkinter import *

win = Tk()
win.title("Grid")

label1 = Label(text="Пароль")
label1.grid(row=0, column=0, sticky=E) #N, S, E, W

label2 = Label(text="Логин")
label2.grid(row=1, column=0, sticky=E)

entry1 = Entry(width=7)
entry1.grid(row=0, column=1)

c1 = Checkbutton(text="Сохранить?")
c1.grid(row=2, columnspan=2)

entry2 = Entry(width=7)
entry2.grid(row=1, column=1)

win.mainloop()