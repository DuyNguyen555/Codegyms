import turtle
import random

p = turtle.Turtle()
p.hideturtle()
p.penup()
p.goto(-350,0)
up = random.randint(10,40)
down = random.randint(10,40)
p.color('green')
p.showturtle()

count = 0
while count <= 10:
    p.pendown()
    p.fd(up)
    p.penup()
    p.fd(down)
    count += 1

turtle.done()