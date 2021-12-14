def week(i):
    switcher={
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    return switcher.get(i,"Ngay ko co trong tuan")

def main():
    try:
        i = int(input())
        print(week(i))
    except:
        print('ko hop le')
if __name__ == '__main__':
    main()
