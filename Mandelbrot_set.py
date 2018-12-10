# -*- coding: utf-8 -*- #
from matplotlib import pylab

import pylab
from Tkinter import *

#freal.write(str(x) + "\n");fim.write(str(y) + "\n");
#freal = open("outputreal.txt", "w")
#fim = open("outputimage.txt", "w")
#freal.close()
#fim.close()


def printer(event):
	xlist = []
	ylist = []

	def manfunc(x, y):
		z = 0 + 0j
		c = complex(x, y)
		i = 0
		while abs(z) < 2 and i <= 100:
			z = z * z + c
			i += 1
		xlist.append(x)
		ylist.append(y)

	X = -1.5
	Y = -1
	while X < 1.5:
		while Y < 1:
			manfunc(X, Y)
			Y = Y + 0.001
		Y = -1
		X = X + 0.001
	pylab.plot(xlist,ylist,'m.')
	pylab.grid()
	pylab.show()

#Создание интерфейса

#Создание главного объекта
root = Tk()

#Создание кнопки
but = Button(root,
          text="Нарисовать фрактал Мандельброта", #надпись на кнопке
          width=30,height=5, #ширина и высота
          bg="blue",fg="white") #цвет фона и надписи

#Создание радиобатона
var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="Красный",
          variable=var,value=0)
rad1 = Radiobutton(root,text="Черный",
          variable=var,value=1)
rad2 = Radiobutton(root,text="Пурпурный",
          variable=var,value=2)

#Создание метки
lab = Label(root, text="Выберите цвет фрактала", font="Arial 18")

#Привязка кнопки к событию
but.bind("<Button-1>",printer)



#Отображение элементов
but.pack()
lab.pack()
rad0.pack()
rad1.pack()
rad2.pack()
root.mainloop()# -*- coding: utf-8 -*- #
from matplotlib import pylab

import pylab
from Tkinter import *

#freal.write(str(x) + "\n");fim.write(str(y) + "\n");
#freal = open("outputreal.txt", "w")
#fim = open("outputimage.txt", "w")
#freal.close()
#fim.close()


def printer(event):
	xlist = []
	ylist = []

	def manfunc(x, y):
		z = 0 + 0j
		c = complex(x, y)
		i = 0
		while abs(z) < 2 and i <= 100:
			z = z * z + c
			i += 1
		xlist.append(x)
		ylist.append(y)

	X = -1.5
	Y = -1
	while X < 1.5:
		while Y < 1:
			manfunc(X, Y)
			Y = Y + 0.001
		Y = -1
		X = X + 0.001
	pylab.plot(xlist,ylist,'m.')
	pylab.grid()
	pylab.show()

#Создание интерфейса

#Создание главного объекта
root = Tk()

#Создание кнопки
but = Button(root,
          text="Нарисовать фрактал Мандельброта", #надпись на кнопке
          width=30,height=5, #ширина и высота
          bg="blue",fg="white") #цвет фона и надписи

#Создание радиобатона
var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="Красный",
          variable=var,value=0)
rad1 = Radiobutton(root,text="Черный",
          variable=var,value=1)
rad2 = Radiobutton(root,text="Пурпурный",
          variable=var,value=2)

#Создание метки
lab = Label(root, text="Выберите цвет фрактала", font="Arial 18")

#Привязка кнопки к событию
but.bind("<Button-1>",printer)



#Отображение элементов
but.pack()
lab.pack()
rad0.pack()
rad1.pack()
rad2.pack()
root.mainloop()
