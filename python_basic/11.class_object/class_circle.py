import turtle
import math

class circle:
    def __init__(self, radium,):
        """Hàm khởi tạo có tham số"""
        self.radium = radium
    
    def draw(self):
        """Hàm này dùng để vẽ"""
        turtle.hideturtle()
        turtle.circle(self.radium)
        turtle.exitonclick()

    def area(self):
        """Hàm này tính diện tích hình tròn"""
        return math.pi * self.radium**2
    
    def perimeter(self):
        """Hàm này tính chu vi hình tròn"""
        return 2 * math.pi * self.radium

if __name__ == '__main__':
    c = circle(50)
    print("S =", c.area())
    print("C =", c.perimeter())
    c.draw()
    