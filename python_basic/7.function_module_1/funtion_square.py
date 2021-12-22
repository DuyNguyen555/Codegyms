import turtle as t
# Màu bút
t.color('red')
# Độ dày bút
t.pensize(3)
def square(edge):
    # Góc
    angle = 90
    for _ in range(4):
        t.fd(edge)
        t.rt(angle)
    t.done()
    
square(100)