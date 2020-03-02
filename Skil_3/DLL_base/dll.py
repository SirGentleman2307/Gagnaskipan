
class Node:
    def __init__(self, data = '', prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.none_node = Node(None, self.tail, self.head)
        self.size = 0

    def __str__(self):
        out_str = ''
        n = self.head
        while n:
            out_str += str(n.data) + ' '
            n = n.next
        return out_str

    def __len__(self):
        out_int = 0
        n = self.head
        while n:
            out_int  += 1
            n = n.next
        return out_int

    def insert(self, value):
        self.size += 1

        new_node = Node(value, self.current, self.current.next)
        self.current.next = new_node
        self.current = new_node

        if self.size == 1:
            self.head = self.current    # Set Head
            self.tail = self.current    # Set Tail


    def remove(self):
        self.size -= 1

        if self.size < 0:
            self.size = 0
            return None
        else:
            self.current.next.prev = self.current.prev
            self.current.prev.next = self.current.next
            self.current = self.current.prev

        if self.current.next == None:
            self.tail = self.current


    def get_value(self):
        return str(self.current.data)

    def move_to_next(self):
        pass

    def move_to_prev(self):
        pass

    def move_to_pos(self, position):
        pass

    def remove_all(self, value):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass