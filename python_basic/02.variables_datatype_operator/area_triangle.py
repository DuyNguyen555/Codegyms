import math
def triangle():
    # Nhap 3 lan
    a,b,c = [float(input("Input size: ")) for _ in range (3)]
    if a + b > c or a + c > b or b + c > a:
        # perimeter triangle
        p = (a+b+c)/2

        # area
        print("Area of the triangle: %.3f"%((math.sqrt((p*(p-a)*(p-b)*(p-c))))))
    else:
        print("Error")

def circle ():
    r = float(input("Input radius: "))
    s = math.pi * (r**2)
    print("Area of the circle: %.3f"%(s))

def square():
    a =float(input("Input size: "))
    print("Area of the square: %.3f"%(a*a))

if __name__ == '__main__':
    triangle()