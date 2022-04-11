def sort(x, y, z):
    sorted_number = sorted((x, y, z))
    return sorted_number

def main():
    x, y ,z = (int(input("Enter 3 number: ")) for _ in range (3))
    print('Original number:',x ,y , z)
    print('Sorted number:', end = ' ')
    for i in sort(x, y, z):    
        print(i, end =" ")

if __name__ == '__main__':
    try:
        main()
    except:
        print('Error')