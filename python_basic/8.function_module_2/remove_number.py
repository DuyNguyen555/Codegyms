def remove_largest_number(num):

    """
    Xóa phần tử lớn nhất
    """

    # Sắp xếp từ nhỏ đến lớn rồi lấy giá trị cuối
    sort = sorted(num)[-1]
    # Xóa giá trị đó trong tham số num
    num.remove(sort)

def main():
    number = [9, 52, 79, 28, 37, 43, 22, 84, 16]
    remove_largest_number(number)
    print(number)

if __name__ == '__main__':
    main()