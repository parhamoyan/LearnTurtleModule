from turtle import *
setup(840, 440)
speed(0)
pensize(1)

for j in range(2):
    for i in range(400//10+1):
        penup()
        goto(-200*(-1)**j,200-i*10)
        pendown()
        goto((-200+10*i)*(-1)**j,-200)

for j in range(2):
    for i in range(400//10+1):
        penup()
        goto(-200*(-1)**j,-200+i*10)
        pendown()
        goto((-200+10*i)*(-1)**j,+200)

hideturtle()
