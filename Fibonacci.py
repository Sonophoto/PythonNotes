# Fibonacci Series: Pythonized sequencer
# Implementation (c) 2016 Brig Young (github.com/Sonophoto)
# License: BSD-2c, i.e. Cite.

def Fibonacci(N):
    """Fibonacci Sequencer, generates f(N) per:www.oeis.org/"""
    fibp, fib = 0, 1
    if (N == fibp): return (fibp)
    while(N > 1): 
        N, fibp, fib = (N - 1), fib, (fibp + fib) 
    return (fib)



if __name__ == "__main__":
# Reference for this Series: https://oeis.org/search?q=fibonacci
# OEIS: Online Encyclopedia of Integer Sequences
# F(n) = (F(n-1) + F(n-2) with F(0) == 0 and F(1) == 1
# F(0) = 0, F(1) == 1, F(2) == 1, F(3) == 2, F(4) == 3, ...
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

    for x in range(17):
        print( x, Fibonacci(x), fibs[x]) 
