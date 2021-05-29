from graph import *
import sys

def CheckProperColoring(G):
    different = 0
    same = 0
    for x, y in G._edges:
        if G._color[x] != G._color[y]:
            different += 1
        if G._color == G._color[y]:
            same += 1
    if same > 0:
        return False
    if different > 0 and same == 0:
        return True

def getVertices(inputFile):
    verticeNumber = inputFile[0]
    inputFile = inputFile[1:]
    vertices = set()
    for i in inputFile:
        vertices.add(i)

    return vertices


def getEdges(inputFile):
    verticeNumber = inputFile[0]
    inputFile = inputFile[1:]
    edgeList = []
    while len(inputFile) > 0:
        edgeList.append((inputFile[0], inputFile[1]))
        inputFile = inputFile[2:]
    
    return edgeList

def printColorsUsed(colorDictionary):
    maxColoredVert = max(colorDictionary, key=colorDictionary.get)
    maxColor = colorDictionary[maxColoredVert]
    colorsUsed = set()
    for i in range(1,maxColor + 1):
        colorsUsed.add(i)
    return f'{maxColor} colors used: {colorsUsed}'









def usage():
    sys.stderr.write('Usage: $ python3 GraphColoring.py <input file> <output file>')
    


# end
def main():
 # check command line arguments and open files

 # read each line of input file

 # get number of vertices on first line, create vertex list

 # create edge list from remaining lines

 # create graph G

 # Determine a proper coloring of G and print it to the output file

    """
    # Check that the coloring is correct
    print(file=outfile)
    msg = 'coloring is proper: {}'.format(CheckProperColoring(G))
    print(msg, file=outfile )

    """
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
            G.find_best(getVertices(R))
            colored = G.Color()
            A = printColorsUsed(colored)
            # print('', file=outfile)
            # print(A, file=outfile)
            # print('', file=outfile)
            # print('vertex    color', file=outfile)
            # print('----------------', file=outfile)
            # for vertice, color in colored.items():
            #     if 0 < vertice < 10:
            #         print(f' {vertice}         {color}         ', file=outfile)
            #     elif 10 <= vertice < 100:
            #         print(f' {vertice}        {color}         ', file=outfile)
            #     elif 100 <= vertice < 1000:
            #         print(f'{vertice}       {color}         ', file=outfile)
            print('')
            print(A)
            print('')
            print('vertex    color')
            print('----------------')
            for vertice, color in colored.items():
                if 0 < vertice < 10:
                    print(f' {vertice}         {color}         ')
                elif 10 <= vertice < 100:
                    print(f' {vertice}        {color}         ')
                elif 100 <= vertice < 1000:
                    print(f' {vertice}       {color}         ')
            print(CheckProperColoring(G))

            


        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            usage()

if __name__ == '__main__':
    main()

# V = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# E = [(1,7),(7,12),(7,5),(7,3),(3,2),(5,2),(5,11),(6,9),(6,10),(10,4),(10,15),(15,14),(14,13),(9,13),(13,8)]
# G = Graph(V,E)

# print()
# print(G.vertices)
# print(G.edges)
# print(G.find_best(V))
# print(G.Color())
# print(G.get_color(5))
# print(CheckProperColoring(G))

# V = [1,2,3,4,5,6,7]
# E = [(1,2),(2,5),(2,3),(2,6),(2,4),(5,4),(5,3),(3,6),(3,7),(7,4),(4,3)]
# G = Graph(V,E)

# print()
# print(G.vertices)
# print(G.edges)
# print(G.find_best(V))
# print(G.Color())
# #print(G.get_color(5))
# print(CheckProperColoring(G))
# # end