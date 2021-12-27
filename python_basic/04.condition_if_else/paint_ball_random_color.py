import turtle
import random

number = int(random.uniform(0,3))
print(number)
turtle.bgcolor('skyblue')
turtle.title('circle')
ball = turtle.Turtle()
ball.shape('circle')
ball.color('green') if number < 1 else ball.color('yellow') if number < 2 else ball.color('red') if number < 3 else print("This's no colors")



turtle.done()