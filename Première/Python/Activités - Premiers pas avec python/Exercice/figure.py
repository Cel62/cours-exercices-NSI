from turtle import *

color("red")
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)

penup()
setx(-20)
pendown()
color("green")
for _ in range(6):
    left(60)
    forward(100)

penup()
setx(20)
pendown()
color("blue")

forward(40)
backward(20)
left(60)
for _ in range(6):
    forward(20)
    backward(20)
    left(60)