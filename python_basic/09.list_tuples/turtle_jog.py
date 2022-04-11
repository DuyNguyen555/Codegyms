import turtle as t
from random import choice
# Tạo màn hình
screen = t.Screen()
screen.setup(1500,300,0,0)

def race_track():
    race = t.Turtle()
    race.hideturtle()
    race.speed(0)
    position_race = -75
    for i in range(7):
        race.penup()
        race.goto(x = -660, y = position_race + 30*i)
        race.pendown()
        # for n in range(2):
        for j in range(4):
            race.fd(10)
            race.lt(90)
        race.fd(50)
    race.pensize(5)
    race.color("red")
    race.rt(90)
    race.fd(180)
    race.rt(180)

def full_turtle():
                
    # lưu tất cả rùa vào list
    global all_turtle
    all_turtle = []
    # Màu của rùa
    color_turtle = ['red', 'blue', 'green', 'orange', 'hotpink', 'black']
    # Khoảng cách mà rùa đi được
    global speed_turtle
    speed_turtle = [5, 10, 15, 20, 25, 30]
    # Nơi xuất phát
    position_x = -650
    position_y = [-60, -30, 0, 30, 60, 90]

    for i in range(6):
        turtles = t.Turtle(shape='turtle')
        turtles.hideturtle()
        turtles.speed(0)
        turtles.penup()
        turtles.goto(position_x, position_y[i])
        turtles.showturtle()
        turtles.pendown()
        turtles.color(color_turtle[i])
        all_turtle.append(turtles)

def Turtle_running(turtle):
    run = True
    while run:
        for i in turtle:
            i.penup()
            i.fd(choice(speed_turtle))
            i.pendown()
            i.fd(choice(speed_turtle))
        if i.xcor() > 100 :
            run = False

def main():
    race_track()
    full_turtle()
    Turtle_running(all_turtle)
    t.exitonclick()

if __name__ == '__main__':
    main()
