import turtle

g = 90
g2 = 100
g3 = 282
g4 = 200
g5 = 400
# create backgroup
turtle.bgcolor("skyblue")
turtle.setup(7000,800,1,1)
# create pen
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(50)


# ##create house
# #front
pen.penup()
pen.bk(600)
pen.lt(g)
pen.bk(350)
pen.pendown()

pen.fillcolor("blue")
pen.begin_fill()
for i in range(4):
    pen.fd(g5)
    pen.rt(g)
pen.end_fill()

# door
pen.penup()
pen.rt(g)
pen.fd(150)
pen.lt(g)
pen.pendown()
pen.fillcolor("lime")
pen.begin_fill()
for i in range(2):
    pen.fd(g4)
    pen.rt(g)
    pen.fd(g2)
    pen.rt(g)
pen.end_fill()

# #left side
pen.penup()
pen.rt(g)
pen.fd(250)
pen.lt(30)
pen.pendown()

pen.fillcolor("yellow")
pen.begin_fill()
pen.fd(250)
pen.lt(60)
pen.fd(g5)
pen.lt(120)
pen.fd(250)
pen.lt(60)
pen.fd(g5)
pen.end_fill()

# window
pen.penup()
pen.lt(180)
pen.fd(240)
pen.rt(60)
pen.fd(g2)
pen.pendown()

pen.fillcolor("brown")
pen.begin_fill()
pen.fd(80)
pen.lt(60)
pen.fd(g)
pen.lt(120)
pen.fd(80)
pen.lt(60)
pen.fd(g)
pen.end_fill()
pen.penup()
pen.rt(60)
pen.fd(g2)
pen.rt(120)
pen.fd(160)
pen.pendown()

# #roof
pen.fillcolor("fuchsia")
pen.begin_fill()
pen.lt(45)
pen.fd(g3)
pen.lt(g)
pen.fd(283)
pen.lt(135)
pen.fd(g5)
pen.end_fill()

pen.fillcolor("orange")
pen.begin_fill()
pen.lt(30)
pen.fd(250)
pen.lt(105)
pen.fd(g3)
pen.lt(75)
pen.fd(250)
pen.lt(105)
pen.fd(g3)
pen.end_fill()
# ##End_Home

pen.penup()
pen.rt(45)
pen.fd(g5)
pen.lt(g)
pen.fd(600)
pen.pendown()

# Tree
pen.fillcolor("Brown")
pen.begin_fill()
for i in range (2):
    pen.fd(50)
    pen.lt(g)
    pen.fd(g2)
    pen.lt(g)
pen.end_fill()
pen.lt(g)
pen.fd(g2)

pen.fillcolor("lawngreen")
pen.begin_fill()
pen.lt(g)
pen.fd(75)
pen.bk(g4)
pen.rt(45)
pen.fd(141)
pen.lt(g)
pen.fd(141)
pen.end_fill()
pen.bk(141)
pen.rt(135)
pen.end_fill()
for i in range(2):
    pen.begin_fill()
    pen.lt(g)
    pen.fd(g2)
    pen.bk(g4)
    pen.rt(45)
    pen.fd(141)
    pen.lt(g)
    pen.fd(141)
    pen.end_fill()
    pen.bk(141)
    pen.rt(135)
    pen.end_fill()
# #End_try

pen.penup()
pen.fd(g4)
pen.lt(g)
pen.fd(g4)
pen.pendown()
# #sun
for i in range(4):
    pen.fd(g2)
    pen.bk(g2)
    pen.lt(g)
    
pen.lt(45)
for i in range(4):
    pen.fd(75)
    pen.bk(75)
    pen.lt(g)

pen.fillcolor("gold")
pen.rt(135)
pen.fd(50)
pen.lt(g)
pen.begin_fill()
pen.circle(50)
pen.end_fill()
pen.shapesize(0.1)


turtle.done()