#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  pa3
#  lines.py
#------------------------------------------------------------------------------
import math

class Point(object):
   """Class representing a Point in the x-y coordinate plane."""

   def __init__(self, x, y):
      """Initialize a Point object."""
      self.xcoord = x
      self.ycoord = y
   # end

   def __str__(self):
      """Return the string representation of a Point."""
      return '({}, {})'.format(self.xcoord, self.ycoord)
   # end

   def __repr__(self):
      """Return the detailed string representation of a Point."""
      return 'geometry.Point({}, {})'.format(self.xcoord, self.ycoord)
   # end

   def __eq__(self, other):
      """
      Return True if self and other have the same coordinates, False otherwise.
      """
      eqx = (self.xcoord==other.xcoord)
      eqy = (self.ycoord==other.ycoord)
      return eqx and eqy
   # end

   def distance(self, other):
      """Return the distance between self and other."""
      diffx = self.xcoord - other.xcoord
      diffy = self.ycoord - other.ycoord
      return math.sqrt( diffx**2 + diffy**2 )
   # end

   def norm(self):
      """Return the distance from self to the origin (0, 0)."""
      return self.distance(Point(0,0))
   # end

   def midpoint(self, other):
      """Return the midpoint of the line segment from self to other."""
      midx = (self.xcoord + other.xcoord)/2
      midy = (self.ycoord + other.ycoord)/2
      return Point(midx, midy)
   # end

   def join(self, other):
      """
      If self==other return None. Otherwise return the line passing through
      self and other.
      """
      if self == other:
          return None
      if self.xcoord - other.xcoord != 0:
          return Line(self, (self.ycoord - other.ycoord)/(self.xcoord - other.xcoord))
      else:
          return Line(self, 'infinity')
   # end

# end

class Line(object):
   """Class representing a Line in the x-y coordinate plane."""

   def __init__(self, P, m):
      """Initialize a Line object."""
      self.P = P
      self.m = m
      if self.m != 'infinity':
          self.b = self.P.ycoord - self.m*(self.P.xcoord)
      if self.m == 'infinity':
          self.b = 0
   # end

   def __str__(self):
      """Return a string representation of a Line."""
      return f'Line through {self.P} of slope {self.m}'
   # end

   def __repr__(self):
      """ Return a detailed string representation of a Line."""
      return f'lines.Line(point={self.P}, slope={self.m})'

   # end

   def __eq__(self, other):
      """
      Return True if self and other are identical Lines, False otherwise.

      """
      # if self.m == other.m and (self.contains_point(other.P) or other.contains_point(self.P)):
      #     return True
      # else:
      #     return False
      if self.m == other.m:
          return self.b == other.b
      if (self.m == 'infinity' and other.m == 'infinity') and self.P.xcoord == other.P.xcoord:
          return True
      else:
          return False
   # end

   def parallel(self, other):
      """
      Return True if self and other are parallel lines, False otherwise.
      """
      if (self.m == other.m) :
          return True
      else:
          return False
   # end

   def perpendicular(self, other):
      """
      Return True if self and other are perpendicular lines, False otherwise.
      """

      if (self.m != "infinity" and self.m != 0) and (other.m != 'infinity' and self.m != 0):
          if (-1/(self.m)) == other.m:
              return True
          else:
              return False
      if self.m == 'infinity' and other.m == 0:
          return True
      if other.m == 'infinity' and self.m == 0:
          return True

   # end

   def contains_point(self, P):
      """
      Return True if self contains point P, False otherwise.
      """
      if self.m != 'infinity':
          if P.ycoord == self.m * P.xcoord + self.b:
              return True
          if P.ycoord != self.m * P.xcoord + self.b:
              return False
      if self.m == 'infinity' and (P.xcoord == self.P.xcoord):
          return True
      else:
          return False
   # end

   def intersect(self, other):
      """
      If self and other are parallel, return None.  Otherwise return their
      Point of intersection.
      """
      if self.m != 'infinity' and other.m != 'infinity':
          if self.m == other.m:
              return None
          else:
              x = (other.b - self.b) / (self.m - other.m)
              y = (self.m * x) + self.b
              return Point(x, y)
      if self.m == 'infinity' and other.m != 'infinity':
          return Point(self.P.xcoord, (other.m * self.P.xcoord) + other.b )
      if other.m == 'infinity' and self.m != 'infinity':
          return Point(other.P.xcoord, (self.m * other.P.xcoord) + self.b )
      if self.m == 'infinity' and other.m == 'infinity':
          return None

   # end

   def parallel_line(self, P):
      """Returns the Line through P that is parallel to self."""
      return Line(P, self.m)
   # end

   def perpendicular_line(self, P):
      """Returns the Line through P that is perpendicular to self."""
      if self.m == 'infinity':
          return Line(P, 0)
      elif self.m == 0:
          return Line(P, 'infinity')
      else:
          return Line(P, (-1/self.m))
   # end

# end

def main():

   P = Point(1, 3)
   Q = Point(3, 3)
   R = Point(1, 1)
   S = Point(3, 1) #3,1
   T = Point(4, 3)
   U = Point(5, 5)
   V = Point(2, 2)
   W = Point(2, 5)
   X = Point(2, -1)
   G = Point(2,-1)
   N = Point(1, -3.5)
   # Z = Point(3, -1)
   # me = Point(2, 2)

   A = Line(P, -1)
   B = Line(R, 1)
   C = S.join(T) #points_to_line(S, T)
   D = Line(W, 'infinity')
   L = Line(W, 'infinity')
   E = Line(Q, 0)
   F = C.parallel_line(P) #c.parr
   Y = Line(Z, 6.5)

   print()
   print('A =', A)
   print(repr(A))
   print()
   print('B =', B)
   print(repr(B))
   print()
   print('C =', C)
   print(repr(C))
   print()
   print('D =', D)
   print(repr(D))
   print()
   print('E =', E)
   print(repr(E))
   print()
   print('F =', F)
   print(repr(F))
   #
   print()
   print(B.intersect(C)==U)
   print(A.intersect(B)==V)
   print(D.intersect(C)==X)
   print(D.intersect(Line(T,'infinity'))==None)
   print(A.perpendicular(B))
   print(D.perpendicular(E))
   print(A.parallel(B.perpendicular_line(Q)))
   print(A.contains_point(S))
   print(B.contains_point(U))
   print(C.contains_point(X))
   print(F.contains_point(W))
   print()

   # print(Y.perpendicular_line(me))

# end

#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end
