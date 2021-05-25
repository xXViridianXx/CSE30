#------------------------------------------------------------------------------
#  graphs.py
#  Definition of the Graph class.
#------------------------------------------------------------------------------
from queue import *

class Graph(object):
   """Class representing an undirected graph."""

   def __init__(self, V, E):
      """Initialize a Graph object."""

      # basic attributes
      self._vertices = list(V)
      self._vertices.sort()
      self._edges = list(E)
      self._adj = {x:list() for x in V}
      for e in E:
         x,y = tuple(e)
         self._adj[x].append(y)
         self._adj[y].append(x)
         self._adj[x].sort()
         self._adj[y].sort()
      # end
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

    def add_vertex(self, x):
      """Adds a vertex x to self."""
      if x not in self.vertices:
         self.vertices.append(x)
         self.vertices.sort()
         self._adj[x] = list()

      # end
   # end 

   def add_edge(self, e):
      """Adds an edge e to self."""
      x, y = tuple(e)
      self.add_vertex(x)
      self.add_vertex(y)
      self._adj[x].append(y)
      self._adj[y].append(x)
      self._adj[x].sort()
      self._adj[y].sort()
      self.edges.append(e)
   # end      

   def degree(self, x):
      """Returns the degree of vertex x."""
      return len(self._adj[x])
   # end