#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  pa4
#  ContinuedFractions.py
#------------------------------------------------------------------------------
from rational import *
from decimal import *
import sys

def CF2R(L):
    if len(L) == 1:
        return Rational(L[0])
    elif len(L) > 1:
        return Rational(L[0]) + (Rational(1) / CF2R(L[1:]))
      
def usage():
    sys.stderr.write('Usage: $ python3 ContinuedFractions.py <input file> <output file>')

def main():
    if len(sys.argv) != 3:
        usage()
    else:
        try:
            getcontext().prec = 100
            in_file = open(sys.argv[1])
            outfile = open(sys.argv[2], 'w')
            lines = in_file.readlines()
            print('', file=outfile)
            for S in lines:
                L = S.split()
                R = list(map(int, L))
                A = CF2R(R)
                a = Decimal(A._numer) / Decimal(A._denom)
                print(A, file=outfile)
                print(a, file=outfile)
                print('', file=outfile)

        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            usage()

if __name__ == '__main__':
    main()
