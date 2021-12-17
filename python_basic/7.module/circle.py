import turtle as t
import math

def draw(r):
    """Hàm vẽ hình tròn với bán kính r"""
    t.speed(1)
    t.hideturtle()
    t.pencolor('red')
    t.circle(r)
    t.done()

def area(r):
    """Hàm tính diện tích hình tròn với bán kính r"""
    return math.pi * r * r

def main():
    r = int(input("Enter radius: "))
    print(area(r))
    draw(r)

if __name__ == '__main__':
    main()