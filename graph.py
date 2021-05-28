# # from queue import *

class Graph:
    def __init__(self, V, E):
        """Initialize a Graph object."""

        # basic attributes
        self._vertices = list(V)
        self._vertices.sort()
        self._edges = list(E)
        self._adj = {x: list() for x in V}
        self._color = {c: 0 for c in V}
        self._ecs = {e: [] for e in V}
        for e in E:
            x, y = tuple(e)
            self._adj[x].append(y)
            self._adj[y].append(x)
            self._adj[x].sort()
            self._adj[y].sort()
        # end

        # additional attributes
        self._component = {x: None for x in V}  # for findComponents()
        self._distance = {x: None for x in V}  # for BFS()
        self._predecessor = {x: None for x in V}  # for BFS()

    @property
    def vertices(self):
        """Return the list of vertices of self."""
        return self._vertices

    # end

    @property
    def edges(self):
        """Return the list of edges of self."""
        return self._edges

    # end

    def __str__(self):
        """Return a string representation of self."""
        s = ''
        for x in self.vertices:
            a = str(self._adj[x])
            s += '{}: {}\n'.format(x, a[1:-1])
        # end
        return s

    # end

    def find_best(self, L):
        vertices = L
        highest_degree = 0
        sorted_vertices = []
        while len(vertices) != 0:
            max = 0
            for i in vertices:
                if self._color[i] == 0 and len(self._adj[i]) > max:
                    max = len(self._adj[i])
                    highest_degree = i
                if len(self._adj[i]) == max:
                    highest_degree == min(highest_degree, i)

            sorted_vertices.append(highest_degree)
            vertices.remove(highest_degree)
        return sorted_vertices

    def Color(self):
        colors = []
        #self._color = self._color
        vertices = self._vertices
        finished_vertices = []

        for c in range(1, len(vertices) + 1):
            colors.append(c)
        sorted_degree = self.find_best(vertices)
        no_constraints = sorted_degree[0]

        while len(sorted_degree) > 0:
            available = []
            if sorted_degree[0] == no_constraints:
                self._color[sorted_degree[0]] = 1
                for i in self._adj[sorted_degree[0]]:
                    self._ecs[i].append(1)
                finished_vertices.append(sorted_degree[0])
                sorted_degree = sorted_degree[1:]
            if sorted_degree[0] != no_constraints:
                for i in colors:
                    if i not in self._ecs[sorted_degree[0]]:
                        available.append(i)
                self._color[sorted_degree[0]] = available[0]
                for i in self._adj[sorted_degree[0]]:
                    if available[0] not in self._ecs[i] and self._color[i] != available[0]:
                        self._ecs[i].append(available[0])
                        self._ecs[i].sort()
                finished_vertices.append(sorted_degree[0])
                sorted_degree = sorted_degree[1:]

        return self._color

    def get_color(self, x):
        return self._color[x]


# V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# E = [(1, 2), (1, 6), (6, 2), (2, 7), (6, 7), (2, 3), (2, 5), (7, 5), (7, 8), (3, 4), (4, 5), (4, 9), (9, 5), (9, 8)]
# G = Graph(V, E)
#
# print(G.vertices)
# print(G.edges)
# print(G.find_best(V))
# print(G.Color())


# V = [1,2,3,4,5,6]
# E = [(1,2),(1,4),(2,3),(2,4),(2,5),(3,5),(3,6),(4,5),(5,6)]
# G = Graph(V,E)
#
# print()
# print(G.vertices)
# print(G.edges)
# print(G.find_best(V))
# print(G.Color())
# print(G.get_color(5))

# V = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# E = [(1,7),(7,12),(7,5),(7,3),(3,2),(5,2),(5,11),(6,9),(6,10),(10,4),(10,15),(15,14),(14,13),(9,13),(13,8)]
# G = Graph(V,E)

# print()
# print(G.vertices)
# print(G.edges)
# print(G.find_best(V))
# print(G.Color())
# print(G.get_color(5))



