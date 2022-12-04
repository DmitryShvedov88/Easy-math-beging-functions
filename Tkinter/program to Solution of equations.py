import math
from tkinter import *

def clicked1():# второй экран когда выбрали линейное уравнение

    txt.grid_remove()

    btn1.grid_remove()
    btn2.grid_remove()
    btn3.grid_remove()

    res = "Привет, {}".format(txt.get())

    lbl1.configure(text=res)
    lbl2.configure(text="Решаем линейное уравнение a*x+b=0, запишите коэффициенты")
    lbl2.grid(column=1, row=2)
    lbl3.configure(text="Коэффициент a")
    lbl3.grid(column=0, row=3)
    lbl4.configure(text="Коэффициент b")
    lbl4.grid(column=0, row=4)

    txt1.grid(column=1, row=3)
    txt2.grid(column=1, row=4)

    btn4.configure(text="Решить уравнение", command=clicked11)
    btn4.grid(column=1, row=5)

def clicked11():

    lbl1.grid_remove()
    lbl3.grid_remove()
    lbl4.grid_remove()
    btn4.grid_remove()

    values.append(float(format(txt1.get())))
    values.append(float(format(txt2.get())))

    alphabet = dict(zip(keys, values))

    txt1.grid_remove()
    txt2.grid_remove()

    if (alphabet["A"] == 0 and alphabet["B"] == 0):
        lbl2.configure(text="Бесконечное количество решений.")
        lbl2.grid(column=1, row=5)
    if (alphabet["A"] == 0 and alphabet["B"] != 0):
        lbl2.configure(text="Решений нет.")
        lbl2.grid(column=1, row=5)
    if (alphabet["A"] != 0):
        f = alphabet["B"] / alphabet["A"]
        lbl2.configure(text="Ответ: x={}".format(f))
        lbl2.grid(column=1, row=5)

def clicked2():# второй экран когда выбрали квадратное уравнение
    txt.grid_remove()

    btn1.grid_remove()
    btn2.grid_remove()
    btn3.grid_remove()

    res = "Привет, {}".format(txt.get())

    lbl1.configure(text=res)
    lbl2.configure(text="Решаем квадратное уравнение a*x**2+b*x+c=0, запишите коэффициенты")
    lbl2.grid(column=1, row=2)
    lbl3.configure(text="Коэффициент a")
    lbl3.grid(column=0, row=3)
    lbl4.configure(text="Коэффициент b")
    lbl4.grid(column=0, row=4)
    lbl5.configure(text="Коэффициент c")
    lbl5.grid(column=0, row=5)

    txt1.grid(column=1, row=3)
    txt2.grid(column=1, row=4)
    txt3.grid(column=1, row=5)

    btn4.configure(text="Решить уравнение", command=clicked21)
    btn4.grid(column=1, row=6)

def clicked21():
    lbl3.grid_remove()
    lbl4.grid_remove()
    lbl5.grid_remove()

    btn4.grid_remove()

    txt1.grid_remove()
    txt2.grid_remove()
    txt3.grid_remove()

    a = float(format(txt1.get()))
    b = float(format(txt2.get()))
    c = float(format(txt3.get()))

    discr = b ** 2 - 4 * a * c
    res = "Дискриминант= {}".format(discr)

    lbl1.configure(text=res)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        lbl2.configure(text="Ответ: x1={}".format(x1))
        lbl2.grid(column=1, row=5)
        lbl3.configure(text="Ответ: x2={}".format(x2))
        lbl3.grid(column=1, row=6)
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
        lbl2.configure(text="Ответ: x={}".format(x))
        lbl2.grid(column=1, row=5)
    else:
        lbl2.configure(text="Корней нет")
        lbl2.grid(column=1, row=5)

def clicked3():# третий экран когда выбрали уравнение третей степени
    txt.grid_remove()

    btn1.grid_remove()
    btn2.grid_remove()
    btn3.grid_remove()

    res = "Привет, {}".format(txt.get())

    lbl1.configure(text=res)
    lbl2.configure(text="Решаем кубическое уравнение a*x**3+b*x**2+c*x+d=0, запишите коэффициенты")
    lbl2.grid(column=1, row=2)

# Первое окно, здоровается, знакомиться и предлагает выбрать тип уравнения
window = Tk()
window.title("Добро пожаловать в приложение по решению уравнений")
window.geometry('800x500')
lbl1 = Label(window, text="Привет это приложение поможет решить тебе уравнение")
lbl1.grid(column=1, row=0)
lbl2 = Label(window, text="Как тебя зовут?")
lbl2.grid(column=0, row=1)

txt = Entry(window, width=10)
txt.grid(column=1, row=1)
txt1 = Entry(window, width=10)
txt2 = Entry(window, width=10)
txt3 = Entry(window, width=10)

lbl3 = Label(window, text="Какое уравнение ты хочешь решить?")
lbl3.grid(column=1, row=3)
lbl4 = Label(window, text="")
lbl5 = Label(window, text="")
lbl6 = Label(window, text="")

btn1 = Button(window, text="Линейное уравнение", command=clicked1)
btn1.grid(column=0, row=4)
btn2 = Button(window, text="Квадратное уравнение", command=clicked2)
btn2.grid(column=1, row=4)
btn3 = Button(window, text="Кубическое уравнение", command=clicked3)
btn3.grid(column=2, row=4)
btn4 = Button(window, text="")

keys = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
values = []

window.mainloop()
