
class ArrayDeque():

    def __init__(self):
        self.Deque = []
        self.Size = 0

    def push_back(self, data):
        self.Size += 1
        self.Deque.append(str(data))

    def push_front(self, data):
        self.Size += 1
        self.Deque.insert(0,str(data))

    def pop_back(self):
        self.Size -= 1
        if self.Size < 0:
            self.Size = 0
            return None
        else:
            return self.Deque.pop()

    def pop_front(self):
        self.Size -= 1
        if self.Size < 0:
            self.Size = 0
            return None
        else:
            return self.Deque.pop(0)

    def get_size(self):
        return self.Size

    def __str__(self):
        return ' '.join(self.Deque)
