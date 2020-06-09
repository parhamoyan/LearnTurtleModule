from turtle import *
import random
colors = ["black", "cyan", "blue", "magenta", "green", "red", "aqua", "brown", "orange"]
n = 15
setup(1000, 500)
speed(0)

for i in range(1,360//n+1):
    color(colors[i%len(colors)])
    circle(50)
    setheading(i*n)
    
hideturtle()
