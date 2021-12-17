import turtle as t
from random import randint
# màu nền
t.bgcolor('black')
# độ to màn hình
t.setup(1530,800,0,0)
# Độ dày của bút
t.pensize(3)
# Tốc độ vẽ
t.speed(100)
# Tất cả màu
t.colormode(255)

def elip():
    # Bán kinh
    r = 200
    # Góc quay
    rotation_angle = 0
    
    while rotation_angle < 36:
        #  màu có tọa độ (0, 0, 0) là màu đen trùng với màu nền nên loại tọa độ màu này ra
        t.color(randint(1,255),randint(1,255),randint(1,255))
        # Vẽ elip
        count = 0
        while count < 2:
            t.circle(r,90)
            t.circle(r/2,90)
            count += 1
        # Xoay góc
        t.rt(10)
        rotation_angle += 1

def main():
    elip()
    t.exitonclick()

if __name__ == '__main__':
    main()