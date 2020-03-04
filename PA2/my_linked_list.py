class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList(Node):

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push_back(self, value):
        '''Adds given value to the back of the Linked List 
         and links the value as a new node'''
        New_node = Node(value)
        if self.size == 0:
            self.head = New_node
            self.tail = New_node
        else:
            self.tail.next = New_node   # Tell current tail where to point
            self.tail = New_node    # Tell tail to point at new tail
        self.size += 1

    def push_front(self, value):
        '''Adds given value to the front of the Linked List 
         and links the value as a new node'''
        New_node = Node(value, self.head)
        if self.size == 0:
            self.head = New_node
            self.tail = New_node
        else:
            self.head = New_node
        self.size += 1

    def pop_front(self):
        '''Removes front value and retuns it'''
        if self.size == 0:
            return None
        else:
            output_value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return output_value

    def get_size(self):
        '''Returns size'''
        return self.size

    def __str__(self):
        return self.make_str_rec(self.head)


# ----- Helper Functions -----
    def make_str_rec(self, Node):
        '''Returns a string of all elements in list'''
        if Node:
            return str(Node.data) + ' ' + self.make_str_rec(Node.next)
        else:
            return ''
