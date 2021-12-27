
import turtle

def up():
    pen.penup()
def down():
    pen.pendown()
def bf():
    pen.begin_fill()
def ef():
    pen.end_fill()

if __name__ == "__main__":
    
    pen = turtle.Turtle()
    pen.pensize (5)
    pen.pencolor ("darkorange")
    pen.speed(20)
    # create big circle
    pen.fillcolor ("sandybrown")
    bf()
    pen.circle (100)
    ef()
    pen.pencolor("black")
    pen.fillcolor("black")
    # eye
    up() 
    pen.goto(40,120)
    down()
    eye = 10
    bf()
    pen.circle(eye)
    ef()
    up() 
    pen.goto(-40,120)
    down()
    bf()
    pen.circle(eye)
    ef()

    # smile
    up()
    pen.rt(90)
    pen.fd(70)
    pen.lt(40)
    down()
    pen.circle(50,100)

    pen.shapesize(0.1)
    turtle.exitonclick()