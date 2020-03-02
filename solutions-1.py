
class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


def is_ordered(head):
    LTH = True
    while head.next != None:
        if LTH:
            if head.data < head.next.data:
                head = head.next
            else:
                return False
        else:
            if head.data > head.next.data:
                head = head.next
            else:
                return False
    return True


class DLL_List:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
        self.size = 0
        self.head = None
        self.tail = None

    def build_list(self,lis):
        if lis == []:       # If there is no data in the list return None
            return None

        if self.head != None or self.tail != None:      # Reset head and tail
            self.head = None
            self.tail = None

        for data in lis:
            new_node = DLL_List(data)
            self.size += 1

            if self.size == 1:                  # If the size is 1 the head and tail will point to the same node
                self.head = new_node
                self.tail = new_node
            else:                               # Insert the next node infront of the tail
                new_node.prev = self.tail       # Current tail is the second to last node in the DLL
                self.tail.next = new_node       # Current tail points to the new node
                self.tail = new_node            # The new node becomes the new tail

    def print(self, backwards = False):

        if backwards:                               # See if print is going to be backwaeds or not
            node = self.tail                        # Start form the tail and iterate to the head
            while node:                             # See if the node has data or is None
                print(str(node.data), end= ' ')
                node = node.prev
        else:
            node = self.head                        # Start form the head adn iterate to the tail
            while node:                             # See if the node has data or is None
                print(str(node.data), end= ' ')
                node = node.next
        print()

    def contains(self, val):
        node = self.head
        while node:                 # See if the node has data or is None
            if node.data == val:    # If the node data is the given val return True
                return True
            node = node.next
        return False

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))
