# Fibonacci Series:  
# Implementation (c) 2016,2017 Brig Young (github.com/Sonophoto)
# License: BSD-2c, i.e. Cite.
#
# Reference for this Series: https://oeis.org/search?q=fibonacci
# OEIS: Online Encyclopedia of Integer Sequences
# F(n) = (F(n-1) + F(n-2) with F(0) == 0 and F(1) == 1
# F(0) = 0, F(1) == 1, F(2) == 1, F(3) == 2, F(4) == 3, ...

# Thanks to http://gozips.uakron.edu/~crm23/fibonacci/fibonacci.htm
# for the closed form of the Fibonacci sequence used in the generator.

from math import sqrt

def fibonacciIteration(N):
    """Fibonacci Sequencer, returns f(N) per:www.oeis.org/"""
    if (N < 0): return (-1)
    fibp, fib = 0, 1
    if (N == fibp): return (fibp)
    while(N > 1):
        N, fibp, fib = (N - 1), fib, (fibp + fib)
    return (fib)

def fibonacciGenerator():
    """Fibonacci Generator, yields next Fibonacci number on each call"""
    n = 0
    while True:
        yield int(1/sqrt(5) * ((((1+sqrt(5))/2)**n)-(((1-sqrt(5))/2)**n)))
        n = n + 1

# TODO def fibonacciRecursion():


if __name__ == "__main__":

    """ 51 Fibonacci numbers: Values indexed 0 - 38 are from OEIS (link above),
        39 - 50 manually verified by Brig Young"""
    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,\
            55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,\
            6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,\
            832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,\
            39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733,\
            1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]
 
    print("Testing fibonacciIteration(N)")
    print("Index, fibonacci[Index], fibonacciIteration(Index)")
    [print( x, fibonacciIteration(x), fibs[x]) for x in range(len(fibs))]

    print("Testing fibonacciGenerator")
    print("Index, fibonacci[Index], fibonacciGenerator()")
    fibgen = fibonacciGenerator()
    [print(x, fibs[x], next(fibgen)) for x in range(len(fibs))]





