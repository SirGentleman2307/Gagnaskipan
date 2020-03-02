class Tracker:
    ''' Class that holds information on the leading element we want to inspect in a list '''
    def __init__(self, current_head):
        ''' Make current_head be the current leading Node that we inspect witht the current last node '''
        self.current_head = current_head
    
    def get_data(self):
        return self.current_head.data

    def next(self):
        self.current_head = self.current_head.next

# ====================== PALINDROME FUNCTIONS ====================== #

def palindrome(head):
    tracker = Tracker(head) # Let's track the first node of the list 
    return palindrome_recursive(tracker, head)

def palindrome_recursive(tracker, head):
    ''' Recursive function that checks if a list is a palindrome '''
    if head.next != None:
        # Recursive until we reach the end (when head.next == None)
        is_palindrome = palindrome_recursive(tracker, head.next)
        # is_palindrome is a saftey net for if we detect that it is not a palindrome
        if not is_palindrome:
            return False
    if head.data == tracker.get_data():
        # If the data matches with the leading node and the node on the opposite side
        tracker.next() # Change the next leading node
        return True # Returns to line 31, where head retracts back
    else:
        return False # Not a palindrome