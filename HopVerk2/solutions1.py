

class SLL_Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def is_ordered(head):

    if head.next == None:
        return True

    if head.data < head.next.data or head.data > head.next.data:
        return is_ordered(head.next)
    else:
        return False

# print(is_ordered(SLL_Node(1,SLL_Node(2,SLL_Node(3)))))
print(is_ordered(SLL_Node(1,SLL_Node(3,SLL_Node(2)))))
# print(is_ordered(SLL_Node(3,SLL_Node(2,SLL_Node(1)))))