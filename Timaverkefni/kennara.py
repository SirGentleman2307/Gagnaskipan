
class Node:
    def __init__(self, value = None, parent = None, left = None, right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
        self.last = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
            self.last = self.root
        elif self.root is self.last:
            self.root.last = Node(value, self.root)
            self.last = self.root.left
        elif self.last is self.last.parent.left:
            self.last.parent.right = Node(value, self.last.paremt)
            self.last = self.last.parent.right
        else:
            temp = self.last
            while True:
                if temp is self.root :
                    break
                if temp is temp.parent.left:
                    break
                temp = temp.parent
            if temp is not self.root:
                temp = temp.parent.right
            while temp.left is not None:
                temp = temp.left
            temp = Node(value, temp.parent)
        temp = self.last

        while True:
            if temp.parent == None:
                break
            if temp.data > temp.parent.data:
                break
            temp.data, temp.parent.data = temp.parent.data, temp.data
            temp = temp.parent