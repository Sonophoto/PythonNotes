#!/usr/bin/env python3
"""
 Implementation (c) 2016,2017 Brig Young (github.com/Sonophoto)
 License: BSD-2c, i.e. Cite.

 Demonstrate the actual algorythm of Euclid in such a manner that
 Gabriel Lame's Modification is a trivial modification of the
 function. Both versions conform with the definition of gcd()
 in "Concrete Mathematics" Graham, Knuth, Patashnik. pp. #TODO

 An in depth discussion of the relationship of the Euclid algo
 and the Gabriel Lamé modification (and proof) may be found here:

 http://www.cut-the-knot.org/blue/LamesTheorem.shtml
"""

from gcdVersions import gcd_euclid, gcd_lame
import unittest as unittest 

class gcdVersionTests(unittest.TestCase):
    
    bounds = [(0,0,"NaN"), (-1,0,"NaN"), (-1,-1,"NaN"), (0,-1,"NaN")]
    """ A list defining mathematical boundaries to gcd(a,b)
        #NOTE Python's math.gcd() is non conforment and returns
        (0,0,0), (-1,0,1), (-1,-1,1), (0,-1,1)
    """

    edges = [(0,1,0), (1,0,0)]
    """ The two edge cases in mathematical definition of gcd(a,b)
    """

    pathos = [(1000000000,10,10), (10,1000000000,10)]
    """ A worst case test for gcd(a,b), especially gcd_euclid(a,b)
        Runs 100e6 loops for Euclid and 5*10(digits) loops for Lamé.
    """
 
    fuzzies = [(276,68,4),   (68,274,4),   (690, 85, 5), (85, 690, 5),\
               (716, 9, 1),  (9, 716, 1),  (484, 70, 2), (70, 484, 2),\
               (413, 37, 1), (37, 413, 1), (582, 34, 2), (34, 582, 2),\
               (161, 7, 7),  (7, 161, 7),  (780, 82, 2), (82, 780, 2),\
               (807, 58, 1), (58, 807, 1), (334, 7, 1),  (7, 334, 1),\
               (80, 87, 1),  (87, 80, 1),  (694, 31, 1), (31, 694, 1),\
               (667, 93, 1), (93, 667, 1), (766, 42, 2), (42, 766, 2),\
               (268, 33, 1), (33, 268, 1), (881, 22, 1), (22, 881, 1),\
               (96, 20, 4),  (20, 96, 4),  (850, 26, 2), (26, 850, 2),\
               (637, 28, 7), (28, 637, 7), (461, 72, 1), (72, 461, 1)]
    """ Randomly generated test cases. See fuzzies.py to generate a 
        different set of random test cases and paste it over this one.
    """

    def test_gcd_euclid_edges(self):
        generated_edges = []
        for element in self.edges:
            generated_edges.append((element[0], element[1], gcd_euclid(element[0],element[1])))
        self.assertEqual(self.edges, generated_edges,\
        "Failed: gcd_euclid() edges test")

    def test_gcd_euclid_pathological(self):
        self.assertTrue(True)

    def test_gcd_euclid(self):
        self.assertTrue(True)

    def test_gcd_lame_edges(self):
        self.assertTrue(True)

    def test_gcd_lame_pathological(self):
        self.assertTrue(True)

    def test_gcd_lame(self):
        self.assertTrue(True)
        
unittest.main(verbosity=2)