from turtle import *
setup(840, 440)
speed(0)
pensize(1)

for j in range(2):
    for i in range(800//20+1):
        penup()
        goto(-400*(-1)**j,200-i*10)
        pendown()
        goto((-400+20*i)*(-1)**j,-200)

for j in range(2):
    for i in range(800//20+1):
        penup()
        goto(-400*(-1)**j,-200+i*10)
        pendown()
        goto((-400+20*i)*(-1)**j,+200)

hideturtle()
