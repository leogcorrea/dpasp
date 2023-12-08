# Python Program to detect cycle in an undirected FLOAT
from collections import defaultdict
import re

INDEX = 0 
LOW_LINK = 1
ON_STACK = 2



# This class represents a undirected
# graph using adjacency list representation

class Graph:
 
    def __init__(self):
        # Default dictionary to store graph
        self.edges = defaultdict(list)

        #List of vertices
        self.vertices = []

        self.currentComp = []
        self.connectedComps = []

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
    def addEdge(self, v, w, neg = False):
 
        # Add w to v_s list
        self.edges[v].append((w, neg))
 
    # A recursive function that uses
    # visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent, isNegative = False):
 
        self.currentComp.append(v)
        # Mark the current node as visited
        visited[v] = True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for vertex, neg in self.edges[v]:
 
            isNegative |= neg

            # If the node is not
            # visited then recurse on it
            if not visited[vertex]:
                if self.isCyclicUtil(vertex, visited, v, isNegative):
                    return True, isNegative
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != vertex:
                return True, isNegative
 
        return False, isNegative
 
    # Returns true if the graph
    # contains a cycle, else false.

    def isCyclic(self):
 
        result = False
        # Mark all the vertices
        # as not visited

        visited = {k: False for k in self.vertices}

        self.connectedComps = []

        #visited = dict.fromkeys(self.vertices)
        #visited = [False]*len(self.vertices)
 
        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for vertex, visit in visited.items():
 
            # Don't recur for u if it
            # is already visited
            if not visit:
                isCyclic, isNegative = self.isCyclicUtil(vertex, visited, "")
                self.connectedComps.append((isNegative, self.currentComp))
                self.currentComp = []
                result |= isCyclic

        return result, self.connectedComps
