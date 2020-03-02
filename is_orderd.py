def is_ordered(head):
    ''' Function that cheks a singly linked list is ordered, either lowest to highest or highest to lowest '''
    if head.next == None: # Nothing in the list, must be ordered
        return True
    if head.data > head.next.data:
        is_higher = True # highest to lowest
    elif head.data < head.next.data:
        is_higher = False # lowest to highest
    else:
        is_higher = None # equals, could be either one
    return is_ordered_recursive(head, head.next, is_higher)

def is_ordered_recursive(head, next_to_head, is_higher):
    ''' Function that recursively checks if a list is ordered '''
    if next_to_head == None: # We checked all the nodes, it is ordered
        return True
    elif head.data > next_to_head.data and is_higher: # highest to lowest
        return is_ordered_recursive(head.next, next_to_head.next, True)
    elif head.data < next_to_head.data and is_higher == False: # lowest to highest
        return is_ordered_recursive(head.next, next_to_head.next, False)
    elif head.data == next_to_head.data: # if it is equal we save what is_higher was in the last recursion
        return is_ordered_recursive(head.next, next_to_head.next, is_higher)
    else: # Not ordered
        return False