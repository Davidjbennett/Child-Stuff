class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()

print(stack.isEmpty())
print(stack.size())

stack.push(89)
stack.push(74)
stack.push(32)

print(stack.peek())
        