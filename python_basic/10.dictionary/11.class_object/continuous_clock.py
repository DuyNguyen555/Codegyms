from turtle import *
import time

class Continuous_clock():
    def __init__(self, pencolor):
        self.pencolor = pencolor
    
    def screen(self, width_screen = 500, height_screen = 500, color = "black"):
        """Create the screen"""
        global screen
        screen = Screen()
        screen.bgcolor(color)
        screen.title("Clock")
        screen.setup(width = width_screen, height = height_screen)
        screen.tracer(0)
        
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
    
    def clock_work(self, 
        color_second , count_angle_second , height_second , time_clock_second,
        color_minutes, count_angle_minutes, height_minutes, time_clock_minutes,
        color_hours  , count_angle_hours  , height_hours  , time_clock_hours):
        """Work"""
        global pen2
        pen2 = Turtle()
        pen2.pensize(3)
        pen2.hideturtle()
        angle_second = (time_clock_second / count_angle_second) * 360
        angle_minutes = (time_clock_minutes / count_angle_minutes) * 360
        angle_hours = (time_clock_hours / count_angle_hours) * 360
        pen2.penup()
        # second
        pen2.goto(0,0)
        pen2.setheading(90)
        pen2.color(color_second)
        pen2.rt(angle_second)
        pen2.pendown()
        pen2.fd(height_second)
        # minutes
        pen2.goto(0,0)
        pen2.setheading(90)
        pen2.color(color_minutes)
        pen2.rt(angle_minutes)
        pen2.pendown()
        pen2.fd(height_minutes)
        # hours
        pen2.goto(0,0)
        pen2.setheading(90)
        pen2.color(color_hours)
        pen2.rt(angle_hours)
        pen2.pendown()
        pen2.fd(height_hours)
        
    def update_clock(self):
        screen.update()
        time.sleep(1)
        pen2.clear()

if __name__ == '__main__':
    clock = Continuous_clock("skyblue")
    clock.screen()
    clock.paint_clock()
    while True:
        # second
        s = int(time.strftime("%S"))
        # minutes
        m = int(time.strftime("%M"))
        # hours
        h = int(time.strftime("%I"))
        clock.clock_work("pink", 60, 150, s, "blue", 60, 100, m, "red", 12, 50, h)
        clock.update_clock()