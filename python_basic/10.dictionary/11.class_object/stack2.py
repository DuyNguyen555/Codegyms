class stack(object):
    def __init__(self, limit_num = 10):
        self.stk = []
        self.limit = limit_num
        
    def display(self):
        x = self.stk
        x.reverse()
        print("||      ||")
        for i in x:
            print(f"|| |{i}| ||")
        print("==========")

    def push(self, item):
        """
        Hàm này để thêm 1 mục vào
        """
        if len(self.stk) >= self.limit: print("Ngăn xếp đầy")
        else: self.stk.append(item); print("Ngăn xếp đã được thêm vào")
        
    def pop(self):
        """
        Hàm này để lấy ra mục ở trên cùng trong ngăn xếp
        """
        if len(self.stk) == 0:
            print("Ngăn xếp rổng")
            return 0
        else:
            def_item = self.stk.pop()
            print("Lấy ra mục này:", def_item)
            return def_item

if __name__ == '__main__':
    stack1 = stack()
    stack1.push(54)
    stack1.push(96)
    stack1.push(71)
    stack1.push(35)
    stack1.push(10)
    stack1.push(22)
    stack1.pop()
    stack1.display()