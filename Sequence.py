import sys



def power_remainder(n, b, r):
    i = 1
    while True:
        if i**n % b == r:
            yield i**n
        i+=1

def common_terms(g, h):

    x = next(g)
    y = next(h)


    while True:
        if y == x:
            yield y
            x = next(g)
        if x < y:
            x = next(g)
        if y < x:
            y = next(h)

if __name__=='__main__':

    A = power_remainder(2, 3, 1)
    B = power_remainder(3, 5, 4)
    C = common_terms(power_remainder(3, 5, 4), power_remainder(2, 3, 1))

    print()
    for i in range(15):
        s = " {0:<12}{1:<12}{2:<12}".format(next(A), next(B), next(C))
        print(s)
        # end
    print()
# end
