

class Stack:

    def __init__(self, input_list = []):
        self.stack = input_list

    def pop(self):
        self.stack = self.stack[:-1]

    def push(self, input):
        self.stack.append(input)

    def __str__(self):
        return ', '.join(self.stack)

next = Stack(['t','d','a','d','o','e'])


next.pop()
print(next)
next.pop()
print(next)
next.pop()
print(next)
next.push('o')
print(next)
next.pop()
print(next)
next.push('p')
print(next)
next.push('q')
print(next)
next.pop()
print(next)
next.pop()
print(next)
next.pop()
print(next)
next.pop()
print(next)
next.push('f')
print(next)
next.push('g')
print(next)
next.push('h')
print(next)
next.pop()
print(next)
next.pop()
print(next)
next.pop()
print(next)
next.push('j')
print(next)
next.pop()
print(next)
next.pop()