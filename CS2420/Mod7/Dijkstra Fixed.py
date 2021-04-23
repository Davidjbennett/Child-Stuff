#!/usr/bin/env python
# coding: utf-8

# In[2]:


class StorageCollection:
    def __init__(self, isStack):
        if not isinstance(isStack, bool):
            raise ValueError("isStack parameter must be true or false.")
        self.popIndex = 0
        if isStack == True:
            self.popIndex = -1
        self.storage = []
        
    def push(self, value):
        self.storage.append(value)
        
    def pop(self):
        return self.storage.pop(self.popIndex)
        
    def is_empty(self):
        return self.storage == []
        
class Graph:
    def __init__(self):
        self.__vertices =[]        
        self.__matrix = [[]]
    
    def __iter__(self):
        vertices = self.bfs(self.__vertices[0])
        for item in vertices:
            yield item
    
    def add_vertex(self, label):
        vertices_count = len(self.__vertices)
        self.__vertices.append(label)
        temp = self.__matrix
        self.__matrix = [[None for x in range(vertices_count + 1)] for y in range(vertices_count + 1)]   
        for i in range(0, vertices_count):
            for j in range(0, vertices_count):
                self.__matrix[i][j] = temp[i][j]     
    
    def add_edge(self, src, dest, w):
        if src not in self.__vertices or dest not in self.__vertices:
            print("Vertex does not exist")
        else:
            self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)] = w 
            
    def add_edge2way(self, src, dest, w):
        self.add_edge(src, dest, w)
        self.add_edge(dest, src, w)

    def vertex_count(self):
        return len(self.__vertices)
    
    def neighbors(self, vertex):
        result = []
        v = self.__vertices.index(vertex)
        for i in range(self.vertex_count()):
            weight = self.__matrix[v][i]
            if weight is not None:
                result.append((self.__vertices[i], weight))
        return result
        
    def get_weights(self, src, dest):
        if src not in self.__vertices or dest not in self.__vertices:
            print("Vertex does not exist")
        else:
            return self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)]
    
    def __iterative_traversal(self, vertex, collection):
        result = []
        visited = [False] * len(self.__vertices) 
        vertices_count = len(self.__vertices)
        index = self.__vertices.index(vertex)        
        collection.push(index)
        visited[index] = True
        
        while not collection.is_empty():
            v = collection.pop()
            result.append(self.__vertices[v])            
            
            for i in range(vertices_count):
                neighbor = self.__matrix[v][i]
                if neighbor is not None and visited[i] == False:
                    collection.push(i)
                    visited[i] = True
        return result    
    
    def dfs(self, root):
        stack = StorageCollection(True)        
        return self.__iterative_traversal(root, stack)    
        
    def bfs(self, root):
        queue = StorageCollection(False)
        return self.__iterative_traversal(root, queue)        
        
    def __str__(self):
        vertices_count = len(self.__vertices)
        result = "graph {\n"
        for label in self.__vertices:
            index = self.__vertices.index(label)
            for value in range(vertices_count):
                floatValue = self.__matrix[index][value]
                if floatValue is not None:
                    floatString = "{:.1f}".format(floatValue)
                    result += "\t" + label + "->" + self.__vertices[value] + "[label=\"" + floatString + "\",weight=\"" + floatString + "\"];\n"
        result += "}\n"
        return result


# In[3]:


import heapq

def dijkstra_shortest_distance(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex]  = 0
    
    priority_queue = [(0, starting_vertex)]
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        
        for item in graph.neighbors(current_vertex):
            neighbor = item[0]
            weight = item[1]
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances


# In[42]:


import sys

def getIndex(priority_queue, vertex_label):
    for i in range(len(priority_queue)):
        if priority_queue[i][1] == vertex_label:
            return i
    return -1
    
