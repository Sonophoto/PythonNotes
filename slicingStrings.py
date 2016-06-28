# *************************************************************************
# How do I use slices to partition a string?
# Use positional indexes of substrings to return sliced strings:

bd = "Blood Thirsty Dinosaur"
# Make a list of words by offsets:
L1 = [bd[:5], bd[6:13], bd[-8:]]

# or print them out directly:
print([bd[:5] + "*" + bd[6:13] + "*" + bd[-8:]])


# *************************************************************************
# How do I print out a list of strings?
# You can print it directly, element by element, or join() it into a str.
# You could even use a completion
print(L1)

for x in L1: print(x)

print(" ".join(x for x in L1))

DevNull = [print(x) for x in L1]

del L1, bd, x, DevNull
# *************************************************************************
# How do I find out if a substring is in a list? (True or False)
# use the 'in' operator:

L1 = "After this substring - Print Everything Else".split(" ")
Boolean_answer = "substring" in L1


del L1, Boolean_answer
# *************************************************************************
# How do I return the location of a substring in a string?
# Use the str.index(str) method:

s1 = "After this substring - Print Everything Else"
s2 = "substring"
s1_idx_of_s2 = s1.index(s2)


del s1, s2, s1_idx_of_s2
# *************************************************************************
# How do I find out how long a string is?
# use the len() function

s1 = "After this substring - Print Everything Else"
length_of_s1 = len(s1)


del s1, length_of_s1
# *************************************************************************
# How do I return the rest of a string after some substring?
# Use str.index(), add length of "substring", use this offset to slice it:

s1 = "After this substring - Print Everything Else"
s2 = "substring"
s3 = s1[s1.index(s2) + len(s2):]


del s1, s2, s3
# *************************************************************************
# How do I convert a list of ints into a space delimited string of numbers?
# compose a call to " ".join() with a list completion:

L1 = [1, 22, 13, 42, 451, 66, 7, 8, 1999]
s1 = " ".join(str(x) for x in L1)


del L1, s1
# *************************************************************************
# How do I convert a space delimeted string of numbers into a list of ints?
# Use a list completion to generate a list from str.split()
# (It is usually better to use regexes on real data)

s1 = "1 22 13 42 451 66 7 8 1999"
L1 = [int(x) for x in s1.split(" ")]


del L1, s1
# *************************************************************************
# How do I parameterize a string with a dictionary of values?
# Use the .format() method:

D1 = {"temp": str(28), "humid": str(77), "pres": str(1066)}
s1 = "Local Weather: Temperature: {temp}, Humidity: {humid}, Pressure: {pres}"
s1.format(**D1)


