# from course import *

class Pointer:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None
        self.prev = None


class CourseList:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def info(self):
        print(self.first.dataval.number())
        # print(self.first.dataval)

    def insert(self, dataval):
        point = Pointer(dataval)
        if self.first == None:
            self.first = point
            self.last = self.first
        elif self.first.dataval.number() >= dataval.number():
            self.first = self.__set_links(None, point, self.first)
        elif self.last.dataval.number() <= dataval.number():
            self.last = self.__set_links(self.last, point, None)
        else:
            current = self.first
            while current.dataval.number() < point.dataval.number():
                current = current.next
            self.__set_links(current.prev, point, current)
        self.count += 1
              
         
    def remove(self, number):
        if number != None:
            if number >= self.first.dataval.number() and number <= self.last.dataval.number():
                current = self.first
                while current.dataval.number() != number and current.next != None:
                    current = current.next
                if current.dataval.number() == number:
                    self.__remove_item(current)
                
    def remove_all(self, number):
        #!can i use a for loop on courselist in courselist?
        pass

    def find(self, number):
        current = self.first
        if number >= self.first.dataval.number() and number <= self.last.dataval.number():
            while current.next != None:
                if current.dataval.number() == number:
                    return current.dataval
        return -1

    def size(self):
        return self.count

    def calculate_gpa(self):
        gpas = 0
        count = 0
        current = self.first
        while current.next != None:
            gpas += current.dataval.grade()
            count += 1
            current = current.next
        return (gpas/count)

    def is_sorted(self):
        current = self.first
        while current.next != None:
            if current.dataval.number() > current.next.dataval.number():
                return False
            else:
                current = current.next
        return True
    
    def __str__(self):
        string = ""
        current = self.first
        while current != None:
            string += str(current.dataval) + "\n"
            current = current.next
        return string

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current
            current = current.next

    def __set_links(self, before, item, after):
        if item == None:
            if before != None:
                before.next = after
            if after != None:
                after.prev = before
        else:
            if before != None:
                before.next = item
            if after != None:
                after.prev = item
            item.prev = before
            item.next = after
        return item

    def __remove_item(self, current):
        if current == self.first:
            self.first == current.next
        if current == self.last:
            self.last = current.prev
        self.__set_links(current.prev, None, current.next)
        self.count -= 1
