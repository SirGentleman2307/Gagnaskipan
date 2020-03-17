
class TreeNode:
    def __init__(self, name = "", parent = None):
        self.name = name
        self.parent = parent
        self.subs = []

    def add_sub(self, name):
        '''Adds given name as the name of new node'''
        self.subs.append(TreeNode(name, self))

    def names_list(self):
        '''Returns a list of names in sub as str'''
        return [sub.name for sub in self.subs]

def run_commands_on_tree(tree):
    '''Get's input from user and executes that command if possible'''
    print("  current directory: " + tree.name)
    while True:
        user_input = input()
        command = user_input.split()

        if len(command) == 1 and command[0] != 'ls': # Safeguard for if the user dosn't input a second command
            print('Second input missing !!!')
            continue

        name_list = tree.names_list()   # Function call 'names_list' returns a list of names of nodes in tree [str]
        # Use by all of the commends except 'mkdir'

        if command[0] == "mkdir": # Make Directory
            print("  Making subdirectory " + command[1])

            if make_sub_dir(tree, command[1]): # Function call 'make_sub_dir' returns True if subdirectory already exists
                print("  Subdirectory with same name already in directory")

        elif command[0] == "ls": # Print out all subd at current node
            print("  Listing the contents of current directory,  " + str(tree.name))
            print('\n'.join(sorted(name_list))) # Sorts then joins the list

        elif command[0] == "cd": # Change current directory
            print("  switching to directory " + command[1])

            if command[1] == "..": # Go up one
                if tree.parent: # If parant is not None
                    tree = tree.parent
                else:
                    print("Exiting directory program")
                    break
            else:
                if command[1] not in name_list:
                    print("  No folder with that name exists")
                else:
                    index = name_list.index(command[1]) # Get the index corresponding to the command
                    tree = tree.subs[index] # switch to the new directory

            print("  current directory: " + str(tree.name))

        elif command[0] == "rm": # Remove current directory
            print("  removing directory " + command[1])

            if command[1] in name_list: # If the command is in list
                index = name_list.index(command[1]) # Get the index corresponding to the command
                tree.subs.pop(index) # Remove that index
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")

def make_sub_dir(tree, dir_name):
    '''Function used to make/add to the sub of current tree node'''
    if dir_name in tree.names_list(): # Function call 'names_list' returns a list of names of nodes in tree [str]
        return True
    else:
        tree.add_sub(dir_name) # Function call 'add_sub' that adds new node to tree
        return False

def run_directories_program():
    run_commands_on_tree(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
