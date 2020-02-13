

class Node:

    def __init__(self, data = None, Prev = None, Next = None):
        self.data = data
        self.prev = Prev
        self.next = Next

class DLL_Deque:

    def __init__(self):
        self.head = Node('Hello I am head')
        self.tail = Node('Bye I was tail')
        self.size = 0

    def add_front(self, data):
        New_Node = Node(data, self.head, self.head.prev)
        self.head.next = New_Node
    

    def __str__(self):
        out_str = ''
        N_Node = self.head.next
        while N_Node != self.tail:
            out_str += str(N_Node.data) + ''
            N_Node = N_Node.next
        return out_str

K = DLL_Deque()

K.add_front('Hello')
K.add_front('World')
K.add_front('I am ')
K.add_front('Alive')
K.add_front('Bitch')

print(K)