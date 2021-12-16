def Input():
    start_end = input().split()
    return start_end

def fizz_buzz():
    # xét 2 số có ép kiểu được số nguyên không
    try:
        # số đầu tiên, số cuối ép kiểu thành số nguyên
        start, end = map(int,Input())
        # xét điều kiện cho 2 số đầu, cuối
        if start > end:
            print("End number < start number. Try again")
        else:
            print('Begin'.center(20, "*"))
            for i in range (start, end + 1):
                if i % 3 == 0 or i % 5 ==0:
                    if i % 3 == 0 and i % 5 == 0:
                        print("FizzBuzz")
                    elif i % 3 == 0:
                        print("Fizz")
                    else:
                        print("Buzz")
                else:
                    print(i)
            else:
                print('End'.center(20, '*'))
    except:
        # 2 số không phải số nguyên
        print("Error")

def main():
    fizz_buzz()
    
if __name__ == '__main__':
    main()