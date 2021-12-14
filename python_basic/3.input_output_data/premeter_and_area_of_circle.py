def premeter_circle(r):
    import math
    premeter = 2*math.pi*r
    return premeter

def area_circle(r):
    import math
    area = math.pi*r*r
    return area

def paint_circle(r):
    import turtle
    turtle.pensize(5)
    turtle.color('blue')
    turtle.circle(r)
    turtle.pensize(0.1)
    turtle.done()

def main():
    r = float(input('Enter the radius: '))
    print('Premeter of the circle: %.2f'%(premeter_circle(r)))
    print('Area of the circle: %.2f'%(area_circle(r)))
    paint_circle(r)
    
if __name__ == "__main__":
    main()