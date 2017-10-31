# The purpose of this file is to demonstrate the actual algorythm of 
# Euclid in such a manner that Gabriel Lame's Modification is a trivial
# modification of the function. And to point out that Euclid IN FACT
# Used subtraction not %.

def gcd_euclid(a, b):
    if(a == 0 or b == 0): return 0
    while ( a != b):
        if (a > b):
            if (b == 0): return (a)
            a = a - b
        else:
            if (a == 0): return (b)
            b = b - a
    return a

# RECURSION: Code by github/endolith that demonstrates a wrapper that
# does a recursive reduction on an input list:
# https://gist.github.com/endolith/114336
#
# PYTHON LIBRARY: fractions.gcd()
# Return the greatest common divisor of the integers a and b.
# If either a or b is nonzero, then the absolute value of gcd(a, b)
# is the largest integer that divides both a and b. gcd(a,b) has the
# same sign as b if b is nonzero; otherwise it takes the sign of a.
# gcd(0, 0) returns 0.
#
# Concrete Math, Graham, Knuth, Patashnik, pp. 103:
# says gcd(0,0) is undefined, i.e. gcd(0,0):return NaN
# 
# 
#
# Some easy cases:
x = 1000
y = 20
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 12121212
y = 122
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 20
y = 1000
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))


x = 99
y = 11
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

# Edge cases at (0,0), (0,1), (1,0).
# and Off by One cases (3,2), (2,3), (2,1), (1,2), (11,10), (10,11).

x = 0
y = 0
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 0
y = 1
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 1 
y = 0
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 3 
y = 2
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 2 
y = 3
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 2 
y = 1
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 1 
y = 2
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 11
y = 10
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 10 
y = 11
z = 0
z = gcd_euclid(x, y)

print(str(x) + " " +  str(y) + " " + str(z))




