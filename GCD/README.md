[![Build Status](https://travis-ci.org/Sonophoto/PythonNotes.svg?branch=master)](https://travis-ci.org/Sonophoto/PythonNotes)

# GCD: Greatest Common Divisor

## A study of The OG algorithm with modern variations

### Non-recursive Style Euclid
Return the greatest common divisor of the integers a and b by subtractive reduction of the smallest current value from the largest current value until a==b or a==b==1. This function only works on positive values or zero and (0,0) is undefined.

### Non-recursive Style Lame
Return the greatest common divisor of the integers a and b by modulo division of the largest current value by the smallest current value until a==b or a==b==1. This function only works on positive values or zero and (0,0) is undefined.

### Python3 built-in math.gcd()
Return the greatest common divisor of the integers a and b.
gcd(a,b) has the same sign as b if b is nonzero;
otherwise it takes the sign of a.
gcd(0, 0) returns 0.

Concrete Math, Graham, Knuth, Patashnik, pp. 103:
says gcd(0,0) is undefined, i.e. gcd(0,0):return NaN

### Recursive gcd([list]) (This is not included in our tests)
This is an intersting gist that demonstrates a wrapper that
does a recursive reduction on an input list using math.gcd():
https://gist.github.com/endolith/114336





