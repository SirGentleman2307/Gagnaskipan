# Error Classes
class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

# ArrayList Class

class ArrayList:
    def __init__(self, capacity = 4):
        ''''''
        self.__size = 0
        self.__capacity = capacity
        self.__array = [None] * self.__capacity
        self.isorderd = True

    def __str__(self):
        '''Output: A string with numbers in the arraylist
         with ", " inbetween'''

        if self.__size == 0:
            return ''

        output_str = ''
        for i in range(self.__size - 1):
            output_str += str(self.__array[i]) + ", "
        output_str += str(self.__array[self.__size - 1])
        return output_str

# Main Fuctions

    def prepend(self, value):
        '''Adds given value to the front of the array'''
        self._resize_check()

        self._shift_array(self.__size, 0, True)
        self.__array[0] = value
        self.__size += 1

    def insert(self, value, index):

        self._index_check(index)
        self._resize_check()
        self._shift_array(self.__size, index, True)
        self.__array[index] = value
        self.__size += 1

    def append(self, value):
        '''Adds given value to the end of array'''
        self._resize_check()
        self.__array[self.__size] = value
        self.__size += 1

    def set_at(self, value, index):
        '''Replacing given value with the value at given index in array'''
        self._index_check(index)
        self.__array[index] = value

    def get_first(self):
        '''Returns the first value of array'''
        if self.__size == 0:
            raise Empty('Is empty')
        return self.__array[0]

    def get_at(self, index):
        '''Returns the value at given index in array'''
        if self.__size == 0:
           raise Empty('Is empty')
        self._index_check(index)
        return self.__array[index]

    def get_last(self):
        '''Returns the last value of array'''
        if self.__size == 0:
           raise Empty('Is empty')
        return self.__array[self.__size - 1]

    def resize(self):
        '''Doubles the capacity of the array'''
        self.__capacity *= 2
        new_array = [None] * self.__capacity

        for i in range(self.__size):    # Transfer all data form array to new_arry
            new_array[i] = self.__array[i]
        self.__array = new_array

    def remove_at(self, index):
        '''Removes value at given index'''
        self._index_check(index)
        self._shift_array(index, self.__size, False)
        self.__size -= 1

    def clear(self):
        '''Resets the array to it's starting values'''
        self.__capacity = 4
        self.__array = [None] * self.__capacity
        self.__size = 0
        self.isorderd = True

    def insert_ordered(self, value):
        '''First checks if the array is ordered then adds value so
         the array is ordered'''
        self._ordered_cheak(self.size - 1)
        if not self.isorderd:
            raise NotOrdered('Array not ordered')
        if self.__size > 0:
            insert_index = self._find_index_binary(value, 0, self.__size - 1)
        else:
            insert_index = 0
        self.insert(value, insert_index)

    def find(self, value):
        '''Finds index of given value'''
        if self.__size == 0:
           raise NotFound('Value not in array')
        if self.isorderd:
            return self._find_index_binary(value, 0, self.__size - 1)
        else:
            return self._find_index_linear(value, self.__size - 1)

    def remove_value(self, value):
        '''Removes first instans of the value'''
        if self.__size == 0:
           raise Empty('Is empty')
        if self.isorderd:
            remove_index = self._find_index_binary(value, 0, self.__size - 1)
        else:
            remove_index = self._find_index_linear(value, self.size - 1)
        self.remove_at(remove_index)

# Helper Functions

    def _resize_check(self):
        '''Checks if resizing is needed'''
        if self.__size >= self.__capacity:
            self.resize()

    def _shift_array(self, start, stop, shift_right):
        '''Shifts the array 1 space to the right or left'''
        if shift_right:
            shift_int = -1
        else:
            shift_int = 1

        for i in range(start, stop, shift_int):
            self.__array[i] = self.__array[i + shift_int]

    def _index_check(self, index):
        '''Checks if given index is valid'''
        if type(index) == int:
           if index >= self.__size or index < 0:
               raise IndexOutOfBounds('Index out of bounds!')
        else:
            raise TypeError('Index needs to be an int')

    def _ordered_cheak(self, index):
        '''Cheaks if the array is ordered'''
        Value = self.__array[index]
        if type(Value) != int:
            self.isorderd = False

        if index == 0:
            return True
        elif Value < self.__array[index - 1]:
            return False
        else:
            self._ordered_cheak(index - 1)

    def _find_index_binary(self, value, min_index, max_index):
        '''Finds given value recursively with binary search, given that the array is ordered'''
        if max_index - min_index == 0:  # If we have only one value to check
            if value > self.__array[max_index]:
                return max_index + 1
            else:
                return max_index
        else:   # We have more than one value to check
            mid_index = (max_index - min_index)//2
            mid_value = self.__array[mid_index]

            if value > mid_value:
                return self._find_index_binary(value, mid_index + 1, max_index)
            elif value < mid_value:
                return self._find_index_binary(value, min_index, mid_index)
            else:
                return mid_index

    def _find_index_linear(self, value, index):
        '''Finds given value recursively with linear search'''
        if index < 0:
            raise NotFound('Value not in array')
        elif value == self.__array[index]: # Value found
            return index
        else:
            return self._find_index_linear(value, index - 1)

