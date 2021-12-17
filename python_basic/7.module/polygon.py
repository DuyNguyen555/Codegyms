import turtle as t
# Độ dày
t.pensize(3)
# màu bút
t.color("skyblue")
# ẩn bút
t.hideturtle()
t.setup(1400,800,0,0)

def Polygon(num, edge = 100):
    angle = (num - 2) * 180 / num
    for i in range (num):
        t.fd(edge)
        t.rt(180-angle)
    t.done()

def main():
    Polygon(5)

if __name__ == '__main__':
    main()