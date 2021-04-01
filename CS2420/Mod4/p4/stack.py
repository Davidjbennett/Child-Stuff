"""data structure which if first in last out structure"""
class Stack:
    """Initializer. Takes no params"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Adds an item on to the stack"""
        self.items.append(item)

    def pop(self):
        """removes and returns last item from non empty stack"""
        if self.isEmpty():
            raise IndexError()
        return self.items.pop()

    def top(self):
        """returns last item from stack without removing"""
        if self.isEmpty():
            raise IndexError()
        return self.items[-1]

    def size(self):
        """returns size of the stack"""
        return len(self.items)

    def clear(self):
        """clears entire stack"""
        self.items.clear()

    def isEmpty(self):
        """returns true if stack is empty"""
        return self.items == []
