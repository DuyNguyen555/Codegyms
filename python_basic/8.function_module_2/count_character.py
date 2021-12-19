def count(text):
    length = len(text)
    return length

def main ():
    Text_str = str(input("Your srting: "))
    print('Length: ', count(Text_str))

if __name__ == '__main__':
    main()