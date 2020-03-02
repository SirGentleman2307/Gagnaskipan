class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self, capacity = 4):
        self.__size = 0
        self.__capacity = capacity
        self.__items = [None] * self.__capacity
        self.__ordered = True
        self.__spacing = (0,self.__size)
        self.set_spacing = True

    #Time complexity: O(n) - linear time in size of list     DONE(10)
    def __str__(self):
        ''''''
        output_str = ''
        raw_list = self.__items

        for i in range(self.__size):
            element = raw_list[i]
            if element or element == 0:
                output_str += str(element) + ','
        return output_str[:-1]

    #Time complexity: O(n) - linear time in size of list     DONE(10)
    def prepend(self, value):
        ''''''
        if self.__capacity == self.__size:
            self.resize()

        old_list = self.__items
        new_list = [None] * self.__capacity

        new_list[0] = value
        for i in range(self.__size):
            new_list[i + 1] = old_list[i]
        self.__items = new_list

    #Time complexity: O(n) - linear time in size of list     DONE(10)
    def insert(self, value, index):
        ''''''
        if index > self.__size + 1 or index < 0:
            raise IndexOutOfBounds('Index out of bounds!')

        if self.__capacity == self.__size:
            self.resize()

        old_list = self.__items
        new_list = [None] * self.__capacity

        for i in range(self.__capacity):
            if i >= index:
                if i == index:
                    self.__size += 1
                    new_list[i] = value
                    i += 1
                new_list[i] = old_list[i - 1]
            else:
                new_list[i] = old_list[i]
        self.__items = new_list

    #Time complexity: O(1) - constant time                   DONE(10)
    def append(self, value):
        ''''''
        if self.__capacity == self.__size:
            self.resize()

        self.__items[self.__size] = value
        self.__size += 1

    #Time complexity: O(1) - constant time                   DONE(10)
    def set_at(self, value, index):
        ''''''
        if index > self.__size + 1:
            raise IndexOutOfBounds('Index out of bounds!')
        else:
            self.__items[index - 1] = value

    #Time complexity: O(1) - constant time                   DONE(10)
    def get_first(self):
        ''''''
        if self.__size == 0:
            raise Empty('List is empty!')
        else:
            return self.__items[0]

    #Time complexity: O(1) - constant time                   DONE(10)
    def get_at(self, index):
        ''''''
        if index > self.__size:
            raise IndexOutOfBounds('Index out of bounds!')
        else:
            return self.__items[index]

    #Time complexity: O(1) - constant time                   DONE(10)
    def get_last(self):
        ''''''
        return self.__items[self.__size]

    #Time complexity: O(n) - linear time in size of list     DONE
    def resize(self):
        ''''''
        old_capacity = self.__capacity
        new_capacity = old_capacity * 2
        self.__capacity = new_capacity

        old_list = self.__items
        new_list = [None] * self.__capacity

        for i in range(self.__size):
            new_list[i] = old_list[i]
        self.__items = new_list

    #Time complexity: O(n) - linear time in size of list     DONE
    def remove_at(self, index):
        ''''''
        if index > self.__size or index < 0:
            raise IndexOutOfBounds('Index out of bounds!')

        if self.__capacity == self.__size:
            self.resize()

        old_list = self.__items
        new_list = [None] * self.__capacity

        for i in range(self.__capacity):
            if i < index:
                new_list[i] = old_list[i]
            if i == index:
                continue
            if i > index:
                new_list[i - 1] = old_list[i]

        self.__size -= 1
        self.__items = new_list

    #Time complexity: O(1) - constant time                   DONE
    def clear(self):
        ''''''
        self.__size = 0
        self.__capacity = 4
        self.__items = [None] * self.__capacity

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        ''''''
        if self.set_spacing:
            self.set_spacing = False
            self.__spacing = (0,self.__size)


        BOT_INDEX, TOP_INDEX = self.__spacing
        MID_INDEX = BOT_INDEX + ((TOP_INDEX - BOT_INDEX) // 2)

        if MID_INDEX == BOT_INDEX:
            self.set_spacing = True

            if self.__items[MID_INDEX] == value:
                return self.insert(value, MID_INDEX + 1)

            if self.__items[MID_INDEX] < value:
                if self.__items[MID_INDEX + 1] < value:
                    return self.insert(value, MID_INDEX + 2)
                else:
                    return self.insert(value, MID_INDEX + 1)
            else:
                return self.insert(value, MID_INDEX - 1)

        if value < self.__items[MID_INDEX]:
            self.__spacing = BOT_INDEX, MID_INDEX - 1
            return self.insert_ordered(value)

        if value > self.__items[MID_INDEX]:
            self.__spacing = MID_INDEX + 1, TOP_INDEX
            return self.insert_ordered(value)


    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    for i in range(0,16):
        arr_lis.append(i)
    arr_lis.remove_at(7)
    arr_lis.remove_at(11)
    arr_lis.remove_at(8)
    arr_lis.remove_at(3)
    arr_lis.remove_at(5)
    arr_lis.remove_at(2)
    print(str(arr_lis))
    arr_lis.insert_ordered(12)
    arr_lis.insert_ordered(1)
    arr_lis.insert_ordered(1)
    arr_lis.insert_ordered(1)
    arr_lis.insert_ordered(1)
    print(str(arr_lis))


