#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Dictionary:
    def __init__(self):
        self.inner_size = 10
        self.array = [None] * self.inner_size
        self.count = 0

    def isfull(self):
        for i in range(self.inner_size):
            if self.array[i] is None:
                return False
        return True
    
    def add(self, key, value):
        index = hash(key) % self.inner_size
        if self.isfull():
            self.inner_size = self.inner_size * 2
            temp = self.array
            self.array = [None] * self.inner_size
            for item in temp:
                self.add(item[0], item[1])
        if self.array[index] is None:
            self.array[index] = []
            self.array[index].append((key, value))
        else:
            for keyValuePair in self.array[index]:
                if keyValuePair[0] == key:                    
                    keyValuePair[0] = value
                    return
            self.array[index].append((key, value))
        self.count += 1
        if self.getLoadFactor() > 0.75:
            print("self.loadfactor", self.getLoadFactor())
            self.rehash()
            
    def rehash(self):
        self.inner_size *= 2
        temp = []
        for cell in self.array:
            if cell is not None:
                for keyValue in cell:
                    temp.append(keyValue)
        self.array = [None] * self.inner_size
        self.count = 0
        for keyValue in temp:
            self.add(keyValue[0], keyValue[1])        
    
    def getLoadFactor(self):
        return self.count / self.inner_size
        
    def __hash__(self):
        return -12
    
    def get(self, key):
        index =  hash(key) % self.inner_size
        if self.array[index] is None:
            raise KeyError("Key not found")
        for keyValuePair in self.array[index]:
            if keyValuePair[0] == key:
                return keyValuePair[1]
        raise KeyError("Key not found")
            


# In[18]:


diction = Dictionary()
diction.add("One", 1)
diction.add("Two", 2)
diction.add("Three", 3)
diction.add("Four", 4)
diction.add("Five", 5)
diction.add("Six", 6)
diction.add("Seven", 7)
diction.add("Eight", 8)
diction.add("Nine", 9)
print(diction.get("One"))
print(diction.get("Two"))
print(diction.get("Three"))
print(diction.get("Four"))
print(diction.get("Five"))
print(diction.get("Six"))
print(diction.get("Seven"))
print(diction.get("Eight"))
print(diction.get("Nine"))
print(diction.getLoadFactor())


# In[ ]:





# In[ ]:




