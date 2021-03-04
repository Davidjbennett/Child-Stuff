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

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

def isPalindrome(string:str) -> bool:
    myQueue = Queue()
    myStack = Stack()
    for i in range(len(string)):
        if string[i].isspace():
            continue
        myStack.push(string[i].lower())
        myQueue.enqueue(string[i].lower())
    
    while myQueue.isEmpty() == False:
        if (myQueue.dequeue() != myStack.pop()):
            return False
        
    return True

print(isPalindrome("taco cat"))
print(isPalindrome("frederick"))
print(isPalindrome("A nut for a jar of tuna"))

stack = Stack()

print(stack.isEmpty())
print(stack.size())

stack.push(89)
stack.push(74)
stack.push(32)

print(stack.peek())
        