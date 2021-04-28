''''''
#!Questions:
#! in add_vertex & add_edge, whats the purpose of returning the graph?
#! should float get_weight(src, dest) : function have name as --
#! float_get_weight() or get_weight()?
class StorageCollection:
    def __init__(self, isStack):
        if not isinstance(isStack, bool):
            raise ValueError("StorageCollection type must specified with true or false")
        self.popIndex = 0
        if isStack:
            self.popIndex = -1
        self.storage = []

    def push(self, val):
        self.storage.append(val)

    def pop(self):
        return self.storage.pop(self.popIndex)

    def is_empty(self):
        return self.storage == []


class Graph:
    def __init__(self):
        self.vertices = []
        self.matrix = [[]]

    def __iter__(self):
        pass

    def add_vertex(self, label):
        pass

    def add_edge(self, src, dest, w):
        pass

    #!Is float in the name or not?
    # def float get_weight(self, src, dest):
    #     pass

    def dfs(self, starting_vertex):
        pass

    def bfs(self, starting_vertex):
        pass

    #!same thing as float function, but has list
    def dsp(self, src, dest):
        pass

    #!same thing as 2 prev function, but dictionary
    def dsp_all(self, src):
        pass

    def __str__(self):
        pass
        # result = "graph {\n"
        # for x in self.vertices:
        #     result += self
        # result += "}"



def main():
    ''''''
    pass

if __name__ == "__main__":
    main()