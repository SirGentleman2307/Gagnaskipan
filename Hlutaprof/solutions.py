# Hlutapróf 1, Kristján Már Kjartansson
# Kt: 2307993349

## ------------ Part A ------------ 
def count_values(a_list):

    counter_dic = {}
    for element in a_list:      # Iterate over the list

        if element not in counter_dic.keys():   # If elemet is not a key, make it
            counter_dic[element] = 1
        else:                                   # Else add 1
            counter_dic[element] += 1

    for key, value in counter_dic.items():      # Print all
        print('{}: {}'.format(key,value))


## ------------ Part B ------------ 
class ValueCounter:

    def __init__(self):
        '''Too parameters a_list and dict'''
        self.__list = []
        self.__dic = {}

    def set_items(self, a_list):
        '''Input: List of elements to be counted
        Saves the count in a dict, where the keys are the elements in the list and values are the count of element'''
        self.__list = a_list

        for element in a_list:      # Iterate over the list

            if element not in self.__dic.keys():    # If elemet is not a key, make it
                self.__dic[element] = 1
            else:                                   # Else add 1
                self.__dic[element] += 1

    def print_count(self):
        '''Prints out all keys and values from the dict'''
        for key, value in self.__dic.items():
            print('{}: {}'.format(key, value))

