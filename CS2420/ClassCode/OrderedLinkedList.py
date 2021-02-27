#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    """A class used to represent a Node in a Doubly Linked List"""
    def __init__(self, value=None):
        """Constructor for the Node class"""
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        """ToString implementation for the Node class"""
        return str(self.value)    


# In[36]:


class OrderedLinkedList:
    """A class containing a list of items linked through references"""
    def __init__(self):
        """Constructor for the LinkedList class"""
        self.first = None
        self.last = None
        self.count = 0

    def __str__(self):
        """ToString implementation for the LinkedList class"""
        result = ""
        current = self.first
        while current != None:
            result += str(current.value)
            result += "\n"
            current = current.next        
        return result
    
    def __iter__(self):
        self.currentIter = self.first
        return self

    def __next__(self):
        if self.currentIter != None:
            self.currentIter = self.currentIter.next
            if self.currentIter == None: 
                raise StopIteration()
            return self.currentIter
        else:
            raise StopIteration()
#         if self.currentIter == None:
#             self.currentIter = self.first
#         elif self.currentIter.next == None:
#             raise StopIteration()
#         else:
#             self.currentIter = self.currentIter.next
#         return self.currentIter
            
#     def __iter__(self):
#         current = self.first
#            while current is not None:
#                 yield current
#                 current = current.next
    
#     def __getitem__(self, key):
#         if key >= self.count:
#             raise IndexError("List index out of range")
#         if key < 0:
#             if (key * -1) > self.count:
#                 raise IndexError("List index out of range")
#             key += 1
#             current = self.last
#             while key < 0:
#                 current = current.prev
#                 key += 1
#             return current
        
#         current = self.first
#         while key > 0:
#             current = current.next
#             key -= 1
#         return current
    
    def insert(self, node):
        """Inserts the specified node in value order"""
        if self.first == None:
            self.first = self.last = node
        elif self.last.value < node.value:
            self.last = self.__set_links(self.last, node, None)            
        elif self.first.value >= node.value:
            self.first = self.__set_links(None, node, self.first)
        else:
            current = self.first
            while current.value < node.value:
                current = current.next
            self.__set_links(current.prev, node, current)
        self.count += 1
            
    def remove(self, number):
        """Removes the first occurrence of the node with the specified value"""
        if number <= self.last.value and number >= self.first.value:
            current = self.first
            while current.value != number and current.next != None:
                current = current.next
            if current.value == number:
                self.__remove_item(current)
                
    def remove_all(self, number):
        """Removes ALL occurrences of nodes with the specified value"""
        current = self.first
        while current.next != None:
            if current.value == number:
                self.__remove_item(current)                
            current = current.next
    
    def find(self, number):
        """Finds the first occurence of the node with the specified value or returns -1 if not found"""
        index = 0
        if number <= self.last.value and number >= self.first.value:
            current = self.first
            while current.value != number and current.next != None:
                current = current.next
                index += 1
            if current.value == number:
                return index
        return -1                
    
    def size(self):
        """Returns the number of items in the list"""
        return self.count
    
    def __remove_item(self, current):
        """Sets all of the links while removing an item"""
        if current == self.first:
            self.first = current.next
        if current == self.last:
            self.last = current.prev
        self.__set_links(current.prev, None, current.next)
        self.count -= 1
        
    def __set_links(self, before, item, after):
        """Sets the links for all three nodes"""
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


# In[37]:


myList = OrderedLinkedList()

myList.insert(Node(3))
myList.insert(Node(1))
myList.insert(Node(4))
myList.insert(Node(1))
myList.insert(Node(5))
myList.insert(Node(9))
myList.insert(Node(2))
myList.insert(Node(6))
myList.insert(Node(5))
myList.insert(Node(3))

print(myList)

for i in myList:
    print(i.value)


# In[ ]:




