import random
import turtle as t
import math
import colorama
from colorama import *
init()

print("Привет! Эта программа создаёт треугольник Серпинского", Fore.RED + "красные", " точки это вершины треугольнка", Fore.BLUE + "синия"," точка это начальная точка", Fore.GREEN + "зелёные"," точки это точки самого фрактала", Fore.WHITE + " / Hello! This program creates the Sierpinski triangle the", Fore.RED + "red", " dots are the vertices of the triangle the", Fore.BLUE + "blue"," dot is the starting point", Fore.GREEN + "green"," dots are the points of the fractal itself")
print("    ")
print(Fore.WHITE + "Хотите сами задать точки или сделать их случвйно? / Do you want to set the points yourself or make them successfully?")
ask = input("Напешите yes или no / write yes or no: ")
print("    ")
xy = input("Сделать координатную сетку / Make a coordinate grid? /p (write yes or no / напешите yes или no): ")
#создание координат точек треугольника / creating triangle point coordinates
if ask == "no":
	size = 250
	#1
	pointX1 = random.random() *size
	pointY1 = random.random() *size
	#3
	pointX2 = random.random() *size
	pointY2 = random.random() *size
	#5
	pointX3 = random.random() *size
	pointY3 = random.random() *size
	#StartPoint
	StartPointX = random.random() *size
	StartPointY = random.random() *size
if ask == "yes":
	#1
	pointX1 = int(input("Введите 1Х кординату / Enter 1X coordinate: "))
	pointY1 = int(input("Введите 1Y координату / Enter 1X coordinate: "))
	#3
	pointX2 = int(input("Введите 2X координату / Enter 2X coordinate:"))
	pointY2 = int(input("Введите 2Y координату / Enter 2Y coordinate:"))
	#5
	pointX3 = int(input("Введите 3X координату / Enter 3X coordinate:"))
	pointY3 = int(input("Введите 3Y координату / Enter 3Y coordinate:"))
	#StartPoint
	StartPointX = int(input("Enter StartPointX coordinate: "))
	StartPointY = int(input("Enter StartPointY coordinate: "))
line = int(input("количество точек / amount of points: "))
x = 0
wndow = t.Screen()
wndow.title("Треугольник Серпинского / Sierpinski triangle")
wndow.setup(1000, 500)
r1 = 1
r6 = 6
#Создание треуольника и стартовой точки / Creating a triangle and starting point
if xy == "yes":
	t.color("grey")
	t.goto(0, 0)
	t.pendown()
	t.goto(-50, 0)
	t.write('-x', font=('Helvetica', 18, 'bold'))
	t.penup()
	t.goto(0, 0)

	t.pendown()
	t.goto(50, 0)
	t.write('+x', font=('Helvetica', 18, 'bold'))
	t.penup()
	t.goto(0, 0)

	t.pendown()
	t.goto(0, 50)
	t.write('+y', font=('Helvetica', 18, 'bold'))
	t.penup()
	t.goto(0, 0)

	t.pendown()
	t.goto(0, -50)
	t.write('-y', font=('Helvetica', 18, 'bold'))
	t.penup()
if xy == "no":
	print("    ")
	t.penup()

t.color("red")
t.goto(pointX1, pointY1)
t.dot()
t.goto(pointX2, pointY2)
t.dot()
t.goto(pointX3, pointY3)
t.dot()
t.goto(StartPointX, StartPointY)
t.color("blue")
t.dot()
t.color("green") 

#Создание точек для фрактала и рассчёт маршрута до точек / Creating points for a fractal and calculating the route to the points

while x != line:
	kosta = random.randint(r1, r6)
	if kosta == 1:
		corX = t.xcor()
		corY = t.ycor()
		x12 = (pointX1 + corX)/2
		y12 = (pointY1 + corY)/2
		t.setx(x12)
		t.sety(y12)
		t.dot()
		x += 1
	if kosta == 3:
		corX = t.xcor()
		corY = t.ycor()
		x34 = (pointX2 + corX)/2
		y34 = (pointY2 + corY)/2
		t.setx(x34)
		t.sety(y34)
		t.dot()
		x += 1
	if kosta == 5:
		corX = t.xcor()
		corY = t.ycor()
		x56 = (pointX3 + corX)/2
		y56 = (pointY3 + corY)/2
		t.setx(x56)
		t.sety(y56)
		t.dot()
		x += 1
	if x == line:
		t.goto(0,0)
		int=input()
	pass
