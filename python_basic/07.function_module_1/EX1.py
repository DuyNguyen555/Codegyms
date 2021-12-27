def giai_thua(n):
# n!
    if n == 1:
        return 1
    else:
        return n*giai_thua(n-1)

def giai_thua_2(n):
    '''
    BT VẬN DỤNG : SỬ DỤNG VÒNG LẶP FOR VIẾT
    HÀM KHỬ ĐỆ QUY BÀI TÍNH GIAI THỪA
    HƯỚNG DẪN: SỬ DỤNG BIẾN KẾT QUẢ , DÙNG TOÁN TỬ NHÂN
    LẶP TỪ 2 ĐẾN N + 1
    '''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    try:
        n = int(input("Nhập số: "))
        print(giai_thua_2(n))
    except:
        print("Error")

if __name__ == '__main__':
    main()
