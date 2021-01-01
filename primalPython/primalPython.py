# Primal Python:
#
# Functions for calculating primeness of numbers.
# Implementation (c) 2016-2020 Brig Young (github.com/Sonophoto)
# License: BSD-2c, i.e. Cite. [LINK TO REPO]
#
# Original Problem Statement
# accept number input
# list all primes upto and including this number.
# return a python list in ascending order
#
# First code is to sum the digits of the number
# Next we code for divisibility by 3, 5, 7, 


from math import sqrt
from functools import wraps

def digitalRoot(number):
    """ Takes a single value "number" as type(int) or type(str) and 
        calculates the digital root. Recurses as needed to reduce 
        digital_root to a single digit.
        See: https://oeis.org/A010888 for more on digital roots.
    """
    number = _validate(number)
    digital_root = 0
    for c in number: digital_root += int(c) 
    if digital_root < 10:
        return digital_root
    elif digital_root >= 10:                # We have more than one digit, recurse
        return digitalRoot(digital_root)


def digitalSum(number):
    """ Takes a single value "number" as type(int) of type(str) and sums
        the digits to a multi-digit digital sum.
    """
    number = _validate(number)
    digital_sum = 0
    for c in number: digital_sum += int(c)
    return digital_sum

def pyPrimeFinder(number):
   """This is taken directly from python docs, thrown in for fun, this is a classic method
      https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
   """   
   for n in range(2, 10):
      for x in range(2, n):
         if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
      else:
      # loop fell through without finding a factor
      print(n, 'is a prime number')

def _validate(number):
    """ Verify that returned value is valid string representation of an
        integer value or error.
    """
    # Validate Input
    if type(number) == str:      # If it is a string, make sure it is digits 
        if isdigit(number): number
        else:
            print("Verify that your imput consists of the digits 0 thru 9. Your input: ", number)
            return -1 #Bad Input
    elif type(number) == int:    # It is an integer value, convert to string
        number = str(number)
    return number
