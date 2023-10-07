import random
import turtle as t
import math
import time

print("Привет! Эта программа создаёт треугольник Серпинского красные точки это вершины треугольнка синия точка это начальная точка зелёные точки это точки самого фрактала / Hello! This program creates the Sierpinski triangle the red dots are the vertices of the triangle the blue dot is the starting point green dots are the points of the fractal itself")
size = int(input("примерный размер / approximate size: "))
line = int(input("количество точек / amount of points: "))
x = 0
wndow = t.Screen()
wndow.title("Треугольник Серпинского / Sierpinski triangle")
wndow.setup(1000, 500)
r1 = 1
r6 = 6
#создание координат точек треугольника / creating triangle point coordinates

#12
pointX1 = random.random() *size
pointY1 = random.random() *size
#34
pointX2 = random.random() *size
pointY2 = random.random() *size
#56
pointX3 = random.random() *size
pointY3 = random.random() *size

StartPointX = random.random() *size
StartPointY = random.random() *size

#Создание треуольника и стартовой точки / Creating a triangle and starting point

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
		#print(x34, y34)
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
	if kosta == 2:
		corX = t.xcor()
		corY = t.ycor()
		x12 = (pointX1 + corX)/2
		y12 = (pointY1 + corY)/2
		t.setx(x12)
		t.sety(y12)
		t.dot()
		x += 1
	if kosta == 4:
		corX = t.xcor()
		corY = t.ycor()
		x34 = (pointX2 + corX)/2
		y34 = (pointY2 + corY)/2
		t.setx(x34)
		t.sety(y34)
		t.dot()
		x += 1
	if kosta == 6:
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