# Danh sách liên kết đơn, danh sách liên kết đôi, 
# danh sách liên kết vòng

# B1: khởi tạo danh sách liên kết đơn
class Node:
    def __init__(self, data=None):
        # Tạo một nút của  DSLK trỏ tới None = Null
        self.dataval = data
        self.nextval = None

class linked_list:
    def __init__(self):
        self.headval = None

    def listprint(self): 
        printval = self.headval
        #Duyệt từ đầu đến cuối danh sách liên kết 
        while printval is not None:
            # In nút hiện tại
            print(printval.dataval)
            # Cập nhật nút mới
            printval = printval.nextval

    def at_begining(self, newdata):
        new_node = Node(newdata)
        new_node.nextval = self.headval
        self.headval = new_node

    def at_ending(self, newdata):
        new_node = Node(newdata)
        if self.headval is None:
            self.headval = new_node
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = new_node
#Hàm xóa một nút trong DSLK:
    def RemoveNode(self,RemoveKey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if(HeadVal.dataval == RemoveKey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while(HeadVal is not None):
            if HeadVal.dataval == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        if (HeadVal == None):
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None

if __name__ == '__main__':
    list_1 = linked_list()
    list_1.headval = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    list_1.headval.nextval = e2
    e2.nextval = e3
    list_1.at_begining(4)
    list_1.at_ending(9)
    list_1.RemoveNode(4)
    list_1.listprint()
    
#VẬN DỤNG KIỂM TRA SỐ NGUYÊN TỐ, TỔNG SỐ CHẴN, LẺ TRONG DSLK
#vận dụng 3: SẮP XẾP DANH SÁCH LIÊN KẾT
#LIST.SORT()
#GỢI Ý: CÁCH DỄ
#DUYỆT QUA CÁC PHẦN TỬ CỦA DANH SÁCH LK
#THÊM MỘT LIST TẠM, 
# CÁCH KHÓ: HOÁN VỊ, CẬP NHẬT LẠI ĐỊA
# CHỈ CỦA DS LIÊN KẾT
#VẬN DỤNG 4: TÌM KIẾM PHẦN TỬ TRONG DSLK 
#DÙNG PP DUYỆT DANH SÁCH LK, SO SÁNH