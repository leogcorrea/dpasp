# Python Program to detect cycle in an undirected FLOAT
from collections import defaultdict
import re

# This class represents a undirected
# graph using adjacency list representation

class Graph:
 
    def __init__(self):
        # Default dictionary to store graph
        self.edges = defaultdict(list)

        #List of vertices
        self.vertices = []
 
    def searchVertices(self, pattern):
        result = []
        for v in self.vertices:
            idx = v.find(":-")
            if idx == -1:
                label = v
            else:
                label = v[:idx]
            regex = re.compile(pattern)
            if regex.search(label):
                result.append(v)
        return result
    
    def addVertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)

    # Function to add an edge to graph
    def addEdge(self, v, w):
 
        # Add w to v_s list
        self.edges[v].append(w)
 
        # Add v to w_s list
        self.edges[w].append(v)
 
    # A recursive function that uses
    # visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):
 
        # Mark the current node as visited
        visited[v] = True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.edges[v]:
 
            # If the node is not
            # visited then recurse on it
            if not visited[i]:
                if self.isCyclicUtil(i, visited, v):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != i:
                return True
 
        return False
 
    # Returns true if the graph
    # contains a cycle, else false.
 
    def isCyclic(self):
 
        # Mark all the vertices
        # as not visited
        visited = [False]*len(self.vertices)
 
        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i in range(len(self.vertices)):
 
            # Don't recur for u if it
            # is already visited
            if not visited[i]:
                if self.isCyclicUtil(i, visited, -1):
                    return True
 
        return False
 