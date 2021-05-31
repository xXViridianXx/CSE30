#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  pa6
#  graph.py
#-----------------------------------------------------------------------------
from queue import *

class Graph:
    def __init__(self, V, E):
        """Initialize a Graph object."""

        # basic attributes
        self._vertices = list(V)
        self._vertices.sort()
        self._pallete = [c for c in range(1, len(self._vertices) +1)]
        self._edges = list(E)
        self._adj = {x: list() for x in V}
        self._color = {c: None for c in V}
        self._ecs = {e: [] for e in V}
        for e in E:
            x, y = tuple(e)
            self._adj[x].append(y)
            self._adj[y].append(x)
            self._adj[x].sort()
            self._adj[y].sort()
        # end

    @property
    def vertices(self):
        """Return the list of vertices of self."""
        return self._vertices

    # end

    @property
    def edges(self):
        """Return the list of edges of self."""
        return self._edges


    def find_best(self, L):
        L = list(L)
        vertices = L # [1:]
        sorted_vertices = []
        adjacent = {x: len(self._adj[x]) for x in vertices}
        if len(L) > 0:
            while len(adjacent) > 0:
                mostAdj = max(adjacent, key=adjacent.get)
                sorted_vertices.append(mostAdj)
                adjacent.pop(mostAdj)
        else:
            sorted_vertices = []

        return sorted_vertices

    def Color(self):
        sorted_degree = self.find_best(self._vertices)
        if sorted_degree == []:
            return {}
        if len(sorted_degree) == 1:
            return {1}
        else:
            finishedVertices = []
            colors = self._pallete
            while len(sorted_degree) > 0:
                available = []
                if self._ecs[sorted_degree[0]] == [] and self._color[sorted_degree[0]] == None:
                    self._color[sorted_degree[0]] = 1
                    for i in self._adj[sorted_degree[0]]:
                        self._ecs[i].append(1)
                if (self._color[sorted_degree[0]] == None) and sorted_degree[0] not in finishedVertices:
                    for i in colors:
                        if i not in self._ecs[sorted_degree[0]]:
                            available.append(i)
                    self._color[sorted_degree[0]] = available[0]
                    for c in self._adj[sorted_degree[0]]:
                        if available[0] not in self._ecs[c]:
                            self._ecs[c].append(available[0])
                            self._ecs[c].sort()
                finishedVertices.append(sorted_degree[0])
                sorted_degree = sorted_degree[1:]
            colorDictionary = self._color
            maxColoredVert = max(colorDictionary, key=colorDictionary.get)
            maxColor = colorDictionary[maxColoredVert]
            colorsUsed = set()
            for i in range(1,maxColor + 1):
                colorsUsed.add(int(i))
            return colorsUsed
                
    def getColor(self, x):
        return self._color[x]

