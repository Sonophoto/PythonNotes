# Warning, this is all VERY Python 3.4+ specific.
# Don't let anyone fool you, 2.7 and 3.4 are different languages...

# *************************************************************************
# How do I use slices to partition a string?
# Use positional indexes of substrings to return sliced strings:
bd = "Blood Thirsty Dinosaur"

# Make a list of words by offsets:
# Note the index (-8) in the last slice is from the end of the string
L1 = [bd[:5], bd[6:13], bd[-8:]]

# Note also that the last index such as (:5) or the 13 in (6:13)
# *Must*Be* one more than the index of the last character you want.
# This is easy to think of as moving just past the character you need
# to capture to the beginning of the next character after it or the 
# end of the string

# You can also print the slices with a secified delimiter:
print([bd[:5] + "*" + bd[6:13] + "*" + bd[-8:]])

# Or use a manual CSV:
print('"' + str(bd[:5]) + '","' + str(bd[6:13]) + '","' + str(bd[-8:]) + '"')

# Or a simple manual JSON list of string values:
print('["' + str(bd[:5]) + '","' + str(bd[6:13]) + '","' + str(bd[-8:]) + '"]')

# Or just put it back together the way we found it:
new_bd = ' '.join(x for x in L1)

# Lets make sure they are the same:
if (new_bd == bd): print("Hooray!")


del L1, bd, new_bd
# *************************************************************************
# How do I print out a list of strings?
# You can print it directly, element by element, or join() it into a str.
# You could even use a completion
bd = "Blood Thirsty Dinosaur"
L1 = [bd[:5], bd[6:13], bd[-8:]]

print(L1)

for x in L1: print(x)

print(" ".join(x for x in L1))

DevNull = [print(x) for x in L1]

DevNull = [print(x, end=' ') for x in L1]


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
# Use the .format(**kwargs) method:

D1 = {"temp": str(28), "humid": str(77), "pres": str(1066)}
s1 = "Local Weather: Temperature: {temp}, Humidity: {humid}, Pressure: {pres}"
s1.format(**D1)


