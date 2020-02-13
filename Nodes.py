

class Node:

    def __init__(self, data = None, perv = None, next = None):
        self.data = data
        self.perv = perv
        self.next = next

class DDL_Deque:

    def __init__(self):
        self.head = Node('I am the Head')
        self.tail = Node('I am the Tail')
        self.head.next = self.tail
        self.tail.perv = self.head
        self.size = 0


    def add_front(self, data):
        self.size += 1
        new_node = Node(data, self.head, self.head.next)
        self.head.next.perv = new_node
        self.head.next = new_node

    def add_back(self, data):
        self.size += 1
        new_node = Node(data, self.tail.perv, self.tail)
        self.tail.perv.next = new_node
        self.tail.perv = new_node

    def remove_front(self):
        self.size -= 1
        self.head.next.next.perv = self.head
        self.head.next = self.head.next.next

    def remove_back(self):
        self.size -= 1
        self.tail.perv.perv.next = self.tail
        self.tail.perv = self.tail.perv.perv

    def get_value_front(self):
        print(str(self.head.next.data))

    def get_value_back(self):
        print(str(self.tail.perv.data))

    def get_size_value(self):
        print(str(self.size))

    def anti_print(self):
        n = self.tail.perv
        out_str = ''
        while n != self.head:
            out_str += str(n.data) + ' '
            n = n.perv
        print(out_str)

    def __str__(self):
        n = self.head.next
        out_str = ''
        while n != self.tail:
            out_str += str(n.data) + ' '
            n = n.next
        return out_str




K = DDL_Deque()

K.add_front('F')
K.add_front('E')
K.add_front('C')
K.add_front('A')
K.add_front('B')

K.add_back('\n')
K.remove_front()
K.remove_back()

K.add_back('G')
K.add_back('H')
K.add_back('I')
K.add_back('J')
K.add_back('K')

K.get_value_back()
K.get_value_front()

print(K)
K.get_size_value()
K.anti_print()