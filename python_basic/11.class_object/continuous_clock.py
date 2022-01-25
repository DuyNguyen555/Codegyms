from turtle import *
import time
# """Create the screen"""
screen = Screen()
screen.bgcolor("black")
screen.title("Clock")
screen.setup(width = 500, height = 500)
screen.tracer(0)

class Continuous_clock():
    
    def __init__(self, pencolor):
        self.pencolor = pencolor
    
    def face_clock(self, radium = 200, size = 3):
        """Draw the face of the clock"""
        pen = Turtle()
        pen.hideturtle()
        pen.color(self.pencolor)
        pen.penup()
        pen.goto(x = 0, y = -radium)
        pen.pendown()
        pen.pensize(size)
        pen.circle(radium)
        pen.penup()
        pen.goto(0,0)
        pen.pendown()
    
    def clock_makings(self, size, angle, count_angle, hide_height, height):
        """Draw the clock makings for the hours, minutes"""
        pen = Turtle()
        pen.pensize(size)
        pen.hideturtle()
        pen.color(self.pencolor)
        for _ in range (count_angle):
            pen.penup()
            pen.fd(hide_height)
            pen.pendown()
            pen.fd(height)
            pen.penup()
            pen.goto(0,0)
            pen.pendown()
            pen.rt(angle)
        
    def paint_clock(self):
        """Draw full the clock"""
        # Inside
        self.face_clock()
        # Outside
        self.face_clock(220, 7)
        # clock makings for the hours
        self.clock_makings(7, 30, 12, 180, 20)
        # clock makings for the minutes
        self.clock_makings(3, 6, 60, 190, 10)
    
    def clock_work(self, color, count_angle, height, time_clock):
        pen = Turtle()
        pen.pensize(2)
        pen.hideturtle()
        angle = (time_clock / count_angle) * 360
        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)
        pen.color(color)
        pen.rt(angle)
        pen.pendown()
        pen.fd(height)
    
if __name__ == '__main__':
    clock = Continuous_clock("skyblue")
    clock.paint_clock()
    while True:
        # second
        s = int(time.strftime("%S"))
        # minutes
        m = int(time.strftime("%M"))
        # hours
        h = int(time.strftime("%I"))
        clock.clock_work("pink", 60, 150, s)
        clock.clock_work("blue", 60, 100, m)
        clock.clock_work("red", 12, 50, h)
        screen.update()