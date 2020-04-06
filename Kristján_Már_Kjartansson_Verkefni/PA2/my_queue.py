from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:

    def __init__(self, type_input):
        self.queue = self.get_type(type_input)
        self.type_str = type_input

    def add(self, value):
        '''Adds given value to the end of queue
         depending on type used'''
        if self.type_str == 'array':
            self.queue.push_back(value)
        elif self.type_str == 'linked':
            self.queue.push_back(value)

    def remove(self):
        '''Returns and removes the value in the front of queue'''
        if self.type_str == 'array':
            return self.queue.pop_front()
        elif self.type_str == 'linked':
            return self.queue.pop_front()

    def get_size(self):
        '''Returns the size of queue'''
        if self.type_str == 'array':
            return self.queue.get_size()
        elif self.type_str == 'linked':
            return self.queue.get_size()

    def get_type(self, type_input_str):
        '''Returns the type of given string input'''
        if type_input_str == 'array':
            return ArrayDeque()
        elif type_input_str == 'linked':
            return LinkedList()

    def __str__(self):
        '''Returns the str of given type'''
        return self.queue.__str__()