def sort(x, y, z):
    sorted_number = sorted((x, y, z))

    return ' '.join(sorted_number)

def main():
    x, y ,z = [str(input("Enter 3 number: ")) for _ in range (3)]
    print('Original number:',x ,y , z)
    print('Sorted number: ',sort(x, y, z))

if __name__ == '__main__':
    main()