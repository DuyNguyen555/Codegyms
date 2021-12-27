import turtle as t
from random import choice
# Làm phần 2 của cuộc đua của loài rùa
import time

def Race():
    race = t.Turtle()
    race.speed(0)
    race.hideturtle()
    race.rt(90)
    for i in range(1,21):
        race.penup()
        race.goto(x = -320 + 20*i, y = 220)
        race.pendown()
        race.write(i)
        for j in range(10):
            race.fd(20)
            race.penup()
            race.fd(10)
            race.pendown()
        race.write(i)

def AllTurtle():
    # Biến dùng để lưu tất cả rùa
    global all_turtle
    all_turtle = []
    # Màu rùa
    global color_turtle
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
    global finish, finish_time
    # Làm phần 2 của cuộc đua của loài rùa
    finish = [0, 0, 0, 0]
    # Khoảng cách rùa chạy được trong 1 bước chạy
    speed_turtle = [5, 10, 15, 20, 25]
    run = True
    # Làm phần 2 của cuộc đua của loài rùa
    # Bắt đầu đếm thời gian
    start_time = time.time()
    while run:
        count = 0
        for i in turtle:
            speed = choice(speed_turtle)
            n = finish[count] + speed
            finish[count] = n
            i.fd(speed)
            count += 1
        if i.xcor() > 100:
            run = False
    end_time = time.time()
    finish_time = end_time - start_time


def main():
    Race()
    AllTurtle()
    TurtleRunning(all_turtle)
    t.exitonclick()

if __name__ == '__main__':
    main()