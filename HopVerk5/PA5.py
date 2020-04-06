class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class Bucket_node:

    def __init__(self, key = None, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next

# ============== Bucket Class ==============
class Bucket:

    def __init__(self):
        self.head = None
        self.pointer = None
        self.size = 0

    def insert(self, key, data):
        '''Adds this value pair to the collection'''

        if self.size == 0:
            self.size += 1
            new_node = Bucket_node(key, data)
            self.head = new_node
            self.pointer = self.head
        else:
            if self._check_key(key, self.head): # Retruns true if the key is in the collection
                raise ItemExistsException()
            else:
                self.size += 1
                self.pointer.next = Bucket_node(key, data)
                self.pointer = self.pointer.next

    def update(self, key, data):
        '''Sets the data value of the value pair with equal key to data'''

        if self._check_key(key, self.head): # Retruns true if the key is in the collection
            self._update(key, data, self.head)
        else:
            raise NotFoundException()

    def find(self, key):
        '''Returns the data value of the value pair with equal key'''

        if self._check_key(key, self.head):
            return self._get_data(key, self.head)
        else:
            raise NotFoundException()

    def contains(self, key):
        '''Returns True if equal key is found in the collection, otherwise False'''

        if self._check_key(key, self.head):
            return True
        return False

    def remove(self, key):
        '''Removes the value pair with equal key form the collection'''

        if self._check_key(key, self.head):
            self.size -= 1
            self._remove_node(key, self.head)
        else:
            raise NotFoundException()

    def __setitem__(self, key, data):
        '''Adds or updates to the data structure'''

        if self._check_key(key, self.head):
            self._update(key, data, self.head)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        '''Returns the data value of the value pair with equal key'''

        return self.find(key)

    def __len__(self):
        '''Returns the number of items in the entire data structure'''

        return self.size

# ------- Helper Functions -------

    def _check_key(self, key, node):
        '''Function that returns true if the key already in collection'''
        if node == None: # Base case
            return False
        elif node.key == key:
            return True
        else:
            return self._check_key(key, node.next)

    def _update(self, key, data, node):
        '''Updates the data of given key value'''
        if node.key == key:
            node.data = data
        else:
            self._update(key, data, node.next)

    def _get_data(self, key, node):
        '''Returns the data of given key'''
        if node.key == key:
            return node.data
        else:
            return self._get_data(key, node.next)

    def _remove_node(self, key, node):
        '''Removes the node with the given key'''
        if node == self.head: # Edge case
            self.head = self.head.next
        elif node.next.key == key: # Base case
            node.next = node.next.next
        else:
            self._remove_node(key, node.next)

# ============== HashMap Class ==============
class HashMap:

    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.array = [Bucket() for _ in range(self.capacity)]
        self.size = 0

    def insert(self, key, data):
        '''Adds this value pair to the collection'''
        if self.size > self.capacity * 1.2:
            self._rebuild()

        if self.contains(key):
            raise ItemExistsException()
        else:
            bucket = self._find_empty_bucket()
            self.size += 1
            bucket[key] = data

    def update(self, key, data):
        '''Sets the data value of the value pair with equal key to data'''

        if self.contains(key):
            raise NotFoundException()
        else:
            for bucket in self.array:
                if bucket.contains(key):
                    bucket.update(key, data)

    def find(self, key):
        '''Returns the data value of the value pair with equal key'''

        for bucket in self.array:
            if self.contains(key):
                return bucket.find(key)

    def contains(self, key):
        '''Returns True if equal key is found in the collection, otherwise False'''

        for bucket in self.array:
            if bucket.contains(key):
                return True
        return False

    def remove(self, key):
        '''Removes the value pair with equal key form the collection'''

        if self.contains(key):
            self.size -= 1
            for bucket in self.array:
                if bucket.contains(key):
                    bucket.remove(key)
        else:
            raise NotFoundException()

    def __setitem__(self, key, data):
        '''Adds or updates to the data structure'''

        if self.contains(key): # If key found update it else add it
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        '''Returns the data value of the value pair with equal key'''

        if self.contains(key):
            return self.find(key)
        else:
            raise NotFoundException()

    def __len__(self):
        '''Returns the number of items in the entire data structure'''
        return self.size

# ------- Helper Functions -------

    def _rebuild(self):
        '''Doubles the capacity of the Hash map'''
        self.capacity = self.capacity * 2
        new_array = [Bucket() for _ in range(self.capacity)]

        for i in range(self.capacity / 2):
            new_array[i] = self.array[i]
        self.array = new_array

    def _find_empty_bucket(self):
        '''Checks the array and finds a bucket with 0 or 1 items'''
        for bucket in self.array:
            if len(bucket) == 0:
                return bucket
            elif len(bucket) == 1:
                output_bucket = bucket

        return output_bucket


# ============== MyHashableKey Class ==============
class MyHashableKey:

    def __init__(self, int_value, string_value, capacity = 4):
        self.int = int_value
        self.str = string_value
        self.capacity = capacity

    def __eq__(self, other):
        '''Compares two instances of MyHashableKey and returns True if their values are equal, otherwise False'''
        if self.__hash__() == other.__hash__():
            return True
        return False

    def __hash__(self):
        '''Hashing with a formula'''
        # Formula h(k) = ((a*k + b)
        # a and b are random numbers

        a = 3
        b = 7
        k = self._make_k()
        return ((a*k + b))

# ------- Helper Functions -------

    def _make_k(self):
        '''Makes a number out of the given number and string'''
        # First number tell the lenght of the given number, the number is add behind, then the lenght of 
        # Given string, the character ord values are added in oreder after that.
        output_str = str(len(str(self.int))) + str(self.int) + str(len(self.str))
        for ch in self.str:
            output_str += str(ord(ch))
        return int(output_str)
