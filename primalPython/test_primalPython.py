#!/usr/bin/env python3

# test_primalPython: Test harness for primalPython.py module.
#    Tests againsts known good data to validate output of functions.
# Implementation (c) 2016,2020 Brig Young (github.com/Sonophoto)
# License: BSD-2c, i.e. Cite.
#

import unittest
import primalPython as pp

class primalTests(unittest.TestCase):
    """
        DOCS
    """

    digit_roots = {0:0, 1:1, 11:2, 111:3, 1111:4, 11111:5, 111111:6, 1111111:7, 11111111:8, 111111111:9,
                   1111111111:1, 99:9, 999:9, 9999:9, 99999:9, 999999:9, 9999999:9, 99999999:9, 
                   999999999:9, 9999999999:9, 9999999999999999999999999999999999999999999999999999999:9}
    digit_sums = {0:0, 1:1, 1111111111:10, 451:10, 99999:54, 999999999999:108,
                  9999999999999999999999:216, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:1008}

#    def test_digitalSum(self):
#        """ Run through a set of precalculated values in self.digital_sums
#        """

    def test_digitalRoot(self):
        """ Run through a set of precalculated values in self.digital_roots
        """
        digitalRoot_domain = self.digit_roots.keys()
        digitalRoot_range = list(self.digit_roots.values())
        output_list = []
        [output_list.append(pp.digitalRoot(x)) for x in digitalRoot_domain]
        print("\n", output_list)
        print("\n", digitalRoot_range)
        self.assertEqual(output_list, digitalRoot_range,
        "digitalRoot() has calculated incorrect values")
     



unittest.main(verbosity=2)

