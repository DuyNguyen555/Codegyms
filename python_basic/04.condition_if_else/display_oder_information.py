def information(money):
    if money >= 150:
        print("Total: ", money - 50)
    elif money >= 100:
        print("Total: ", money - 25)
    elif money >= 75:
        print("Total: ", money - 15)
    else:
        print("Total: " , money)

def main():
    money = float(input("Money oder: "))
    information(money)

if __name__ == '__main__':
    main()