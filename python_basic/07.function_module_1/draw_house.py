import turtle
# Hiển thị độ to màn hình
turtle.setup(1530,800,0,0)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(5)

def rectangle(length = 150,width = 100,color = "skyblue"):
    # Bút vẽ 
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.fd(length)
        pen.rt(90)
        pen.fd(width)
        pen.rt(90)
    pen.end_fill()

def roof():
    pen.color("black")
    pen.fillcolor("#FF33FF")
    pen.begin_fill()
    pen.fd(100)
    pen.rt(135)
    pen.fd(180)
    pen.rt(45)
    pen.fd(650)
    pen.rt(45)
    pen.fd(180)
    pen.rt(135)
    pen.fd(800)
    pen.end_fill()
    
def house_body():
    pen.penup()
    pen.goto(0,-450)
    pen.lt(90)
    pen.pendown()
    color1 = ["#6699FF","#9999FF","#CC99FF"]
    for i in range(7):
        for j in color1:
            pen.penup()
            pen.color(j)
            pen.fd(150)
            pen.pendown()
            rectangle(color = j)
        pen.penup()
        pen.bk(450)
        pen.lt(90)
        pen.fd(100)
        pen.rt(90)
        pen.pendown()

def door():
    pen.fillcolor("#33CCCC")
    pen.begin_fill()
    for _ in range(2):
        pen.fd(150)
        pen.rt(90)
        pen.fd(100)
        pen.rt(90)
    pen.end_fill()
    pen.rt(90)
    pen.fd(50)
    pen.lt(90)
    pen.fd(150)
    
def window():
    pen.color("black")
    pen.fillcolor("white")
    pen.begin_fill()    
    for _ in range (2):
        for _ in range (2):
            pen.fd(150)
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
        pen.rt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()
    pen.fd(75)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(75)

def main():
    house_body()
    pen.up()
    pen.home()
    pen.goto(-600,150)
    pen.lt(180)
    pen.down()
    roof()
    pen.up()
    pen.home()
    pen.goto(-200,-150)
    pen.rt(90)
    pen.down()
    door()
    pen.penup()
    pen.home()
    pen.rt(90)
    pen.pendown()
    window()
    pen.up()
    pen.lt(90)
    pen.fd(400)
    pen.lt(90)
    pen.down()
    window()
    
    turtle.exitonclick()

if __name__ == '__main__':
    main()