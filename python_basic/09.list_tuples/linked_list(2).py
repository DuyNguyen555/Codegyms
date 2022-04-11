class Node:
    def __init__(self, num = None):
        self.data = num
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_begin_list(self, new_num):
        new_node = Node(new_num)
        new_node.next = self.head
        self.head = new_node

    def append_end_list(self, new_num):
        new_node = Node(new_num)
        if self.head is None:
            new_node = self.head
            return
        num_next = self.head
        while num_next.next:
            num_next = num_next.next
        num_next.next = new_node

    def remove_num(self, num):
        pass

    def display_list(self):
        list_num =[]
        num = self.head
        while num is not None:
            list_num.append(num.data)
            num = num.next
        print(list_num)

if __name__ == '__main__':
    linked = LinkedList()
    linked.head = Node(1)
    list_2 = Node(2)
    list_3 = Node(3)
    linked.head.next = list_2
    list_2.next = list_3
    linked.append_begin_list(0)
    linked.append_begin_list(-1)
    linked.append_end_list(4)
    linked.append_end_list(5)
    linked.display_list()