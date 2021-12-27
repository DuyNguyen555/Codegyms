import turtle

# Màu nền
turtle.bgcolor("black")
# Tạo bút
pen = turtle.Turtle()
# Độ dày
pen.pensize(5)
# Màu
pen.color("#98F5FF")
# Tốc độ
pen.speed(0)

def square(angle):
    for _ in range(3):
        pen.fd(100)
        pen.rt(90)    

    pen.fd(100)
    pen.rt(90 + angle)

step = 36
angle = 360 / step
for i in range(step):
    square(angle) 

turtle.done()
