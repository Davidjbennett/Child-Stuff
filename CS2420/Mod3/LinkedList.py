class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None

    def recursiveAppend(self, dataval):
        if self.next == None:
            self.next = Node(dataval)
        else:
            self.next.recursiveAppend(dataval)

    def __str__(self):
        return str(self.dataval)

class My_List:
    def __init__(self):
        self.first = None
        self.last = None
        self.prev = None

    def add(self, dataval):
        if (self.first == None):
            self.first = Node(dataval)
            self.last = self.first
        else:
            item = Node(dataval)
            item.next = self.first
            self.first = item
    
    def index(self, item):
        index = 0
        while index <= self.length():
            if self.get(index).dataval == item:
                return index
            index += 1
        return -1

    def remove(self, item):
        index = self.index(item)
        if self.last == self.first:
            self.last = None
            self.first = None
        if index == 0:
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

    def search(self, item):
        pass

    def append(self, dataval):
        if self.first == None:
            self.first = Node(dataval)
            self.last = self.first
        else:
            new_item = Node(dataval)
            self.last.next = new_item
            new_item.prev = self.last
            self.last = new_item
            new_item.next = None
            # item = self.first
            # while item.next != None:
            #     item = item.next
            # item.next = Node(dataval)

    def get(self, index):
        current = 0
        if index >= self.length() and index < 0:
            return None
        item = self.first
        while current < index:
            item = item.next
            current += 1
        return item

    def __len__(self):
        return self.length()

    def recursiveAppend(self, dataval):
        if self.first == None:
            self.first = Node(dataval)
        else:
            self.first.recursiveAppend(dataval)
    
    def isEmpty(self):
        return self.first == None

    def length(self):
        result = 0
        if self.first == None:
            return result
        item = self.first
        result += 1
        while item.next != None:
            item = item.next
            result += 1
        return result

    # def pop(self):
    #     last = self.last
    #     self.remove(self.last.dataval)
    #     last = self.get(self.length() - 1)
    #     self.remove(last.dataval)
    #     return last
    
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


def main():
    my_list = My_List()

    print(my_list)

    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    my_list.add(4)
    my_list.add(5)
    my_list.add(6)
    print(my_list)

    my_list.remove(4)
    print(my_list)

    item = my_list.pop()
    print(item)
    print(my_list)
    # print(my_list.get(1))

    my_list.recursiveAppend(13)
    my_list.recursiveAppend(11)
    my_list.recursiveAppend(9)
    print(my_list)

if __name__ == "__main__":
    main()
