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


def gcd_lame(a, b):
    if (a == 0 or b == 0): return 0
    while ( a != b):
        if (a > b):
            if (b == 0): return (a)
            a = a % b
        else:
            if (a == 0): return (b)
            b = b % a
    return a



