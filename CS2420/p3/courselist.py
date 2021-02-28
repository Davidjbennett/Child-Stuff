"""Pointer and Courselist are datastructures used to hold data. It is a
Ordered Linked List"""
class Pointer:
    """Pointer holds data and points to the next and previous data pieces"""
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None
        self.prev = None


class CourseList:
    """Courselist is a ordered linked list type used to hold courses"""
    
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
    # A method that i was using
    # def info(self):
    #     print(self.first.dataval.number())
    #     # print(self.first.dataval)

    def insert(self, dataval):
        """Inserts a course into the courselist in order of class number"""
        point = Pointer(dataval)
        if self.first is None:
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
        """Removes a course according to number parameter"""
        current = self.first
        if number >= self.first.dataval.number() and number <= self.last.dataval.number():
            while current.next is not None and current.dataval.number() is not number:
                current = current.next
            if current.dataval.number() == number:
                self.__remove_item(current)

    def remove_all(self, number):
        """Removes all courses with specified class number"""
        current = self.first
        while current.next is not None:
            if current.dataval.number() == number:
                self.__remove_item(current)
            current = current.next

    def find(self, number):
        """finds first occurence of number in courselist"""
        current = self.first
        if number >= self.first.dataval.number() and number <= self.last.dataval.number():
            while current.next is not None and current.dataval.number() is not number:
                current = current.next
            if current.dataval.number() == number:
                return current.dataval
        return -1

    def size(self):
        """returns size of courselist"""
        return self.count

    def calculate_gpa(self):
        """Calculates and returns gpa of courses in courselist"""
        if self.first is not None:
            current = self.first
            total_grade_points = 0.0
            total_credits = 0.0
            while current.next is not None:
                total_grade_points += current.dataval.grade() * current.dataval.credit_hr()
                total_credits +=  current.dataval.credit_hr()
                current = current.next
            return total_grade_points/total_credits

    def is_sorted(self):
        """returns true if list is sorted and false otherwise"""
        current = self.first
        while current.next is not None:
            if current.dataval.number() > current.next.dataval.number():
                return False
            current = current.next
        return True

    def __str__(self):
        """returns list as a string"""
        string = ""
        current = self.first
        while current is not None:
            string += str(current.dataval) + "\n"
            current = current.next
        return string

    def __iter__(self):
        """iterates through courselist items"""
        current = self.first
        while current is not None:
            yield current
            current = current.next

    def __set_links(self, before, item, after):
        """Helper method that sets new links when courselist is changed"""
        if item is None:
            if before is not None:
                before.next = after
            if after is not None:
                after.prev = before
        else:
            if before is not None:
                before.next = item
            if after is not None:
                after.prev = item
            item.prev = before
            item.next = after
        return item

    def __remove_item(self, current):
        """Helper function that removes an item and sets new links in courselist"""
        if current is self.first:
            self.first = current.next
        if current is self.last:
            self.last = current.prev
        self.__set_links(current.prev, None, current.next)
        self.count -= 1
