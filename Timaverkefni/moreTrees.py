

class Node:
    def __init__(self, name = '', list_kids = [], father = ''):
        self.name = name
        self.kids = list_kids
        self.father = father

class Tree:
    def __init__(self, root = None):
        self.root = root

    def _populate_rec(self):
        data_str = str(input('Enter in data: '))
        if data_str == '':
            return None
        left = self._populate_rec()
        right = self._populate_rec()
        list_kids = [left, right]
        return Node(data_str, list_kids)

    def add_branch(self):
        self.root = self._populate_rec()

    def _print_tree_rec(self, node):
        if node == None:
            return
        print(node.name, end= ' ')
        for kid in node.kids:
            self._print_tree_rec(kid)

    def print_tree(self):
        self._print_tree_rec(self.root)

    def _print_posterder_rec(self, node):
        if node == None:
            return
        for kid in node.kids:
            self._print_posterder_rec(kid)
        print(node.name, end= ' ')

    def print_postorder(self):
        self._print_posterder_rec(self.root)

if __name__ == '__main__':
    BT = Tree()
    BT.add_branch()
    BT.print_tree()
    BT.print_postorder()
