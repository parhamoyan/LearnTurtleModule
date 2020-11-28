from turtle import *
setup(1000, 500)
speed(0)
pensize(3)
n = 15
colors = ["purple","indigo","blue","green", "yellow", "orange", "red"]
for j in range(1,360//15+1):
    color(colors[j%len(colors)])
    for i in range(4):
        forward(100)
        left(90)
    setheading(j*15)
hideturtle()
