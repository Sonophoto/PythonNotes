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

def fibonacciSequencer(N):
    """Fibonacci Sequencer, returns f(N) per:www.oeis.org/
       Performance is O(N) from calculating (N) by sequencing.
    """
    if (N < 0): return (-1)
    fibp, fib = 0, 1
    if (N == fibp): return (fibp)
    while(N > 1):
        N, fibp, fib = (N - 1), fib, (fibp + fib)
    return (fib)

def fibonacciClosedForm(N):
    """Fibonacci Function uses closed form equation to return fibonacci(N)
       This function is O(Constant) for any N.
    """
    return(int(1/sqrt(5) * ((((1+sqrt(5))/2)**N)-(((1-sqrt(5))/2)**N))))


def fibonacciGenerator():
    """Fibonacci Generator, yields next Fibonacci number on each call
       Performance is O(N) from calculating in sequence.
    """
    n = 0
    while True:
        yield int(1/sqrt(5) * ((((1+sqrt(5))/2)**n)-(((1-sqrt(5))/2)**n)))
        n = n + 1

def fibonacciNaiveRecursion(N):
    """Fibonacci Recursion uses naive recursion to calculate fibonacci(N)
       Performance is O(Really Bad) from deep call stacks on N > 30
    """
    if (N == 0):
        return (0)
    elif (N == 1):
        return (1)
    else:
        return(fibonacciNaiveRecursion(N-1) + fibonacciNaiveRecursion(N-2))

