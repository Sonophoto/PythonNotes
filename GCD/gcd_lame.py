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


# Some easy cases:
x = 1000
y = 20
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 12121212
y = 122
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 20
y = 1000
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))


x = 99
y = 11
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

# Edge cases at (0,0), (0,1), (1,0).
# and Off by One cases (3,2), (2,3), (2,1), (1,2), (11,10), (10,11).

x = 0
y = 0
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 0
y = 1
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 1 
y = 0
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 3 
y = 2
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 2 
y = 3
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 2 
y = 1
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 1 
y = 2
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 11
y = 10
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))

x = 10 
y = 11
z = 0
z = gcd_lame(x, y)

print(str(x) + " " +  str(y) + " " + str(z))




