import turtle
pen = turtle.Turtle()
pen.speed(5)
distance_limit = int(input())
count = 0
while int(pen.distance(0,0)) <= distance_limit:
    pen.circle(10*count,180)
    count += 1

turtle.exitonclick()

