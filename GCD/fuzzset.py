#!/usr/bin/env python3

"""
 Generate random triples of values for testing gcd_euclid() and gcd_lame()

 Implementation (c) 2016,2017 Brig Young (github.com/Sonophoto)
 License: BSD-2c, i.e. Cite.
"""

from math import gcd
from random import random

number_of_tuples = 20
""" Number of random tuples to create """

double_tuples = True
""" Create reverse tuples as well? i.e. (a,b)->(b,a) """

a_size  = 1000
""" Range of a_size ==  1 to (a_value-1) """

b_size  = 100
""" Range of b_size ==  1 to (b_value-1) """

fuzzies = []
""" This list collects the generated values """

for element in range(number_of_tuples):
    a_value = int(random()*a_size)
    b_value = int(random()*b_size)
    gcd_value = gcd(a_value, b_value)
    fuzzies.append((a_value, b_value, gcd_value))
    fuzzies.append((b_value, a_value, gcd_value))

# Output, modify to suit your specific needs
print(fuzzies)
