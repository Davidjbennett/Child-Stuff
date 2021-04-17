'''HashMap class to keep track of key value pairs'''
class HashMap:
    '''HashMap class to keep track of key value pairs'''
    def __init__(self):
        '''initializes key val pair'''
        self.inner_size = 7
        self.array = [None] * self.inner_size
        self.count = 0

    def get(self, key):
        '''returns the keyvaluepair relating to input key'''
        index =  hash(key) % self.inner_size
        if self.array[index] is None:
            raise KeyError("Key not found")
        for key_val_pair in self.array[index]:
            if key_val_pair[0] == key:
                return key_val_pair[1]
        raise KeyError("Key not found")

    def set(self, key, value):
        '''sets keyvaluepair and adds it to hashmap'''
        index = self.hashTuple(key) % self.inner_size
        if self.isfull():
            self.inner_size = self.inner_size * 2
            self.array = [None] * self.inner_size
        if self.array[index] is None:
            self.array[index] = []
            self.array[index].append((key, value))
        else:
            for kvp in range(len(self.array[index])):
                key_val_pair = self.array[index][kvp]
                if key_val_pair[0] == key:
                    self.array[index][kvp] = None
                    self.array[index][kvp] = ((key_val_pair[0], value))
                    return
            self.array[index].append((key, value))
        self.count += 1
        if self.getLoadFactor() >= 0.80:
            self.rehash()

    def getLoadFactor(self):
        '''returns how full the hashmap is'''
        return self.count / self.inner_size

    def rehash(self):
        '''reorders hashmap'''
        self.inner_size = self.inner_size * 2 - 1
        temp = []
        for cell in self.array:
            if cell is not None:
                for key_val in cell:
                    temp.append(key_val)
        self.array = [None] * self.inner_size
        self.count = 0
        for key_val in temp:
            self.set(key_val[0], key_val[1])

    def isfull(self):
        '''returns true if arr is full'''
        for i in range(self.inner_size):
            if self.array[i] is None:
                return False
        return True

    def hashTuple(self, tuple_val):
        '''hashes tuplue and returns value'''
        if tuple_val is tuple:
            return tuple_val[0] ** tuple_val[1]
        return hash(tuple_val)

    def remove(self, key):
        '''removes key val pair from arr'''
        index =  hash(key) % self.inner_size
        if self.array[index] is None:
            raise KeyError("Key not found")
        for key_val_pair in self.array[index]:
            if key_val_pair[0] == key:
                self.array[index] = None

    def clear(self):
        '''clears hashmap and creates a new one of size 7'''
        self.inner_size = 7
        self.array = [None] * self.inner_size
        self.count = 0

    def capacity(self):
        '''returns capacity of hashmap'''
        return self.inner_size

    def size(self):
        '''returns how many elements are in hashmap'''
        return self.count

    def keys(self):
        '''returns a list of keys'''
        result = []
        for index in range(self.inner_size):
            print(self.array[index])
            if self.array[index] is not None:
                for item in self.array[index]:
                    result.append(item[0])
        return result

    def __hash__(self):
        '''hash function'''
        return -12
