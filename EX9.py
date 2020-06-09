from turtle import *
import random
color("red")
setup(800, 400)

begin_fill()
penup()
goto(-50, -50)
for i in range(4):
    forward(100)
    left(90)
pendown()
end_fill()
hideturtle()
