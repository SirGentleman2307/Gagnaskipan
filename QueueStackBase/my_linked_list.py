class Node:

    def __init__(self, data, next = None):
        self.data = str(data)
        self.next = next



class LinkedList():

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def push_back(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def push_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def pop_front(self):
        self.size -= 1
        if self.size < 0:
            self.size = 0
            return None
        else:
            out_value = self.head.data
            self.head = self.head.next
            return out_value

    def get_size(self):
        return self.size

    def __str__(self):
        out_str = ''
        n = self.head.next
        while n != self.tail:
            out_str += n.data + ' '
            n = n.next
        return out_str