import turtle as t
from random import choice

def AllTurtle():
    # Biến dùng để lưu tất cả rùa
    global all_turtle
    all_turtle = []
    # Màu rùa
    color_turtle = ['red', 'black', 'green', 'blue']
    # Tọa độ đặt rùa
    position_x = -300
    position_y = [-30, 30, 90, 150]
    # Khởi tạo rùa
    for i in range(4):
        turtle = t.Turtle(shape = 'turtle')
        turtle.hideturtle()
        turtle.speed(0)
        turtle.penup()
        turtle.goto(x = position_x, y = position_y[i])
        turtle.showturtle()
        turtle.pendown()
        turtle.color(color_turtle[i])
        all_turtle.append(turtle)

def TurtleRunning(turtle):
    # Khoảng cách rùa chạy được trong 1 bước chạy
    speed_turtle = [5, 10, 15, 20, 25]
    run = True
    while run:
        for i in turtle:
            i.fd(choice(speed_turtle))
        if i.xcor() > 100:
            run = False

def main():
    AllTurtle()
    TurtleRunning(all_turtle)
    t.exitonclick()

if __name__ == '__main__':
    main()
