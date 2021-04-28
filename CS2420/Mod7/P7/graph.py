''''''
#!Questions:
#! in add_vertex & add_edge, whats the purpose of returning the graph?
#! should float get_weight(src, dest) : function have name as --
#! float_get_weight() or get_weight()?

import sys
import heapq
import math
class StorageCollection:
    ''' creates a storage of queue or stack depending on true or false param passed in.
    Stack is true and queue is false'''
    def __init__(self, isStack):
        if not isinstance(isStack, bool):
            raise ValueError("StorageCollection type must specified with true or false")
        self.popIndex = 0
        if isStack:
            self.popIndex = -1
        self.storage = []

    def push(self, val):
        '''appends a value to the storage'''
        self.storage.append(val)

    def pop(self):
        '''pops a value from storage'''
        return self.storage.pop(self.popIndex)

    def is_empty(self):
        '''returns true if storage is empty'''
        return self.storage == []


class Graph:
    '''class graph creates a graph which is used to store points and edges'''
    def __init__(self):
        self.vertices = []
        self.matrix = [[]]

    def __iter__(self):
        '''iterator'''
        vertices = self.bfs(self.vertices)
        for item in vertices:
            yield item

    def add_vertex(self, label):
        '''adds a vertex to the graph object'''
        if label == 0:
            raise ValueError("Weight must be greater than 0")
        num_vertices = len(self.vertices)
        self.vertices.append(label)
        temp = self.matrix
        self.matrix = [[math.inf for x in range(num_vertices+1)]for y in range(num_vertices+1)]
        for i in range(0,num_vertices):
            for x in range(0,num_vertices):
                self.matrix[i][x] = temp[i][x]
        return self

    def add_edge(self, src, dest, w):
        '''adds an edge between 2 graph objects'''
        if src not in self.vertices and dest not in self.vertices:
            raise ValueError("One of the points are not valid")
        elif isinstance(w, str):
            raise ValueError("Weight must be a number")
        self.matrix[self.vertices.index(src)][self.vertices.index(dest)] = w
        return self

    #! Is float in the name or not?
    def get_weight(self, src, dest):
        '''gets the weight of an edge between a src and destination'''
        if src not in self.vertices and dest not in self.vertices:
            raise ValueError("One of the points are not valid")
        return float(self.matrix[self.vertices.index(src)][self.vertices.index(dest)])

    def neighbors(self, vertex):
        '''gets the neighbors of a given vertex'''
        result = []
        v = self.vertices.index(vertex)
        for i in range(len(self.vertices)):
            weight = self.matrix[v][i]
            if weight is not None:
                result.append((self.vertices[i], weight))
        return result

    def __traverse(self, vertex, collection):
        '''helper function to help traverse the graph'''
        result = []
        visited = [False] * len(self.vertices)
        vertices_count = len(self.vertices)
        index = self.vertices.index(vertex)
        collection.push(index)
        visited[index] = True

        while not collection.is_empty():
            v = collection.pop()
            result.append(self.vertices[v])
            for i in range(vertices_count):
                neighbor = self.matrix[v][i]
                if neighbor is not math.inf and visited[i] == False:
                    collection.push(i)
                    visited[i] = True
        return result

    def dfs(self, starting_vertex):
        '''traverses the graph depth first'''
        stack = StorageCollection(True)
        return self.__traverse(starting_vertex, stack)

    def bfs(self, starting_vertex):
        '''traverses the graph breadth first'''
        queue = StorageCollection(False)
        return self.__traverse(starting_vertex, queue)

    def __str__(self):
        '''Returns the graph in graphviz notation'''
        vertices_count = len(self.vertices)
        result = "digraph G {\n"
        for label in self.vertices:
            index = self.vertices.index(label)
            for value in range(vertices_count):
                floatValue = self.matrix[index][value]
                if floatValue is not math.inf:
                    floatString = "{:.1f}".format(floatValue)
                    result += "   " + label + " -> " + self.vertices[value] + " [label=\"" + floatString + "\",weight=\"" + floatString + "\"];\n"
        result += "}\n"
        return result

    def getIndex(self, queue, vertex_label):
        for i in range(len(queue)):
            if queue[i][1] == vertex_label:
                return i
        return -1

    #!same thing as float function, but has list
    def dsp(self, src, dest):
        '''Finds the shortest path from src to destination'''
        queue = []
        visited = []
        num_vertices = len(self.vertices)

        for vertex in self.vertices:
            if vertex == src:
                queue.insert(0, (0, vertex, None))
            else:
                queue.append((float('infinity'), vertex, None))

        while queue[0][0] < float('infinity') and dest not in visited:
            for x in range(num_vertices):
                if queue[x][1] not in visited:
                    current_vertex = queue[x][1]
                    current_dist = queue[x][0]
                    break
            # a = self.neighbors(current_vert)
            for item in self.neighbors(current_vertex):
                neighbor = item[0]
                if neighbor in visited:
                    continue
                weight = item[1]
                distance = current_dist + weight
                neighbor_ind = self.getIndex(queue, neighbor)
                neighbor_dist = queue[neighbor_ind][0]
                if neighbor == -1:
                    continue
                elif neighbor_dist > distance:
                    queue[neighbor_ind] = (distance,neighbor,current_vertex)

            visited.append(current_vertex)
            queue = sorted(queue, key = lambda x:x[0])

        target_index = self.getIndex(queue, dest)
        result_length = queue[target_index][0]
        if result_length == float('infinity'):
            return result_length, []
        else:
            current_vertex = dest
            result_path = []
            result_path.append(current_vertex)
            while current_vertex != src:
                current_vertex = queue[self.getIndex(queue,current_vertex)][2]
                result_path.insert(0, current_vertex)
            return result_length, result_path

    def dsp_all(self, src):
        '''Creates a dictionary with the shortes path from the src to every other vertex'''
        sorted_vertices = sorted(self.vertices)
        result = {vertex: [] for vertex in sorted_vertices}

        for current_vert in self.vertices:
            result[current_vert] = self.dsp(src, current_vert)[1]
        return result


def main():
    '''Main creates a graph and then preforms various graph functions'''
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "F", 9)
    graph.add_edge("B", "C", 8)
    graph.add_edge("B", "D", 15)
    graph.add_edge("B", "F", 6)
    graph.add_edge("C", "D", 1)
    graph.add_edge("E", "C", 7)
    graph.add_edge("E", "D", 3)
    graph.add_edge("F", "E", 3)
    graph.add_edge("F", "B", 6)

    print(graph)

    print("starting BFS with vertex A")
    for vertex in graph.bfs("A"):
        print(vertex, end = "")
    print()

    print("starting BFS with vertex A")
    for vertex in graph.dfs("A"):
        print(vertex, end = "")
    print()

    print(graph.dsp("A", "F"))
    # print(graph.dsp_all("A"))
    a_paths = graph.dsp_all("A")
    for path in a_paths:
        print(f"{path}: {a_paths[path]}")


if __name__ == "__main__":
    main()
