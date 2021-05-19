#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  pa5
#  TestList.py
#------------------------------------------------------------------------------

from list import *
# ------------------------------------------------------------------------------
#  Test the List type
# ------------------------------------------------------------------------------
def main():

    L = List()
    L.append(1)
    L.append(2)
    L.append(3)
    print(len(L))
    print(L)
    print(repr(L))

    A = List()
    A.append(1)
    A.append(2)
    A.append(3)
    print('A==L :', A == L)
    A.append(4)
    print('A==L :', A == L)
    L.append(5)
    print(L)
    print(A)
    print('A==L is', A == L)

    L.clear()
    print(len(L))
    print(L)

    B = A.copy()
    print(B)
    print(repr(B))
    print('A==B :', A == B)
    print('A is B :', A is B)

    N = List()
    N.append(2)
    N.append(5)
    N.append(3)

    print()
    print(B)
    B.insert(0, 'foo')
    print(B)
    B.insert(3, 'bar')
    print(B)
    B.insert(6, 'one')
    print(B)
    B.insert(-2, 'two')
    print(B)
    print(repr(B))
    print(len(B))

    print()
    print(B.pop(0))
    print(B)
    print(B.pop(2))
    print(B)
    print(B.pop(5))
    print(B)
    print(B.pop(-2))
    print(B)
    print(len(B))
    print()
    N[5] = 9
    print(N)
    N[-2] = 7
    print(N)
    print(N[1])
    print(A + N)
    print(A * -1)
    print(-1 * A)
    print(A * 2)
    print(2 * A)
    A += N
    print(A)
    A.reverse()
    print(A)

# end

# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end
