import turtle as t
# Hiển thị màn hình
t.setup(1530,800,0,0)
# Tiêu đề "Ngôi sao"
t.title("star")
# màu nền 
t.bgcolor("black")
# Đồ dày của bút
t.pensize(2)
# Tốc độ vẽ
t.speed(0)
# Màu vẽ
t.color("red")

def star():
    # Độ dài của ngôi sao
    lenght = 200
    # Góc của ngôi sao
    angle = 144
    for _ in range (1, 73):
        for _ in range (1, 6):
            t.fd(lenght)
            t.rt(angle)
        t.rt(5)
        
def main():
    star()
    t.exitonclick()
    
if __name__ == '__main__':
    main()