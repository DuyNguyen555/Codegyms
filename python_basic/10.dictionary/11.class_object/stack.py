class Stack(object):
    #khởi tạo ngăn xếp với giới hạn
    def __init__(self,limit = 10):
        self.stk = []
        self.limit = limit
    #phương thức 2: kiểm tra ngăn xếp có rỗng
    #hay không 
    def isEmpty(self):
        return len(self.stk) <= 0
    #phương thức 3: thêm một phần tử vào ngăn xếp
    #phương thức PUSH 
    def push(self,item):
        #kiểm tra xem ngăn xếp có đầy hay chưa
        if len(self.stk)>= self.limit:
            print('NGĂN XẾP ĐẦY!')
        else: 
            self.stk.append(item)
        print('Ngan xep da duoc them vao')
    #PHƯƠNG THỨC 4 : LẤY MỘT PHẦN TỬ TRONG NGĂN XẾP 
    #RA NGOÀI , PHƯƠNG THỨC POP 
    def pop(self):
        #kiểm tra chiều dài ngăn xếp <=0 thông báo lỗi 
        if len(self.stk) <= 0:
            print('Ngan xep rong')
            return 0
        else: 
            return self.stk.pop()
    #phương thức 5: tính chiều dài của ngăn xếp 
    def size(self): 
        return len(self.stk)

if __name__ == "__main__": 
    our_stack = Stack(5)
    our_stack.push(5)
    our_stack.isEmpty()