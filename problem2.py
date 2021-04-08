import sys

def Sum(n,m):
    if n > m:
        return 0
    return m + Sum(n, m-1)




if __name__=='__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    print(Sum(n, m))
