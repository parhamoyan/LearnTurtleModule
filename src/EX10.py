from turtle import *
import random
color("red", "yellow")
setup(800, 400)
pensize(5)
penup()
goto(-50, -50)
pendown()
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
hideturtle()
