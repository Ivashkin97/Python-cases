#1 окно
"""
from tkinter import *

win = Tk()
win.title("Графическая программа на Python")
win.geometry("400x300")

win.mainloop()
"""

#2 два окна
"""
from tkinter import *
win1 = Tk()
win1.title("Окно 1")
win1.geometry("400x300")

win2 = Tk()
win2.title("Окно 2")
win2.geometry("500x300")

win1.mainloop()
win2.mainloop()
"""

#3 виджет "кнопка"
"""
from tkinter import *

win = Tk()
win.title("Кнопка")
win.geometry("400x400")

#параметры виджета задаются при его создании
button1 = Button(win, text="OK", bg="green")

#параметры виджета создаются в процессе работы программы

button1["fg"] = "yellow"
button1["text"] = "Пока"

#button1.config(height=20)
#button1.configure(pady=40)
button1.config(padx=20)
button1.pack()
win.mainloop()

"""
#4 две кнопки

"""

from tkinter import *

win = Tk()
win.title("Две кнопки")
win.geometry("400x400")

btn1 = Button(win, text="Кнопка1")
btn2 = Button(win, text="Кнопка2")

btn2.pack()
btn1.pack()
"""

#5 событие, привязанное к кнопке

from tkinter import *

def click_button():
    btn.config(bg="red")
    label1["text"] = "Пока"

win = Tk()
win.title("Событие")
win.geometry("400x400")

btn = Button(text="OK", command=click_button)
btn.pack()

label1 = Label(text="Привет")
label1.pack()

win.mainloop()