# *************************************************************************
# How do I use slices to partition a string?
# Use positional indexes of words to return sliced words:

bd = "Blood Thirsty Dinosaur"
b = bd[:5]
t = bd[6:13]
d = bd[-8:]
print(b + "*" + t + "*" + d )


del b, t, d
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


