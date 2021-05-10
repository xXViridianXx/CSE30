

class Vector(object):
    def __init__(self, a, b):
        self.xcomp = a
        self.ycomp = b

    def __str__(self):
        """str(Vector(a, b)) returns the string '(a, b)'."""
        return f'({self.xcomp}, {self.ycomp})'

    def __eq__(self, other):
        """u==v returns True if and only if vectors u and v have
        equal x-components and equal y-components."""
        return self.xcomp == other.xcomp and self.ycomp == other.ycomp

    def __add__(self, other):
        """Returs the vector sum: (a,b)+(c,d)=(a+c,b+d)."""
        return Vector(self.xcomp + other.xcomp, self.ycomp + other.ycomp)


    def __sub__(self, other):
        """Returns the vector difference: (a,b)+(c,d)=(a-c,b-d)."""
        return Vector(self.xcomp - other.xcomp, self.ycomp - other.ycomp)

    def dot(self, other):
        """Returns the vector dot product: (a,b).dot(c,d)=ac+bd."""
        return (self.xcomp*other.xcomp) + (self.ycomp*other.ycomp)
    
    def __lt__(self, other):
        return (self.xcomp < other.xcomp or self.xcomp == other.xcomp) and self.ycomp < other.ycomp

    def __le__(self, other):
        return self.xcomp <= other.xcomp and self.ycomp <= other.ycomp


u = Vector(2, 5)
v = Vector(-1, 7)
n = Vector(2, 5)
print(u == v)
print(u+v)
print(u-v)
print(v-u)
print(u.dot(v))
print(u<v)
print(u<=n)
