import turtle
import random

def circle():
    # create the limit of turtle
    limit = turtle.Turtle()
    limit.hideturtle
    limit.pensize(5)
    limit.speed(20)
    limit.penup()
    limit.goto(0,-200)
    limit.pendown()
    limit.circle(200)
    
def _turtle_():
    # create turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.pensize(3)
    # create turtle angle
    count = 0
    while count <= 10:
        t.speed(1)
        t.forward(188)
        t.hideturtle()
        t.speed(10)
        t.goto(0, 0)
        # swivel angle
        angle = random.randint(0, 360)
        t.right(angle)
        t.showturtle()
        count += 1

def main():
    circle()
    _turtle_()
    turtle.done()
    
if __name__ == '__main__':
    main()