# *********************************************************************
print("so on the subject of ternary conditionals...")
#
true_case = "True Case Returned"
false_case = "False Case Returned"
a, b = 0, 1 

for conditional in [0,1]:
    print( (true_case) if (conditional) else (false_case) )

#> False Case Returned
#> True Case Returned

print("")
print("*********************************************************************")
print("Also consider this idiom:")
a, b = 0, 1

out = ("False", "True")[bool(a > b)]
#> out == "False" NOTE! it does not == False ;-)
print(out)

out = ("0", "1")[bool(b > a)]
#> out == "1" NOTE! it does not == 1 ;-)
print(out)

out = ("Down", "Up")[bool(2 > b)]
#> out == "Up" NOTE! it does not == "Cantaloupe Butcher" 
print(out)

# The conditional returns True or False which are equiv to 1 or 0
# which is then used as an index to select one of two values.

print("")
print("*********************************************************************")
print("Now lets kick it up a notch and use references to code()")
a, b = 0, 1

def zerofunc(): return 0
def onefunc(): return 1

print(( zerofunc(), onefunc() )[bool(a > b)] )
#> 0
print(( zerofunc(), onefunc() )[bool(a < b)] )
#> 1
print(( zerofunc(), onefunc() )[bool(a == b)] )
#> 0

# Now we have a bifurcated joint in our code from Anything that has
# a bool(able) value.

print("")
print("*********************************************************************")
print("Now lets kick it up another notch and use references like true madness")
a, b = 0, 1

def twofunc(): return 2
def threefunc(): return 3
def fourfunc(): return 4
def fivefunc(): return 5

my_funcs = (zerofunc(), onefunc(), twofunc(), threefunc(), fourfunc(), fivefunc())


print("")
print("First we print out the native return type which in this case is 'int'")
for x in my_funcs:
   print(x) 

print("")
print("or we can compose with a call to str() to get a string value instead:")
for x in my_funcs:
   print(str(x)) 

print("")
print("...they both look the same on screen...")





