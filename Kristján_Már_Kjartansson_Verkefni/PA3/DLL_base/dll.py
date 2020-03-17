
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
        self.size = 0

    def __str__(self):
        '''Returns string with all elements in the DLL'''
        out_str = ''
        n = self.head
        while n:
            out_str += str(n.data) + ' '
            n = n.next
        return out_str

    def __len__(self):
        '''Retruns the length of the DLL'''
        out_int = 0
        n = self.head
        while n:
            out_int  += 1
            n = n.next
        return out_int

    def insert(self, value):
        '''Inserts given value to the front of current position'''
        if self.current:
            new_node = Node(value, self.current, self.current.next)
            self.current.next = new_node
            self.current = new_node
        else:
            self.current = Node(value)
        self.size += 1

        if self.size == 1:
            self.head = self.current    # Set Head
            self.tail = self.current    # Set Tail

        if self.current.next == None:   # Check for head and tail
            self.tail = self.current
        if self.current.prev == None:
            self.head = self.current

    def remove(self):
        '''Removes current position's value'''
        if self.size <= 0:
            self.size = 0
            return None

        if self.current.next == None and self.current.prev == None: # If we remove only one value
            self.current = None
            self.head = None
            self.tail = None
        elif self.current == self.head: # If current is head
            self.current = self.head.next
            self.current.prev = None
            self.head = self.current
        elif self.current == self.tail: # If current is tail
            self.current = self.tail.prev
            self.current.next = None
            self.tail = self.current
        else:
            self.current.next.prev = self.current.prev
            self.current.prev.next = self.current.next
            self.current = self.current.prev
        self.size -= 1

    def get_value(self):
        '''Gets the value of current position'''
        if self.current:
            return str(self.current.data)

    def move_to_next(self):
        '''Moves the current position to the next'''
        if self.current:
            if self.current.next != None:
                self.current = self.current.next

    def move_to_prev(self):
        '''Moves the current position to the prev'''
        if self.current:
            if self.current.prev != None:
                self.current = self.current.prev

    def move_to_pos(self, position):
        '''Sets current position to given position'''
        if position < 0:
            position = self.size
        elif position > self.size:
            position = self.size

        node_at = self.head
        for _ in range(position - 1):
            node_at = node_at.next
        self.current = node_at

    def remove_all(self, value):
        '''Removes all value from DLL that are the sama as given value'''
        N = self.head
        while N:
            self.current = N
            if N.data == value:
                self.remove()   # Remove N
            N = N.next
        self.current = self.head

    def reverse(self):
        '''Reverses the order of the DLL'''
        N = self.head
        while N:
            N_temp = N.next
            N.next = N.prev
            N.prev = N_temp
            N = N_temp
        temp_head = self.head
        self.head = self.tail
        self.tail = temp_head
