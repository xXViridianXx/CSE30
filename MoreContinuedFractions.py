#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  la3
#  ContinuedFractions.py
#-----------------------------------------------------------------------------
from rational import *
from decimal import *
import sys

def CF2R(L):
    if len(L) == 1:
        return Rational(L[0])
    elif len(L) > 1:
        return Rational(L[0]) + (Rational(1) / CF2R(L[1:]))

def R2CF(x):
    numer = x.numer
    denom = x.denom
    gcd_list = []
    q = numer // denom
    r = numer % denom
    if r == 0:
        gcd_list.append(q)
        return gcd_list
    gcd_list.append(q)
    x = Rational(denom, r)
    return gcd_list + R2CF(x)

def GCF2R(L):
    
    if len(L) == 0:
        return Rational(1)

    if len(L) == 1:
        return Rational(L[0])
    else:
        return Rational(L[0]) + (Rational(L[1]) / GCF2R(L[2:]))

def pi_gen():
    k = -1
    counter = 0
    while True:
            if k == -1:
                yield 0
                k += 1
            if k == 0:
                yield 4
                k += 1
                counter += 1
            elif k >= 1 and counter % 2 == 1:
                yield (2*k) -1
                counter += 1
            elif k >= 1 and counter % 2 == 0:
                yield k**2
                k +=1
                counter += 1

        
    #return L

def main():
    pi_list = []
    gen = pi_gen()
    for i in range(268):
        pi_list.append(next(gen))
    getcontext().prec = 101
    S = GCF2R(pi_list)
    numerator = S.numer
    denominator = S.denom
    pi = Decimal(numerator) / Decimal(denominator)
    approx = Rational(numerator, denominator)
    print('')
    print(S)
    print('')
    print(pi)
    print('')
    print(R2CF(approx))
    print('')

if __name__ == '__main__':
    main()
