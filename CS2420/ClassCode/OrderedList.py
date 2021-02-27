class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.dataval)
    
class OrderedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
    
    def add(self, dataval):
        if self.isEmpty():
            self.first = Node(dataval)
            self.last = self.first
        elif self.first.dataval > dataval:
            newNode = Node(dataval)
            newNode.next = self.first
            self.first.prev = newNode.next
            self.first = newNode        
        else:
            current = self.first
            
            while current.next != None and current.next.dataval < dataval:
                current = current.next            
            newNode = Node(dataval)
            newNode.next = current.next
            current.next = newNode
            newNode.prev = current
            if (newNode.next != None):
                newNode.next.prev = newNode
            else:
                self.last = newNode
        self.count += 1
    
    #def index(self, item):
    
    #def remove(self, item):
         
    #def search(self, item):
        
    #def append(self, dataval):
    
    def get(self, index):
        if index < 0 or index >= self.count:
            return None        
        if self.isEmpty():
            return None
        else:
            idx = 0
            current = self.first
            while idx < index:                    
                current = current.next
                idx += 1
            return current
    
    #def __len__(self):
    
    def isEmpty(self):
        return self.first == None
        
    def length(self):
        return count
    
    #def pop(self):
        
    #def pop(self, pos):
        
    def __str__(self):
        result = ""
        current = self.first
        while current.next != None:
                result += str(current)
                result += " "
                current = current.next            
        result += str(current)
        return result

