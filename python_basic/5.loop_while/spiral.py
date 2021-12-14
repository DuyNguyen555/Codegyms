import turtle
pen = turtle.Turtle()
pen.speed(10.5)
count = 1
while count <= 30:
    pen.circle(10*count,180)
    count += 1

turtle.exitonclick()