
#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  pa2
#  Queens.py
#------------------------------------------------------------------------------
import sys

def createBoard(n):
    rows = []
    for i in range(n+1):
        cols = []
        for j in range(n+1):
            cols.append(0)
        rows.append(cols)
    return rows

def placeQueen(B, i, j):
    B[i][j] = 1
    B[i][0] = j
    for row in range(i+1, len(B)):
        for col in range(1, len(B)):
            if (col - row == j - i) or (col + row == j + i) or (col == j):
                B[row][col] -= 1

    return B


def removeQueen(B, i, j):
    B[i][j] = 0
    B[i][0] = 0
    for row in range(i+1, len(B)):
        for col in range(1, len(B)):
            if (col - row == j - i) or (col + row == j + i) or (col == j):
                B[row][col] += 1

    return B

def findSolutions(B, i, mode):
    sum = 0
    if i > len(B)-1:
        if mode == '-v':
            print(printBoard(B))
        return 1
    else:
        for j in range(1, len(B)):
            if B[i][j] == 0:
                placeQueen(B, i, j)
                sum  += findSolutions(B, i+1, mode)
                removeQueen(B, i, j)
    return sum

def printBoard(B):
    j = 0
    output = '('
    for i in range(1, len(B)):
        if output == '(':
            output += str(B[i][0])
        else:
            output += f', {B[i][0]}'
    output += ')'

    return output


def main():
    if len(sys.argv) > 1:
        n = sys.argv[1]
        if n.strip().isdigit():
            n = int(n)
            print(f'{n}-Queens has {findSolutions(createBoard(n), 1, None)} solutions')
        elif isinstance(n, str):
            n = str(n)
            if n != '-v':
                print('Usage: python3 Queens.py [-v] number')
                print('Option: -v verbose output, print all solutions')
            if len(sys.argv) == 3:
                k = sys.argv[2]
                if k.strip().isdigit():
                    k = int(k)
                    print(f'{k}-Queens has {findSolutions(createBoard(k), 1, n)} solutions')
    if len(sys.argv) == 1:
        print('Usage: python3 Queens.py [-v] number')
        print('Option: -v verbose output, print all solutions')

if __name__=='__main__':

   main()

# end
