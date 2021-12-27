def premeter_rectangle(width,length):
    premeter = (width+length)*2
    return premeter

def area_rectangle(width,lenght):
    area = width*lenght
    return area

def color_rectangle(width,length):
    import turtle
    color = input("Color or color code: ")
    turtle.color(color)
    turtle.begin_fill()
    for i in range (2):
        turtle.fd(length)
        turtle.rt(90)
        turtle.fd(width)
        turtle.rt(90)
    turtle.end_fill()
    
    turtle.done()
    
def main():
    width = int(input("Enter the width of the rectangle: "))
    length = int(input("Enter the length of the rectangle: "))
    print("Premeter of the rectangle:", premeter_rectangle(width, length))
    print("Area of the rectangle:", area_rectangle(width,length))
    color_rectangle(width, length)
    
if __name__ == "__main__":
    main()