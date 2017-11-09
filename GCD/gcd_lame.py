#!/usr/bin/env python3
"""
Calculate gcd using #TODO Lame's mod-ification.

Implementation (c) 2016, 2017 Brig Young (github.com/Sonophoto)
License: BSD-2c, i.e. Cite.
"""

def gcd_lame(a, b):
    if (a == 0 and b == 0): return("NaN")
    if (a == 0 or b == 0): return (0)
    while (a != b):
        if (a > b):
            if (b == 0): return (a)
            a = a % b
        else:
            if (a == 0): return (b)
            b = b % a
    return a

