from turtle import *
setup(600, 500)
speed(10)

# rainbow
colors = ["purple","indigo","blue","green", "yellow", "orange", "red"]
color("black")
for i in range(6, -1, -1):
    penup()
    goto(0,-(i+1)*10+50)
    pendown()
    color(colors[i])
    begin_fill()
    circle((i+1)*10)
    end_fill()
    
hideturtle()
