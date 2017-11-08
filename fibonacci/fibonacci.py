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


if __name__ == "__main__":

    import unittest

    class FibonacciTests(unittest.TestCase):
        """Test all Fibonacci functions against a list of known Fibonacci numbers
           Values indexed  0 - 38 are from OEIS https://oeis.org/search?q=fibonacci
                          39 - 50 manually calculated and verified by Brig Young
        """

        fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,\
                55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,\
                6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,\
                317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,\
                9227465, 14930352, 24157817, 39088169, 63245986, 102334155,\
                165580141, 267914296, 433494437, 701408733, 1134903170,\
                1836311903, 2971215073, 4807526976, 7778742049, 12586269025]
        """A curated list of Fibonacci numbers with correctly matched indexes
        """

        def test_Sequencer(self):
            """Create a list of fibonacci numbers via sequencing over count of known
               good values and compare to list of known good values.
            """
            sequenced_list = []
            [sequenced_list.append(fibonacciSequencer(x)) for x in range(len(self.fibs))]
            self.assertEqual(sequenced_list, self.fibs,\
            "fibonacciSequencer() has calculated incorrect values")

        def test_Generator(self):
            """Create a list of fibonacci numbers via a python generator indexed by
               count of known good values and compare to list of known good values.
            """
            generated_list = []
            fibgen = fibonacciGenerator()
            [generated_list.append(next(fibgen)) for x in range(len(self.fibs))]
            self.assertEqual(generated_list, self.fibs,\
            "fibonacciGenerator() has caculated incorrect values")

        def test_ClosedForm(self):
            """Create a list of fibonacci numbers via closed form equation indexed by
               count of known good values and compare to list of known good values.
            """
            closedform_list = []
            [closedform_list.append(fibonacciClosedForm(x)) for x in range(len(self.fibs))]
            self.assertEqual(closedform_list, self.fibs,\
            "fibonacciClosedForm() has calculated incorrect values")

        def test_NaiveRecursion(self):
            """Create a list of fibonacci numbers via naive recursion indexed by
               count of known good values and compare to list of known good values.
            """
            fibs_short_list = self.fibs[:20]
            recursion_list = []
            [recursion_list.append(fibonacciNaiveRecursion(x)) for x in range(len(fibs_short_list))]
            self.assertEqual(recursion_list, fibs_short_list,\
            "fibonacciRecursion() has calculated incorrect values")


    unittest.main()

