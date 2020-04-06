class Node:

    def __init__(self, data = None, parend = None):
        self.data = data
        self.parend = parends
        self.left = None
        self.right = None


class BinHeapTree:

    def __init__(self, root = None):
        self.root = Node(root)
        self.last = self.root.left

    def add(self, value):
        
        if self.last == self.last.parend.left:
            Node(value, self.last.parend)
            self.last = self.last.parend.right
        elif self.last == self.last.parend.right:
            Node(value, self.last.parend)
            self.last = self._find_next_last_rec()

    def _find_next_last_rec(self, Position):

        if Position == Position.parend.right:
            pass