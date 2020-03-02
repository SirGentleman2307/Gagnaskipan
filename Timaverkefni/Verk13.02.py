

class Node:

    def __init__(self, data = None, Prev = None, Next = None):
        self.data = data
        self.prev = Prev
        self.next = Next

def add_to_front(head, data):
    return Node(data, None, head)

def remove_front(head):
    head = head.next
    return head

def add_to_back(head, data):
    node = head
    if node == None:
        return Node(data)

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
        print(str(head.data), end= ' ')
        return display(head.next)
    print()
    return

def count_length_iter(head):
    try:
        n = head.next
    except AttributeError:
        return None

    counter = 0
    while n != None:
        counter += 1
        n = n.next
    return counter

def count_length_rec(head):
    try:
        n = head.next
    except AttributeError:
        return None

    if n == None:
        return 0
    else:
        return 1 + count_length_rec(n)

def add_ordered(head, value):
    pass



Head = Node('I am Head')
Head = remove_front(Head)
for i in range(11):
    Head = add_to_back(Head, i*2)
display(Head)
print(str(count_length_rec(Head)))
