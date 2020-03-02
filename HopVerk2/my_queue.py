from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, type_str):
        ''' Initialize the data type that holds the elements of the queue '''
        self.list_type = self._get_type(type_str) # Either linked list or array deque

    def _get_type(self, type_str):
        ''' Function that checks the string given in parameter and returns respective data type '''
        try:
            if type_str == "array" : return ArrayDeque()
            elif type_str == "linked" : return LinkedList()
            else : raise # invalid string
        except:
            raise InvalidTypeOfList("Invalid type of list(should be 'array' or 'linked')")

    def __str__(self):
        ''' return string of the elements of the list '''
        return str(self.list_type) # __str__ from their respected class 

# ====================== PUBLIC FUNCTIONS FOR THE CLASS ====================== #

    def add(self, value):
        ''' Function that adds a value to the back of the list in correlation with the rules of the queue '''
        self.list_type.push_back(value)
    
    def get_size(self):
        ''' Function that returns the number of elements in the queue '''
        return self.list_type.get_size()

    def remove(self):
        ''' Function that removes and returns a value to the at the front in correlation with the rules of the queue '''
        return self.list_type.pop_front()