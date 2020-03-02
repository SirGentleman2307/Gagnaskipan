class DLL:
    ''' Data structure composed of nodes that point to their successor and predecessor '''
    class _Node:
        def __init__(self, next, prev, data):
            self.next = next
            self.prev = prev
            self.data = data

    def __init__(self):
        ''' Initialize the class

            Values needed for the linked list
            ---------------------------------
            header, trailer : Node
                Empty Nodes(sentinels) that point to the head and the tail of the linked list
            current : Node
                Holds the node that is currently being pointed at, removes and inserts at/or around that node
            current_index : int
                indicates what index the current is pointing at (0 : (self.size-1)) for unreversed,
                (-1 : (self.size-2)) for reveresed
            is_reversed : boolean
                Indicates wheter the list is reversed or not. We fake that the list is reversed for O(1) time
            size : int
                size of the linked list
        ''' 
        self.header = self._Node(None, None, None)
        self.trailer = self._Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.current = self.trailer
        self.current_index = 0
        self.is_reversed = False
        self.size = 0
    
    # ============= PRINT FUNCTIONS ================ #

    def __str__(self):
        ''' Function that prints out the elements in the linked list in order '''
        if self.size == 0:
            return ""
        elif self.is_reversed:
            # Make the string ordered from the back to represent it is reversed
            return self._make_str_recursive(self.trailer.prev)
        else:
            return self._make_str_recursive(self.header.next)

    def _make_str_recursive(self, current):
        ''' Function that creates the sting that represents the elements in the list, reversed or not '''
        # Last element of the list, base step
        if self.header == self._next_step(current) or self.trailer == self._next_step(current):
            return str(current.data) + " "
        else:
            return str(current.data) + " " + self._make_str_recursive(self._next_step(current)) # Iterate

    def _next_step(self, current):
        ''' Function that detects what the next step is in the list depending if it is reversed or not '''
        if self.is_reversed:
            return current.prev
        else:
            return current.next

    # ============= MISCELLANEOUS FUNCTIONS ================ #

    def __len__(self):
        ''' Function that returns number of elements stored in the linked list '''
        return self.size

    def get_value(self):
        ''' Function that returns the value of the current node '''
        return self.current.data

    def reverse(self):
        ''' Function that reverses the list '''
        self.is_reversed = not self.is_reversed # Fake it with a boolean
        self._reset_current()

    def _reset_current(self):
        ''' Function that resets the current to the front of the list, used in sort, reverse and remove all '''
        # The current node and index depends on whether the list is reversed or not 
        self.current = self.header.next if not self.is_reversed else self.trailer.prev  # H 1 2 3 T | T 3 2 1 H
        self.current_index = 0 if not self.is_reversed else self.size - 1

    # ============= INSERT AND REMOVE FUNCTIONS ================ #

    def insert(self, value):
        ''' Function that inserts a value in front of the current node '''
        if not self.is_reversed:
            # Insert in front of the current node
            self._insert_between(self.current, self.current.prev, value)
        else:
            # Reversed: insert behind the current node
            self._insert_between(self.current.next, self.current, value)
            self.current_index += 1 # Fix the index
        
    def _insert_between(self, successor, predecessor, value):
        ''' Function that inserts a value into the list between two nodes, and connects them all together '''
        new_node = self._Node(successor, predecessor, value)
        predecessor.next = new_node
        successor.prev = new_node
        self.current = new_node # New current will be the new node 
        self.size += 1

    def remove(self):
        ''' Function that removes a value at the current node '''
        # Can't remove if the current is a sentinel
        if self.current != self.header and self.current != self.trailer:
            self._remove_between(self.current.prev, self.current.next)
            self.size -= 1

    def _remove_between(self, in_front, behind):
        ''' Function that removes the node that the pointer points to, fixes the connection between nodes '''
        self.current.next, self.current.prev = None, None # Help with the garbage collection
        # Establish the new connections
        in_front.next = behind
        behind.prev = in_front
        # The currents becomes the node behind(closer to tail) of the node removed
        if not self.is_reversed:
            self.current = behind
        else:
            # If the list is reversed then the node will come in front but for the user it will look like it want behind
            self.current = in_front 
            self.current_index -= 1 # Fix the index

    def remove_all(self, value):
        ''' Function that removes all elements that equal to the value given '''
        # Keep track of if the current changed and if the list is reveresed
        changed_reverse, current_changed = False, False
        if self.is_reversed:
            # To make this function simpler we temporally make it unreversed
            self.is_reversed = False
            changed_reverse = True # Make sure that we know we did this
        if self.get_value() == value:
            # The current will be removed, move it to the beginning of the list after the removal
            current_changed = True
            org_index = 0
        else:
            # The current will stay on the same node, save it
            org_current = self.current
            org_index = self.current_index

        org_index = self._remove_walk(value, org_index)

        if changed_reverse:
            self.is_reversed = True # Make it reversed again
        if current_changed:
            self._reset_current() # New current will be at the front of the list
        else:
            # The current didn't change
            self.current = org_current
            self.current_index = org_index 

    def _remove_walk(self, value, org_index):
        ''' Function that checks every element of the list and removes elements that fit given value, returns the index of original '''
        self.current = self.header.next
        self.current_index = 0
        # Check all the values until we hit the trailer
        while self.current != self.trailer:
            # Need to remove this node
            if self.get_value() == value:
                # Original index will move one to the left as long as current has not passed it
                if org_index > self.current_index:
                    org_index -= 1
                self.remove()
            else:
                self.move_to_next() # step
        return org_index

    # ============= MOVE CURRENT FUNCTIONS ================ #

    def move_to_next(self, checked = False):
        ''' Function that moves the current node one to the right(closer to tail)
            checked: If the list is reversed it has to move the other way '''
        # End node is diffrent for a reversed and un-reversed list
        end_node = self.trailer if not self.is_reversed else self.trailer.prev
        if self.is_reversed and not checked:
            self.move_to_prev(True) # Move to prev for reversed list
        elif self.current != end_node:
            # Move the current one to the right
            new_current = self.current.next
            self.current = new_current
            self.current_index += 1

    def move_to_prev(self, checked = False):
        ''' Function that moves the current node one to the left(closer to head)
            checked: If the list is reversed it has to move the other way '''
        # End node is diffrent for a reversed and un-reversed list
        end_node = self.header.next if not self.is_reversed else self.header
        if self.is_reversed and not checked:
            self.move_to_next(True) # Move to next for reversed list
        elif self.current != end_node:
            # Move the current one to the left
            new_current = self.current.prev
            self.current = new_current
            self.current_index -= 1

    def move_to_pos(self, position):
        ''' Function that moves the current to a new index(position), given that it is valid '''
        # Can go from the head node to the trailer sentinel
        if 0 <= position <= self.size:
            if self.is_reversed:
                # Equation for new index  of the position if the list is reversed
                position = (self.size - 1) - position
            while self.current_index != position:
                # Move to the end of the list
                if self.current_index < position:
                    self.move_to_next() if not self.is_reversed else self.move_to_prev()
                else:
                    # Move to the beginning of the list
                    self.move_to_prev() if not self.is_reversed else self.move_to_next()

    # ============= SORTING FUNCTIONS ================ #

    def sort(self):
        ''' Function that sorts a linked list using merge sort '''
        # If the list is 0 or 1 elements then it is already sorted
        if self.size > 1:
            # Connect the header to the sorted list
            self.header.next = self._merge_sort(self.header.next, self.size)
            self._connect_prev() # Connect the prev for each node in the list
        if self.is_reversed:
            self.is_reversed = False # It will print the list from highest to lowest if kept True
        self._reset_current()

    def _connect_prev(self):
        ''' Function that connects all the nodes predecessor correctly as long as the successors are correct '''
        walk = self.header
        while walk != self.trailer:
            # Connect the successor to the previous node
            successor = walk.next
            successor.prev = walk
            walk = walk.next # step

    def _merge_sort(self, head_1, size):
        ''' Function that sorts a linked list using merge sort,
            It sorts it so that each node connects to their successor but not their predecessor '''
        if size == 1: # list of size 1 is sorted
            return head_1
        mid = size//2
        head_2 = self._split_list(head_1, mid) # Split the list in two
        size_1, size_2 = self._get_size_after_split(size, mid)
        head_1 = self._merge_sort(head_1, size_1) # Split the smaller lists until they are only contain 1 element
        head_2 = self._merge_sort(head_2, size_2)
        return self._merge_lists(head_1, head_2) # Merge the sorted lists togehter into a larger sorted list

    def _get_size_after_split(self, size, mid):
        ''' Function that returns the size of two list after they are split '''
        if size%2 == 1:
            return mid, mid + 1
        else:
            return mid, mid

    def _split_list(self, head, mid):
        ''' Function that splits a list down the middle, making two different lists '''
        for _ in range(mid - 1): # Until we reach the middle
            head = head.next
        head_2 = head.next # new head will be the continued path of the other
        head.next = self.trailer # seperate the head from head_2
        return head_2 # Save it

    def _merge_lists(self, head_1, head_2):
        ''' Function that merges two list toghther, if they are both sorted,
            the resulting list will also be sorted '''
        # Base case
        # If we reach the end on either of the head the rest of the other head will connect to the previous head
        if head_1 == self.trailer:
            return head_2
        elif head_2 == self.trailer:
            return head_1
        # Recursive step
        else:
            if head_1.data > head_2.data:
                # Smaller value will connect to the next smaller value
                head_2.next = self._merge_lists(head_1, head_2.next)
                return head_2
            else:
                head_1.next = self._merge_lists(head_1.next, head_2)
                return head_1