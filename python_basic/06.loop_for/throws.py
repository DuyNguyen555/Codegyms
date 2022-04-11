def _throws():
    try: 
        return 20/0
    except ZeroDivisionError:
        print('Chia cho không')
    except Exception as problem:
        print('Ngoại lệ')
    finally:
        print('Hủy thực hiện phép toán')

if __name__ == '__main__':
    _throws()