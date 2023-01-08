class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # prints 3
print(stack.peek())  # prints 2
print(stack.size())  # prints 2
print(stack.is_empty())  # prints False