import turtle as t
import random
t.setup(800,800,0,0)

def full_turtle():
    # lưu tất cả rùa vào list
    global all_turtle
    all_turtle = []
    # Màu của rùa
    color_turtle = ['red', 'blue', 'green', 'yellow', 'pink', 'black']
    # Tốc độ của rùa
    global speed_turtle
    speed_turtle = [8, 12, 5, 17, 20, 23]
    # Nơi xuất phát
    position_x = -350
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

def SpeedTurtle():
    
    pass

def main():
    full_turtle()
    t.exitonclick()

if __name__ == '__main__':
    main()