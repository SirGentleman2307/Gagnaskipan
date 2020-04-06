
class ArrayDeque():

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [None] * self.capacity

        self.head = 0
        self.tail = 0

    def push_back(self, value):
        '''Adds given value to the back of the deque'''
        self._resize_check()
        self.tail = self.push(self.tail)
        self.array[self.tail] = value
        self.size += 1

    def push_front(self, value):
        '''Adds given value to the front of the deque'''
        self._resize_check()
        self.head = self.push(self.head)
        self.array[self.head] = value
        self.size += 1

    def pop_back(self):
        '''Removes the last value in the deque and returns it'''
        if self.size == 0:
            return None

        self._resize_check()
        output_value = self.array[self.tail]
        self.array[self.tail] = None
        self.tail -= 1

        if self.tail < 0:   # Save gaurd
            self.tail = self.capacity - 1
        self.size -= 1
        return output_value

    def pop_front(self):
        '''Removes the last value in the deque and returns it'''
        if self.size == 0:
            return None

        self._resize_check()
        output_value = self.array[self.head]
        self.array[self.head] = None
        self.head += 1

        if self.head == self.capacity:   # Save gaurd
            self.head = 0
        self.size -= 1
        return output_value

    def get_size(self):
        return self.size

    def __str__(self):
        return self.make_str_rec(self.head)[:-2]

# ----- Helper Functions -----

    def _resize_check(self):
        '''Checks if resize is needed and dose so accordingly'''
        if self.size == self.capacity:  # Need to make the array bigger
            self.capacity *= 2
            new_array =[None] * self.capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array

    def make_str_rec(self, index, Passed_Head = False):
        '''Makes string with all emlements in deque'''
        if index == self.capacity:
            index = 0

        if index == self.head and Passed_Head: # Passed_Head is used to stop looping
            return ''
        else:
            if self.array[index]:
                return str(self.array[index]) + ', ' + self.make_str_rec(index + 1, True)
            return '' + self.make_str_rec(index + 1, True)

    def push(self, pointer):
        '''Returns index were the next value should go, depending on
         sould it go to the front/back'''
        if pointer == self.tail:
            movement = 1
        else:
            movement = -1

        if self.size != 0:
            return (pointer + movement) % self.capacity
        return pointer
