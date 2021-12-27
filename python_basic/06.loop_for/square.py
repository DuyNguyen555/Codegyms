import turtle as t
# cài cửa sổ
t.bgcolor("black")
t.title("rectangle")

# Cài bút vẽ
t.pensize(3)
t.color("blue")

# Vẽ hình vuông
for i in range (4):
    t.fd(200)
    t.rt(90)

t.exitonclick()