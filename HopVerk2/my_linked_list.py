class LinkedList:
    ''' List datatype connected as sequence of nodes that point to each other '''
    class _Node:
        ''' Simple node representing a cell in a list, it saves the location of the next Node of the list '''
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next 

    def __init__(self):
        ''' initialize important variables '''
        self.size = 0
        self.head = None
        self.tail = None
        self.size = 0

# ====================== PRINT FUNCTIONS FOR THE CLASS ====================== #

    def __str__(self):
        ''' Returns a string of all the elements of the list seperated by a space '''
        if self.size == 0:
            return "" # Empty
        else:
            return self.make_list_str(self.head)

    def make_list_str(self, list_node):
        ''' Recursive function that returns all the elements of a list seperated by a space ''' 
        if list_node.next == None:
            return str(list_node.data) # No need for a space at the last element
        else:
            # Add the value stored in current node and run recursively through the next nodes 
            return str(list_node.data) + " " + self.make_list_str(list_node.next)

# ====================== PUBLIC FUNCTIONS FOR THE CLASS ====================== #

    def get_size(self):
        ''' function that returns the size of the list '''
        return self.size

    def pop_front(self):
        ''' Function that removes and returns the value at the front of the list '''
        if self.size == 0:
            return None # Nothing to return in an empty list
        else:
            new_head = self.head.next # the new head is next to the one that is being removed
            return_value = self.head.data # Save the value
            # Help with the garbage collection
            self.head.data = None
            self.head.next = None
            self.head = new_head
            self.size -= 1
            return return_value

    def push_back(self, value):
        ''' Function that adds a value to the front of the list '''
        if self.size == 0:
            self._set_for_first(value)
        else:
            new_tail = self._Node(value, None)
            self.tail.next = new_tail # The old tail points to the new tail
            self.tail = new_tail # Assign the new tail
        self.size += 1

    def push_front(self, value):
        ''' Function that adds a value to the back of the list '''
        if self.size == 0:
            self._set_for_first(value)
        else:
            self.head = self._Node(value, self.head) # The new head points to the old head
        self.size += 1

# ====================== NON-PUBLIC FUNCTIONS FOR THE CLASS====================== #

    def _set_for_first(self, value):
        ''' Helper function that assigns head and tail for a empty list '''
        # If the list is empty, the tail and head point to the same cell
        self.head = self._Node(value, None)
        self.tail = self.head