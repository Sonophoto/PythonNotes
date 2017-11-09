#!/usr/bin/env python3
"""
Calculate 2 colour combos from R-O-Y-G-B-Purple

Implementation (c) 2017 Brig Young (github.com/Sonophoto)
License: BSD-2c, i.e. Cite.
"""

warm_colours = ["red", "orange", "yellow"]
cool_colours = ["green", "blue", "purple"]

list_of_colours = []
number_of_colours = 0

# Generate a set of colour tuples and output
for tone in warm_colours:
    for tint in cool_colours:
        list_of_colours.append( (tone, tint) )
        list_of_colours.append( (tint, tone) )
        number_of_colours += 2

# Output tuples as linefeed delimited strings
for output_index in range(number_of_colours):
    output_string = " ".join(str(x) for x in list_of_colours[output_index])
    print(output_string)

