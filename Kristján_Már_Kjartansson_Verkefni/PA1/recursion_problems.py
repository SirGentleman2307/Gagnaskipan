# Main Fuctions
def modulus(a, b):
    '''Recursively finds the modulus of a and b'''
    Diff = a - b
    if Diff == 0:
        return 0
    elif Diff < 0:
        return b - (b - a)
    else:
        return modulus(Diff, b)


def how_many(lis1, lis2):

    number_dict = dict()
    count_rec(number_dict, lis1)
    return compare_rec(number_dict, lis2)

# Helper Functions

def count_rec(dic, lis):
    '''Recursively counts items in a given list and stores values in the given dict'''
    if lis == []:   #If list is empty stop recursion
        return None

    Value = lis[0]
    if Value not in dic: # Basic count dictonary
        dic[Value] = 1
    else:
        dic[Value] += 1
    count_rec(dic, lis[1:])

def compare_rec(dic, lis):
    '''Recursively counts how many instances of elements in dict and list'''
    if lis == []:   #If list is empty stop recursion
        return 0

    Value = lis[0]
    if Value in dic:
        count = dic[Value]
    else:
        count = 0
    return count + compare_rec(dic, lis[1:])
