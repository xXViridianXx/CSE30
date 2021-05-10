#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  pa4
#  ratioanl.py
#------------------------------------------------------------------------------

import sys

def _gcd(n, d):
    # This is the "without loss of generality" part.
    if n >= 0 and d > 0 :
        d, n = (n, d) if d > n else (d, n)
    elif n >= 0 and d < 0:
        d, n = (d, n) if d > n else (n, d)
    elif n <= 0 and d > 0:
        d, n = (n, d) if d > n else (d, n)
    elif n <= 0 and d < 0:
        d, n = (d, n) if d > n else (n, d)
    return n if d == 0 else _gcd(d, n % d)

class Rational(object):
    '''class representing a rational number'''

    def __init__(self, numerator, denominator = 1):
        '''Initialize a Rational object.'''
        if denominator < 0 and numerator >= 0 or numerator <= 0 and denominator > 0:
            self._numer = int(numerator // _gcd(numerator, denominator)) * -1
            self._denom = int(denominator // _gcd(numerator, denominator)) * -1
        else:
            self._numer = int(numerator // _gcd(numerator, denominator))
            self._denom = int(denominator // _gcd(numerator, denominator))

    @property
    def numer(self):
        '''Return the numerator of a rational number.'''
        return self._numer

    @property
    def denom(self):
        '''Return the denominator of a rational number.'''
        return self._denom

    def __add__(self, other):
        '''Return the sum of two rational numbers.'''
        added_numer = self._numer + other._numer
        common_denom = self._denom * other._denom
        if self._denom == other._denom:
            return Rational(added_numer, self._denom)
        else:
            return Rational((self._numer*other._denom) + (other._numer*self._denom), common_denom)

    def __sub__(self, other):
        '''Return the difference of two rational numbers.'''
        subtracted_numer = self._numer - other._numer
        common_denom = self._denom * other._denom
        if self._denom == other._denom:
            return Rational(subtracted_numer, self._denom)
        else:
            return Rational((self._numer*other._denom) - (other._numer*self._denom), common_denom)

    def __str__(self):
        '''Return the string representation of a rational number.'''
        return f'{self._numer}/{self._denom}'

    def __repr__(self):
       '''Return the detailed string representation of a rational number.'''
       return 'rational.Rational({}, {})'.format(self._numer, self._denom)

    def __mul__(self, other):
       '''Return the product of two rational numbers.'''
       numerator = self._numer * other._numer
       denominator = self._denom * other._denom
       return Rational(numerator, denominator)

    def __truediv__(self, other):
       '''Return the quotient of two rational numbers.'''
       numerator = self._numer * other._denom
       denominator = self._denom * other._numer
       return Rational(numerator, denominator)

    def __float__(self):
        '''Return the float equivalent of self.'''
        return (self._numer/self._denom)

    def __le__(self, other):
        '''Return true if self <= other, False otherwise.'''
        if float(self._numer/self._denom) <= float(other._numer/other._denom):
            return True
        else:
            return False
    def __lt__(self, other):
        '''Return true if self < other, False otherwise.'''
        if float(self._numer/self._denom) < float(other._numer/other._denom):
            return True
        else:
            return False
    def __ge__(self, other):
        '''Return true if self >= other, False otherwise.'''
        if float(self._numer/self._denom) >= float(other._numer/other._denom):
            return True
        else:
            return False
    def __gt__(self, other):
        '''Return true if self > other, False otherwise.'''
        if float(self._numer/self._denom) > float(other._numer/other._denom):
            return True
        else:
            return False

    def __ne__(self, other):
        '''Return False if self == other, True otherwise.'''
        if self._numer == other._numer and self._denom == other._denom:
           return False
        else:
           return True

    def __eq__(self, other):
        '''Return True if self == other, False otherwise.'''
        if self._numer == other._numer and self._denom == other._denom:
            return True
        else:
            return False

    def inverse(self):
        return Rational(self._denom, self._numer)
