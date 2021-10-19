import unittest
from convex.convex import convex_combs

class CombsTests(unittest.TestCase):

    def test_combs_empty(self):
        output = list(convex_combs([], 5))
        assert(len(output) == 0)

    def tests_combs_negative_n(self):
        output = list(convex_combs([1, 2, 3], -5))
        assert(len(output) == 0)


    
