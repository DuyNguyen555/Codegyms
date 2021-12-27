def circle(radius):
    import turtle
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.circle(radius)
    turtle.done()

    
def main():
    radius = int(input())
    circle(radius)

if __name__ == '__main__':
    main()