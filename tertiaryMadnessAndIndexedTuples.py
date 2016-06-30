# *********************************************************************
# so on the subject of ternary conditionals...
#
true_case = "True Case Returned"
false_case = "False Case Returned"
a, b = 0, 1 

for conditional in [0,1]:
    print( (true_case) if (conditional) else (false_case) )

#> False Case Returned
#> True Case Returned

# *********************************************************************
# Also consider this idiom:

out = ("False", "True")[bool(a > b)]
#> out == "False" NOTE! it does not == False ;-)
out = ("0", "1")[bool(b > a)]
#> out == "1" NOTE! it does not == 1 ;-)
out = ("Down", "Up")[bool(2 > b)]
#> out == "Up" NOTE! it does not == "Cantaloupe Butcher" 

# The conditional returns True or False which are equiv to 1 or 0
# which is then used as an index to select one of two values.

# *********************************************************************
# Now lets kick it up a notch and use references to code()
def zerofunc() return 0
def onefunc(): return 1

print(( zerofunc(), onefunc() )[bool(a > b)] )
#> 0
print(( zerofunc(), onefunc() )[bool(a < b)] )
#> 1
print(( zerofunc(), onefunc() )[bool(a == b)] )
#> 0

# Now we have a bifurcated joint in our code from Anything that has
# a bool(able) value.
