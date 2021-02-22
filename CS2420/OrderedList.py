class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None

    def __str__(self):
        return str(self.dataval)

class ordered_list:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def add(self, dataval):
        if self.isEmpty():
            self.first = Node(dataval)
            self.last = self.first
        elif self.first.dataval > dataval:
            new_node = Node(dataval)
            new_node.next = self.first
            self.first.prev = new_node.next
            self.first = new_node
        else:
            #find where item is > than dataval
            # find where next is none
            current = self.first
            while current.next != None and current.next.dataval < dataval:
                current = current.next
            new_node = Node(dataval)
            new_node.next = current.next
            current.next = new_node
            new_node.prev = current
            if new_node.next != None:
                new_node.next.prev = new_node
            else:
                self.last = new_node
        self.count += 1

    def index(self):
        pass

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


    def isEmpty(self):
        return self.first == None
    
    def __str__(self):
        result = ""
        current = self.first
        while current.next != None:
            result += str(current) + " "
            current = current.next
        result += str(current)
        return result
            

def main():
    lyst = ordered_list()
    lyst.add(2)
    lyst.add(5)
    lyst.add(9)
    lyst.add(23)
    lyst.add(4)
    lyst.add(6)
    print(str(lyst))
    print(lyst.get(1))

if __name__ == "__main__":
    main()
