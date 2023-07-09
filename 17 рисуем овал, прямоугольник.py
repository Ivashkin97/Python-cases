#1 

from tkinter import *
from tkinter.messagebox import *

def fun1():
    win2.title("Прямоугольник")

def fun2():
    win2.title("Овал")

def draw():
    canvas.delete("all")

    x1 = entry1.get()
    y1 = entry3.get()

    x2 = entry2.get()
    y2 = entry4.get()

    try:
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        if (x1 <= 0) or (x1 > 400) or (y1 <= 0) or (y1 > 400) or\
            (x2 <= 0) or (x2 > 400) or (y2 <=0) or (y2 >400):
            showwarning("Внимание!", "Координаты вышли за границу диапазона!")
        else:
            if r.get() == 1:
                canvas.create_rectangle(x1, y1, x2, y2)
            else:
                canvas.create_oval(x1, y1, x2, y2)
    except ValueError:
        showwarning("Внимание!", "Не все символы являются числами!")

win = Tk()
win.geometry("110x190+200+200")

label1 = Label(text="x1")
label2 = Label(text="x2")
label3 = Label(text="y1")
label4 = Label(text="y2")

entry1 = Entry(width=5)
entry2 = Entry(width=5)
entry3 = Entry(width=5)
entry4 = Entry(width=5)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=0, column=2)
label4.grid(row=1, column=2)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=0, column=3)
entry4.grid(row=1, column=3)

r = IntVar()

radio1 = Radiobutton(text="Прямоугольник", variable=r, value=1, command=fun1)
radio1.select()
radio2 = Radiobutton(text="Овал", variable=r, value=2, command=fun2)

radio1.grid(row=2, columnspan=4, sticky=W)
radio2.grid(row=3, columnspan=4, sticky=W)

btn1 = Button(text="Нарисовать", command=draw)
btn1.grid(row=4, columnspan=4)

win2 = Tk()
win2.title("Прямоугольник")
win2.geometry("500x200+400+100")

canvas = Canvas(win2, width=400, height=400)
canvas.pack()

win.mainloop()
win2.mainloop()


#2 меню
"""
from tkinter import *
win = Tk()

main_menu = Menu(win) #создается объект меню
win.config(menu=main_menu) #окно конфигурируется с указанием меню

first_menu = Menu(main_menu)
main_menu.add_cascade(label="Первое", menu=first_menu) #отображается в главном меню

first_menu.add_command(label="новое окно")
first_menu.add_command(label="Выход")

second_menu = Menu(main_menu)
main_menu.add_cascade(label="Второе", menu=second_menu)

second_menu.add_command(label="+")
second_menu.add_command(label="-")
second_menu.add_command(label="/")
second_menu.add_command(label="*")

win.mainloop()
"""


#3 
"""
from tkinter import *

def new_window():
    win2=Tk()
    Label1 = Label(win2, text="Ура! Меня создали!").pack()
    Label1.pack()

def exit_app():
    win.destroy()

win = Tk()

main_menu = Menu(win) #создается объект меню
win.config(menu=main_menu) #окно конфигурируется с указанием меню

first_menu = Menu(main_menu)
main_menu.add_cascade(label="Первое", menu=first_menu) #отображается в главном меню

first_menu.add_command(label="новое окно", command=new_window)
first_menu.add_command(label="Выход", command=exit_app)

second_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Второе", menu=second_menu)

second_menu.add_command(label="+")
second_menu.add_separator()
second_menu.add_command(label="-")
second_menu.add_separator()
second_menu.add_command(label="/")
second_menu.add_separator()
second_menu.add_command(label="*")
second_menu.add_separator()

win.mainloop()
"""

"""
#Диалоговое окно
from tkinter import *
from tkinter.messagebox import *

def fun():
#   answer = askquestion("Вопрос1", "Вы перестали есть плюшки по ночам?")
#   answer = askyesno("Вопрос2", "Вы перестали есть плюшки по ночам?")
#   answer = askokcancel("Вопрос3", "Повторить булочки?")
    answer = askretrycancel("Вопрос4", "Повторить булочки?")

    label1.config(text=answer)

win = Tk()

btn = Button(text="Я просто кнопка", font=("Ubuntu", 20), command=fun)
btn.grid(row=0, column=0)

label1 = Label(font=("Ubuntu, 20"), width=12)
label1.grid(row=0, column=1)

win.mainloop()
"""