def dijkstra_shortest_path(graph, starting_vertex, target_vertex):    
    priority_queue = []
    # Set all nodes as unvisited
    visited = []    
    
    vertex_count = graph.vertex_count()
    
    # Assign to every node a tentative distance value
    for vertex in graph:        
        if vertex == starting_vertex:
            priority_queue.insert(0, (0, vertex, None))
        else:
            priority_queue.append((float('infinity'), vertex, None))                    
    
    while priority_queue[0][0] < float('infinity') and target_vertex not in visited:
        # Get the current node, the first unvisited node in the priority queue
        for i in range(vertex_count):
            if priority_queue[i][1] not in visited:
                current_vertex = priority_queue[i][1]
                current_distance = priority_queue[i][0]
                break;        
        
        # Visit all the neighbors and assign a tentative distance
        for item in graph.neighbors(current_vertex):
            neighbor = item[0]
            if neighbor in visited:
                continue;
            weight = item[1]
            distance = current_distance + weight
            # Find the vertex in the priority queue to check and update its distances
            neighbor_index = getIndex(priority_queue, neighbor)
            if neighbor_index == -1:
                continue                
            elif (priority_queue[neighbor_index][0] > distance):
                priority_queue[neighbor_index] = (distance, neighbor, current_vertex)

        visited.append(current_vertex)

        # Sort list so lowest distance is on top
        priority_queue = sorted(priority_queue, key = lambda x:x[0])
    
    # See if we found a path
    target_index = getIndex(priority_queue, target_vertex)
    resulting_length = priority_queue[target_index][0]
    if resulting_length == float('infinity'):
        return resulting_length, []
    else:
        # Trace back the path from the target to the source
        current_vertex = target_vertex
        resulting_path = []
        resulting_path.append(current_vertex)
        while current_vertex != starting_vertex:
            current_vertex = priority_queue[getIndex(priority_queue, current_vertex)][2]
            resulting_path.insert(0, current_vertex)
        return resulting_length, resulting_path


# In[43]:


graph = Graph()
graph.add_vertex("eu")
graph.add_vertex("el")
graph.add_vertex("go")
graph.add_vertex("ge")
graph.add_vertex("sq")
graph.add_vertex("pa")
graph.add_vertex("er")
graph.add_vertex("wh")
graph.add_vertex("sa")
graph.add_vertex("sf")
graph.add_vertex("ma")
graph.add_vertex("sv")
graph.add_vertex("pr")
graph.add_vertex("or")
graph.add_vertex("vi")
graph.add_vertex("li")
graph.add_vertex("pg")
graph.add_vertex("af")
graph.add_vertex("hi")
graph.add_vertex("le")
graph.add_vertex("ss")
graph.add_vertex("em")
graph.add_vertex("cf")
graph.add_vertex("ff")
graph.add_edge2way("eu", "ff", 49)
graph.add_edge2way("eu", "el", 12)
graph.add_edge2way("el", "em", 28)
graph.add_edge2way("el", "go", 5)
graph.add_edge2way("go", "ge", 5)
graph.add_edge2way("ge", "sq", 4)
graph.add_edge2way("sq", "pa", 8)
graph.add_edge2way("pa", "sf", 8)
graph.add_edge2way("pa", "sa", 3)
graph.add_edge2way("pa", "er", 5)
graph.add_edge2way("er", "wh", 4)
graph.add_edge2way("er", "sa", 4)
graph.add_edge2way("wh", "sa", 4)
graph.add_edge2way("sa", "sf", 8)
graph.add_edge2way("sf", "ma", 5)
graph.add_edge2way("sf", "sv", 6)
graph.add_edge2way("sf", "pr", 9)
graph.add_edge2way("ma", "sv", 4)
graph.add_edge2way("sv", "pr", 6)
graph.add_edge2way("pr", "or", 7)
graph.add_edge2way("or", "vi", 4)
graph.add_edge2way("or", "li", 4)
graph.add_edge2way("or", "pg", 7)
graph.add_edge2way("li", "pg", 2)
graph.add_edge2way("pg", "af", 3)
graph.add_edge2way("af", "hi", 4)
graph.add_edge2way("af", "le", 3)
graph.add_edge2way("le", "hi", 5)
graph.add_edge2way("le", "cf", 15)
graph.add_edge2way("ss", "em", 11)
graph.add_edge2way("em", "ff", 9)
graph.add_edge2way("cf", "ff", 5)


# In[48]:


dijkstra_shortest_path(graph, "sq", "ss")


# In[ ]:




