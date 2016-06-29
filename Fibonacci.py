# Reference: https://oeis.org/search?q=fibonacci
# F(n) = (F(n-1) + F(n-2) + ... + F(n-n)
# F(0) = 0, F(1) == 1, F(2) == 1, F(3) == 3
# 0, 1, 1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 
def Fibonacci(N):
    idx, np, nn, fibnum = 1, 0, 1, 0
    if not (N): return (fibnum)
    
    while(True):
        fibnum = (np + nn)
        np, nn, idx = (nn, fibnum, (idx + 1))
        if (idx >= N):
            return (fibnum)

if __name__ == "__main__":

    print(  0,  Fibonacci(0) )
    print(  1,  Fibonacci(1) )
    print(  2,  Fibonacci(2) )
    print(  3,  Fibonacci(3) )
    print(  4,  Fibonacci(4) )
    print(  5,  Fibonacci(5) )
    print(  6,  Fibonacci(6) )
    print(  7,  Fibonacci(7) )
    print(  8,  Fibonacci(8) )
    print(  9,  Fibonacci(9) )
    print( 10, Fibonacci(10) )
    print( 11, Fibonacci(11) )
    print( 12, Fibonacci(12) )
