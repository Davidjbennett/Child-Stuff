"""Pointer and Courselist are datastructures used to hold data. It is a
Ordered Linked List"""
class CourseList:
    """Courselist is a ordered linked list type used to hold courses"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, dataval):
        """Inserts a course into the courselist in order of class number"""
        # point = Pointer(dataval)
        if self.head is None:
            self.head = dataval
            self.tail = self.head
        elif self.head.course_num >= dataval.course_num:
            self.head = self.__set_links(None, dataval, self.head)
        elif self.tail.course_num <= dataval.course_num:
            self.tail = self.__set_links(self.tail, dataval, None)
        else:
            current = self.head
            while current.course_num < dataval.course_num:
                current = current.next
            self.__set_links(current.prev, dataval, current)
        self.count += 1
        current=self.head

    def remove(self, number):
        """Removes a course according to number parameter"""
        current = self.head
        if number >= self.head.course_num and number <= self.tail.course_num:
            while current.next is not None and current.course_num != number:
                current = current.next
            if current.course_num == number:
                self.__remove_item(current)

    def remove_all(self, number):
        """Removes all courses with specified class number"""
        current = self.head
        while current.next is not None:
            if current.course_num == number:
                self.__remove_item(current)
            current = current.next

    def find(self, number):
        """finds first occurence of number in courselist"""
        current = self.head
        if number >= self.head.course_num and number <= self.tail.course_num:
            while current.next is not None and current.course_num != number:
                current = current.next
            if current.course_num == number:
                return current
        return -1

    def size(self):
        """returns size of courselist"""
        return self.count

    def calculate_gpa(self):
        """Calculates and returns gpa of courses in courselist"""
        if self.head != None:
            current = self.head
            total_grade_points = 0.0
            total_credits = 0.0
            while current is not None:
                total_grade_points += current.gpa * current.course_credits
                total_credits +=  current.course_credits
                current = current.next
            return total_grade_points/total_credits
        return 0.0

    def is_sorted(self):
        """returns true if list is sorted and false otherwise"""
        current = self.head
        if current is None:
            return True
        while current.next is not None:
            if current.course_num > current.next.course_num:
                return False
            current = current.next
        return True

    def __str__(self):
        """returns list as a string"""
        string = ""
        current = self.head
        while current is not None:
            string += str(current) + "\n"
            current = current.next
        return string

    def __iter__(self):
        """iterates through courselist items"""
        current = self.head
        while current != None:
            yield current
            current = current.next

    def __set_links(self, before, item, after):
        """Helper method that sets new links when courselist is changed"""
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
        """Helper function that removes an item and sets new links in courselist"""
        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.prev
        self.__set_links(current.prev, None, current.next)
        self.count -= 1
