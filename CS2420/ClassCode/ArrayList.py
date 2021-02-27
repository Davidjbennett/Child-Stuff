class ArrayList:
    def __init__(self):
        self.myArray = []
        self.lastIndex = 0
        self.maxSize = 0
        self.sizeExponent = 0
    
    def add(self, value):
        if self.lastIndex > self.maxSize - 1:
            self.__resize__()
        for i in range(self.lastIndex, 0, -1):
            self.myArray[i + 1] = self.myArray[i]
        self.myArray[0] = value
        
    def append(self, value):
        if self.lastIndex > self.maxSize - 1:
            self.__resize__()
        self.myArray[self.lastIndex] = value
        self.lastIndex += 1
        
    def __resize__(self):
        newSize = 2 ** self.sizeExponent
        newArray = [0] * newSize
        for i in range(self.maxSize):
            newArray[i] = self.myArray[i]
        self.maxSize = newSize
        self.myArray = newArray
        self.sizeExponent += 1
    
    def __getitem__(self, index):
        if index > self.lastIndex:
            raise LookupError('Index out of bounds')
        return self.myArray[index]