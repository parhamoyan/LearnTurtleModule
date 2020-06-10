from turtle import *
setup(840, 500)
speed(0)

for i in range(1,13):
    color("darkblue")
    penup()
    goto(-470+i*70,0)
    pendown()
    begin_fill()
    circle(25, i*30)
    goto(-470+i*70,25)
    end_fill()
    setheading(0)
    
hideturtle()
