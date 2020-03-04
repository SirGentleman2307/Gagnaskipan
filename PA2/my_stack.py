from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:

    def __init__(self, type_input):
        self.stack = self.get_type(type_input)
        self.type_str = type_input

    def push(self, value):
        '''Adds given value to the end of stack
         depending on type used'''
        if self.type_str == 'array':
            self.stack.push_front(value)
        elif self.type_str == 'linked':
            self.stack.push_front(value)

    def pop(self):
        '''Returns and removes the value on the to of stack (Last value)'''
        if self.type_str == 'array':
            return self.stack.pop_back()
        elif self.type_str == 'linked':
            return self.stack.pop_front()

    def get_size(self):
        '''Returns the size of stack'''
        if self.type_str == 'array':
            return self.stack.get_size()
        elif self.type_str == 'linked':
            return self.stack.get_size()

    def get_type(self, type_input_str):
        '''Returns the type of given string input'''
        if type_input_str == 'array':
            return ArrayDeque()
        elif type_input_str == 'linked':
            return LinkedList()

