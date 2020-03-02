class InvalidTypeOfList(Exception):
    pass

from my_linked_list import LinkedList
from my_array_deque import ArrayDeque

class Stack:
    def __init__(self, type_str):
        self.list_type = self._get_type(type_str)

    def __str__(self):
        return str(self.list_type)

    def _get_type(self, type_str):
        try:
            if type_str == "array" : return ArrayDeque()
            elif type_str == "linked" : return LinkedList()
            else : raise
        except:
            raise InvalidTypeOfList("Invalid type of list(should be 'array' or 'linked')")  

# ====================== PUBLIC FUNCTIONS FOR THE CLASS ====================== #

    def push(self, value):
        self.list_type.push_front(value)

    def pop(self):
        return self.list_type.pop_front()

    def get_size(self):
        return self.list_type.get_size()