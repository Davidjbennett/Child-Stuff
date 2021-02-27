class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.dataval)
    
class MyList:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, dataval):
        if (self.first == None):
            self.first = Node(dataval)
            self.last = self.first
        else:
            temp = Node(dataval)
            temp.next = self.first
            self.first = temp

    def index(self, item):
        index = 0
        while index < self.length():            
            if self.get(index).dataval == item:                
                return index
            index += 1
        return -1
    
    def remove(self, item):
        index = self.index(item)        
        if self.last == self.first:
            self.last = None
            self.first = None
        elif index == 0:            
            temp = self.first.next
            self.first.next = None
            self.first = temp
        elif index > 0:
            oneBefore = self.get(index - 1)            
            temp = oneBefore.next
            if self.last == temp:
                self.last = oneBefore
            oneBefore.next = temp.next
            temp.next = None
            
    def append(self, dataval):
        if (self.first == None):
            self.first = Node(dataval)
            self.last = self.first
        else:
            newItem = Node(dataval)
            self.last.next = newItem
            newItem.prev = self.last
            self.last = newItem
            newItem.next = None
    
    def get(self, index):
        current = 0
        if index >= self.length() and index < 0:
            return None
        
        item = self.first
        while (current < index):
            item = item.next
            current += 1
        return item        
    
    def __len__(self):
        return self.length()
    
    def isEmpty(self):
        return self.first == None        
        
    def length(self):
        result = 0
        if (self.first == None):
            return result
        
        item = self.first
        result += 1
        while (item.next != None):
            item = item.next
            result += 1
        return result
    
    def pop(self):
        last = self.last
        self.remove(self.last.dataval)
        return last
        
    def __str__(self):
        if (self.first == None):
            return "empty"
        
        result = str(self.first.__str__())
        item = self.first
        while (item.next != None):
            item = item.next
            result = str(result) + str(",") + str(item.__str__())
        return result
    