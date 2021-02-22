import time

class ArrayList:
    def __init__(self):
        self.my_array = []
        self.last_index = 0
        self.max_size = 0
        self.size_exponent = 0

    def add(self, value):
        if self.last_index > self.max_size - 1:
            self.__resize__()
        for ind in range(self.last_index, 0, -1):
            self.my_array[ind+1] = self.my_array[ind]
        self.my_array[0] = value

    def append(self, value):
        if self.last_index > self.max_size - 1:
            self.__resize__()
        self.my_array[self.last_index] = value
        self.last_index += 1

    def __resize__(self):
        new_size = 2**self.size_exponent
        new_array = [0] * new_size #! make an array of new_size and populate with 0s
        for num in range(self.max_size):
            new_array[num] = self.my_array[num]
        self.max_size = new_size
        self.my_array = new_array
        self.size_exponent += 1
    
    def __getitem__(self, index):
        if index > self.last_index:
            raise LookupError("Index out of bounds")
        return self.my_array[index]

def main():
    start = time.perf_counter()
    lyst = ArrayList()
    end = time.perf_counter()
    print(f"Array list creation took {end-start:.8f} seconds")

    start = time.perf_counter()
    for i in range(1000):
        lyst.append(i)
    end = time.perf_counter()
    print(f"It took {end-start:.8f} sec to append 1000 items")

    start = time.perf_counter()
    for i in range(1000):
        lyst.add(i)
    end = time.perf_counter()
    print(f"It took {end-start:.8f} sec to add 1000 items")

if __name__ == "__main__":
    main()
