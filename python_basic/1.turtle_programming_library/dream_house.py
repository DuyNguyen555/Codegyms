import turtle

# create backgroup
turtle.bgcolor("skyblue")
turtle.setup(7000,800,1,1)
# create pen
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(100)

# ##create house
# #front
pen.penup()
pen.bk(600)
pen.lt(90)
pen.bk(350)
pen.pendown()

pen.fillcolor("blue")
pen.begin_fill()
for i in range(4):
    pen.fd(400)
    pen.rt(90)
pen.end_fill()

# door
pen.penup()
pen.rt(90)
pen.fd(150)
pen.lt(90)
pen.pendown()
pen.fillcolor("lime")
pen.begin_fill()
for i in range(2):
    pen.fd(200)
    pen.rt(90)
    pen.fd(100)
    pen.rt(90)
pen.end_fill()

# #left side
pen.penup()
pen.rt(90)
pen.fd(250)
pen.lt(30)
pen.pendown()

pen.fillcolor("yellow")
pen.begin_fill()
pen.fd(250)
pen.lt(60)
pen.fd(400)
pen.lt(120)
pen.fd(250)
pen.lt(60)
pen.fd(400)
pen.end_fill()

# window
pen.penup()
pen.lt(180)
pen.fd(240)
pen.rt(60)
pen.fd(100)
pen.pendown()

pen.fillcolor("brown")
pen.begin_fill()
pen.fd(80)
pen.lt(60)
pen.fd(90)
pen.lt(120)
pen.fd(80)
pen.lt(60)
pen.fd(90)
pen.end_fill()
pen.penup()
pen.rt(60)
pen.fd(100)
pen.rt(120)
pen.fd(160)
pen.pendown()

# #roof
pen.fillcolor("fuchsia")
pen.begin_fill()
pen.lt(45)
pen.fd(282)
pen.lt(90)
pen.fd(283)
pen.lt(135)
pen.fd(400)
pen.end_fill()

pen.fillcolor("orange")
pen.begin_fill()
pen.lt(30)
pen.fd(250)
pen.lt(105)
pen.fd(282)
pen.lt(75)
pen.fd(250)
pen.lt(105)
pen.fd(282)
pen.end_fill()
# ##End_Home

pen.penup()
pen.rt(45)
pen.fd(400)
pen.lt(90)
pen.fd(600)
pen.pendown()

# Tree
pen.fillcolor("Brown")
pen.begin_fill()
for i in range (2):
    pen.fd(50)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
pen.end_fill()
pen.lt(90)
pen.fd(100)

pen.fillcolor("lawngreen")
pen.begin_fill()
pen.lt(90)
pen.fd(75)
pen.bk(200)
pen.rt(45)
pen.fd(141)
pen.lt(90)
pen.fd(141)
pen.end_fill()
pen.bk(141)
pen.rt(135)
pen.end_fill()
for i in range(2):
    pen.begin_fill()
    pen.lt(90)
    pen.fd(100)
    pen.bk(200)
    pen.rt(45)
    pen.fd(141)
    pen.lt(90)
    pen.fd(141)
    pen.end_fill()
    pen.bk(141)
    pen.rt(135)
    pen.end_fill()
# #End_try

pen.penup()
pen.fd(200)
pen.lt(90)
pen.fd(200)
pen.pendown()
# #sun
pen.speed(5)
for i in range(4):
    pen.fd(100)
    pen.bk(100)
    pen.lt(90)
    
pen.lt(45)
for i in range(4):
    pen.fd(75)
    pen.bk(75)
    pen.lt(90)

pen.fillcolor("gold")
pen.rt(135)
pen.fd(50)
pen.lt(90)
pen.begin_fill()
pen.circle(50)
pen.end_fill()
    
turtle.done()