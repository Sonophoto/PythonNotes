#!/usr/bin/env python3
#
# generate random triples of values for testing gcd_euclid() and gcd_lame()


import math
import random

counter = 20
fuzzies = []

for element in range(20):
    a_value = int(random.random()*1000)
    b_value = int(random.random()*100)
    gcd_value = math.gcd(a_value, b_value)
    fuzzies.append((a_value, b_value, gcd_value))
    fuzzies.append((b_value, a_value, gcd_value))


print(fuzzies)
