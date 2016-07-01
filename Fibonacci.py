# Fibonacci Series: Pythonized sequencer
# Implementation (c) 2016 Brig Young (github.com/Sonophoto)

def Fibonacci(N):
    idx, fibp, fib = 1, 0, 1
    if not (N): return (fibp)
    while(True):
        idx, fibp, fib = ((idx + 1), fib, (fibp + fib)) 
        if (idx >= N): return (fib)



if __name__ == "__main__":
# Reference for this Series: https://oeis.org/search?q=fibonacci
# OEIS: Online Encyclopedia of Integer Sequences
# F(n) = (F(n-1) + F(n-2) with F(0) == 0 and F(1) == 1
# F(0) = 0, F(1) == 1, F(2) == 1, F(3) == 2, F(4) == 3, ...
# 0, 1, 1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

    print(  0,  Fibonacci(0),    0)
    print(  1,  Fibonacci(1),    1)
    print(  2,  Fibonacci(2),    1)
    print(  3,  Fibonacci(3),    2)
    print(  4,  Fibonacci(4),    3)
    print(  5,  Fibonacci(5),    5)
    print(  6,  Fibonacci(6),    8)
    print(  7,  Fibonacci(7),   13)
    print(  8,  Fibonacci(8),   21)
    print(  9,  Fibonacci(9),   34)
    print( 10, Fibonacci(10),   55)
    print( 11, Fibonacci(11),   89)
    print( 12, Fibonacci(12),  144)
    print( 13, Fibonacci(13),  233)
    print( 14, Fibonacci(14),  377)
    print( 15, Fibonacci(15),  610)
    print( 16, Fibonacci(16),  987)
