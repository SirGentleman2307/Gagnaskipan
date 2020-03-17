
import sys
from enum import Enum
import operator

class DivisionByZero(Exception):
    pass

class UnknownInTree(Exception):
    pass

class OutputFormat(Enum):
    PREFIX = 0
    INFIX = 1
    POSTFIX = 2

class TreeNode:
    def __init__(self, value = None, parent = None, left = None, right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class PrefixParseTree:
    def __init__(self):
        self.root = None
        self.current = None

        self.format = 0

        self.operations = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}

    def load_statement_string(self, statement):
        '''Takes the given statement and makes a binary tree out off it'''
        if statement == None:
            return None

        for item in statement.split():

            if self.root == None:
                self.root = TreeNode(item)
                self.Prefix = statement
                self.current = self.root

            elif item in ['+','-','*','/']:
                if self.current.left: # If there is something in current left set the incoming to the right
                    self.current.right = TreeNode(item, self.current)
                    self.current = self.current.right
                else:   # Put the current item the right
                    self.current.left = TreeNode(item, self.current)
                    self.current = self.current.left # Go to the left

            else: # If the item is a int or str
                if self.current.left:
                    self.current.right = TreeNode(item, self.current)

                    while self.current.left and self.current.right:
                        if self.current.parent: # If current parent is none don't move current (already at the root of tree)
                            self.current = self.current.parent
                        else:
                            break
                else:
                    self.current.left = TreeNode(item, self.current)

    def set_format(self, out_format):
        '''Sets the output format according to the given format'''
        self.format = out_format.value

    def root_value(self):
        return str(self._get_root_value(self.root))

    def simplify_tree(self):
        '''Simplifys the tree'''
        self._simplify_tree(self.root)

    def solve_tree(self, root_value):
        '''Solves current tree with given root value'''
        # The solve uses the prefix to solve, we know that the tree only has
        #  one unknow value and only one node with value as a operator for each level down
        #  the tree. There are only 4 cases we need to look for:
        #  node value == '+' and (node left == 'x' or node right == 'x'),
        #  node value == '-' and (node left == 'x' or node right == 'x').

        self.simplify_tree() # Start with simplifing the tree
        prefix_solve =  self._solve_tree(self.root, str(root_value)) # Get the solve prefix 
        Solved_tree = PrefixParseTree() # Make a solve tree
        Solved_tree.load_statement_string(prefix_solve) # Load solve prefix
        return Solved_tree.root_value() # Return the root value of the solve tree

    def __str__(self):
        '''Returns string that according to the current format'''
        if self.format == 0:
            return self._get_str_prefix(self.root)
        elif self.format == 1:
            return self._get_str_infix(self.root)
        elif self.format == 2:
            return self._get_str_postfix(self.root)

    # ----- Recursive functions ----

    def _get_str_prefix(self, node):
        '''Retruns string in the prefix format, recursively'''
        if node.value in ['+','-','*','/']:
            left = self._get_str_prefix(node.left)
            right = self._get_str_prefix(node.right)
            return '{} {} {}'.format(node.value, left, right)
        else:
            return str(node.value)

    def _get_str_infix(self, node):
        '''Retruns string in the infix format, recursively'''
        if node.value in ['+','-','*','/']:
            left = self._get_str_infix(node.left)
            right = self._get_str_infix(node.right)
            return '({} {} {})'.format(left, node.value, right)
        else:
            return str(node.value)

    def _get_str_postfix(self, node):
        '''Retruns string in the postfix format, recursively'''
        if node.value in ['+','-','*','/']:
            left = self._get_str_postfix(node.left)
            right = self._get_str_postfix(node.right)
            return '{} {} {}'.format(left, right, node.value)
        else:
            return str(node.value)

    def _get_root_value(self, node):
        '''Returns the value of the tree, recursively, rises errors if division by zero happens or there is a unknown in tree'''
        if node == None:
            return None

        if node.value in ['+','-','*','/']:
            left = self._get_root_value(node.left)
            right = self._get_root_value(node.right)

            if node.value == '/' and right == 0:
                raise DivisionByZero()

            return self.operations[node.value](left, right)
        else:
            try:
                return int(node.value)
            except:
                raise UnknownInTree()

    def _simplify_tree(self, node):
        '''Simplifys the tree, recursively'''
        if node.value in ['+','-','*','/']: # Only need to check nodes with value that are an opertation

            if node.left.value in ['+','-','*','/']: # Check left and right values
                self._simplify_tree(node.left)
            if node.right.value in ['+','-','*','/']:
                self._simplify_tree(node.right)

            if node.value == '/' and node.right.value == 0: # Check if division by zero happens
                raise DivisionByZero

            try:
                node.value = str(self.operations[node.value](int(node.left.value), int(node.right.value))) # Change node value 
                node.left, node.right = None, None
                return None
            except:
                return None

            if (node.left and node.right) == None:
                return None

    def _solve_tree(self, node, prefix_solve = ''):
        '''Returns prefix string that solves the tree, recursivley'''
        if node.value == '+': # Check the operator in use
            if node.left.value == 'x': # Check if node left/right is 'x', if so we return the prefix_solve
                return '{} {} {}'.format('-', prefix_solve, node.right.value)
            elif node.right.value == 'x':
                return '{} {} {}'.format('-', prefix_solve, node.left.value)

            elif node.left.value.isdigit(): # Check if left/right is the digit other one is a operator
                prefix_solve = '{} {} {}'.format('-', prefix_solve, node.left.value)
                self._solve_tree(node.right, prefix_solve)
            elif node.right.value.isdigit():
                prefix_solve = '{} {} {}'.format('-', prefix_solve, node.right.value)
                self._solve_tree(node.left, prefix_solve)

        elif node.value == '-': # Check the operator in use
            if node.left.value == 'x': # Check if node left/right is 'x', if so we return the prefix_solve
                return '{} {} {}'.format('+', prefix_solve, node.right.value)
            elif node.right.value == 'x':
                return '{} {} {}'.format('-', node.left.value, prefix_solve)

            elif node.left.value.isdigit():
                prefix_solve = '{} {} {}'.format('-', node.left.value, prefix_solve)
                self._solve_tree(node.right, prefix_solve)
            elif node.right.value.isdigit():
                prefix_solve = '{} {} {}'.format('+', prefix_solve, node.right.value)
                self._solve_tree(node.left, prefix_solve)

