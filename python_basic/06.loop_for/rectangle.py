def rectangle():
    length = int(input("Input length: "))
    width = int(input("Input width: "))
    while True:
        if length > width:
            break
        else:
            print("length > width , this's a rectangle, Try again ")    
            length = int(input("Input length: "))
            width = int(input("Input width: "))
    # Chiều rộng = cột
    for i in range(1,width + 1):
        # chiều dài = hàng
        for j in range(1,length + 1):
            if j == 1 or i == 1 or i == width or j == length:
                print("*", end = " ")
            else:
                print(" ",end = " ")
        print()


def main():
    try:    
        rectangle()
    except:
        print("Error")

if __name__ == '__main__':
    main()