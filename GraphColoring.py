#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  pa6
#  GraphColoring.py
#-----------------------------------------------------------------------------
from os import initgroups
from graph import *
import sys

def CheckProperColoring(G):
    same = 0
    for x, y in G._edges:
        if G._color[x] == G._color[y]:
            same += 1
    if same > 0:
        return False
    if same == 0:
        return True

def getVertices(inputFile):
    if inputFile == []:
        return []
    else:
        verticeNumber = inputFile[0]
        inputFile = inputFile[1:]
        vertices = set()
        for i in inputFile:
            vertices.add(i)

        return vertices

def getEdges(inputFile):
    if inputFile == []:
        return []
    if len(inputFile) == 1:
        return None
    else:
        verticeNumber = inputFile[0]
        inputFile = inputFile[1:]
        edgeList = []
        while len(inputFile) > 0:
            edgeList.append((inputFile[0], inputFile[1]))
            inputFile = inputFile[2:]
        
        return edgeList

def usage():
    sys.stderr.write('Usage: $ python3 GraphColoring.py <input file> <output file>')
    
# end
def main():
    if len(sys.argv) != 3:
        usage()
    else:
        try:
            in_file = open(sys.argv[1])
            outfile = open(sys.argv[2], 'w')
            lines = in_file.readlines()
            R = []
            for S in lines:
                L = S.split()
                R += list(map(int, L))
                # A = CF2R(R)
                # a = Decimal(A._numer) / Decimal(A._denom)
                # print(A, file=outfile)
                # print(a, file=outfile)
                # print('', file=outfile)
            G = Graph(getVertices(R), getEdges(R))
            if R == []:
                print(G._color, file=outfile)
            else:
                G = Graph(getVertices(R), getEdges(R))
                G.find_best(getVertices(R))
                colored = G.Color()
                print(f'{len(colored)} colors used: {colored}', file=outfile)
                print('', file=outfile)
                print('vertex    color', file=outfile)
                print('----------------', file=outfile)
                for vertice, color in G._color.items():
                    if 0 < vertice < 10:
                        print(f' {vertice}         {color}         ', file=outfile)
                    elif 10 <= vertice < 100:
                        print(f' {vertice}        {color}         ', file=outfile)
                    elif 100 <= vertice < 1000:
                        print(f' {vertice}       {color}         ', file=outfile)
        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            usage()

if __name__ == '__main__':
    main()
