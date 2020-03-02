class DequeIsEmpty(Exception):
    pass

class ArrayDeque:
    ''' Dynamic array type of deque '''
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.de_arr = [0]*self.capacity
        self.head = 0 # Track the position index of head and tail
        self.tail = 0

    def __str__(self):
        ''' for the print function, prints the list with the numbers and a space between them '''
        try:
            self._check_empty() # If it is empty we print ""
            de_arr_str = ""
            walk = self.head  # we don't want to change self.head
            for i in range(self.size - 1):
                de_arr_str += str(self.de_arr[walk]) + " "
                # Walks from the head, if it reaches max index it loops around
                walk = (walk + 1) % self.capacity  
            de_arr_str += str(self.de_arr[walk]) # Last line without a space
            return de_arr_str
        except DequeIsEmpty:
            return ""

# ====================== PUBLIC FUNCTIONS FOR THE CLASS ====================== #

    def get_size(self):
        ''' Function that returns the size of the list '''
        return self.size

    def pop_at(self, pointer_index):
        ''' Function that removes and returns value back/front depending on parameter '''
        try:
            self._check_empty() # Raises DequeIsEmpty if empty
            # Tail moves to the left and head to the right after removal of element
            increment = -1 if pointer_index == self.tail else 1
            return_value = self.de_arr[pointer_index] # Value to return
            self.de_arr[pointer_index] = 0 # Mark the slot of the value empty
            pointer_index = (pointer_index + increment) % self.capacity # max capacity loop
            self.size -= 1
            return return_value, pointer_index
        except DequeIsEmpty:
            return None, pointer_index

    def pop_back(self):
        ''' Function that removes and returns the last of the list '''
        # self.tail stays the same if the list is empty
        return_value, self.tail = self.pop_at(self.tail)
        return return_value

    def pop_front(self):
        ''' Function that removes and returns the first of the list '''
        # self.head stays the same if the list is empty
        return_value, self.head = self.pop_at(self.head)
        return return_value

    def push_back(self, value):
        ''' Function that pushes a value to back of the deque '''
        self._check_resize()
        self.tail = self.push_to(self.tail, value)

    def push_front(self, value):
        ''' Function that pushes a value to the front of the deque '''
        self._check_resize()
        self.head = self.push_to(self.head, value)

    def push_to(self, pointer_index, value):
        ''' Function that pushes a value to the front/back depending on parameters '''
        # increment determines where the head/tail goes next in the modulus loop
        increment = 1 if pointer_index == self.tail else -1
        if self.size != 0:
            # if self.size == 0 then the tail and head hold the same value
            pointer_index = (pointer_index + increment) % self.capacity # max_capacity loop
        self.de_arr[pointer_index] = value
        self.size += 1
        return pointer_index # Need to return the node so we can assign it to head/tail



# ====================== NON-PUBLIC FUNCTIONS FOR THE CLASS ====================== #

    def _resize(self, new_size):
        ''' Function to resize the list for new variables(or shorten a too big list) '''
        # Save the old capacity for the for loop and set the new
        old_capacity = self.capacity
        self.capacity = new_size
        bigger_de_arr = [0]*self.capacity
        walk = self.head # Don't want to change the head, walk to the tail
        for i in range(self.size):
            bigger_de_arr[i] = self.de_arr[walk] # arrange the new array so that head is in index 0 and tail the end of self.size
            walk = (walk + 1) % old_capacity # Walk to the tail, loops if it reaches the old capacity
        self.head, self.tail = 0, (self.size - 1)
        self.de_arr = bigger_de_arr

    def _check_resize(self):
        ''' Function to check if there is a need for resize '''
        if self.size == self.capacity:
            # If the list is too small we need to enlarge it
            self._resize(self.capacity * 2)
        elif self.size == self.capacity//4 and self.capacity > 4:
            # If the list has a lot of empty slots we shrink it
            self._resize(self.capacity // 2)

    def _check_empty(self):
        ''' Function to check whether the list is empty or not '''
        if self.size == 0:
            raise DequeIsEmpty()