class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self, value):
        self.stack.pop(value)

    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        for element in self.stack:
            print(element)
        
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()

s.pop(3)
s.display()

print('------------')
last = s.peek()
print(last)

is_empty = s.is_empty()
print(is_empty)