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
    """ Takes a single value "number" as type(int) or type(str) and sums
        the digits. Recurses as required to reduce very large numbers to
        a single digit. Tested against 710 digit 9s, only two recursions.
    """
    # Validate Input
    if type(number) == str:                                            
        if isdigit(number): number
        else
            print("Verify that your imput consists of the digits 0 thru 9. Your input: ", number)
            return -1 #Bad Input
    elif type(number) == int:
        number = str(number)
    else: return -1 # Bad Input

    # Generate Output 
    digit_sum = 0
    for c in in_val: digit_sum += int(c)
    if digit_sum < 10:
        return digit_sum
    elif digit_sum >= 10: # We still have more than one digit, recurse.
        return digitalRoot(digit_sum)

