

class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def add_to_front(head, data):
    temp_node = Node()
    temp_node.data = data
    temp_node.next = head
    head = temp_node
    return head

def broken_add_to_front(head, data):
    return Node(data, head)

def remove_front(head):
    head = head.next
    return head

def add_to_back(head, data):
    node = head
    while True:
        if node.next == None:
            node.next = Node(data)
            return head
        else:
            node = node.next

def remove_back(head):
    node = head
    if node.next == None:
        return None

    while True:
        if node.next.next == None:
            node.next = None
            return head
        else:
            node = node.next

def display(head):

    if head:
        print(head.data, end= ' ')
        return display(head.next)
    return

head = Node()
head.data = 'I am the head !!!'

for i in range(11):
    head = broken_add_to_front(head, str(i))

head = remove_front(head)
head = add_to_back(head, -1)
head = add_to_back(head, -2)
head = add_to_back(head, -3)

head = remove_back(head)

display(head)



# ------------------------------


class Stacker:
    def __init__(self):
        self.head = Node('I am Head!!!')
        self.size = 0

    def __str__(self):
        return self.get_print_str(self.head)

    def get_print_str(self, head):

        if head:
            return head.data + ' ' + self.get_print_str(self.head.next)
        return ''

    def push(self, data):
        self.head = Node(data)


H = Stacker()
H.push('Nice')
print(H)
