import unittest
import sys
import os
import pprint

# set current dir's parent dir to the pythonpath
import set_path

# config pprint
pp = pprint.PrettyPrinter(indent=4, width=30)

from intersection import Automata, intersection
from util import cartesian_list

class TestAutomata(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_upper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_delta(self):
        start = 'q1'
        final = 'q1'
        states = ['q1', 'q2']
        sigma = [0, 1]
        ttable = [[states[0], states[1]], [states[1], states[0]]]
        auto = Automata(states, sigma, ttable, start, final)

        self.assertEqual(start, auto._delta(start, 0))

    def test_cartesian(self):
        lst1 = [ 1, 2, 3 ]
        lst2 = [ 4, 5, 6 ]
        self.assertEqual(len(cartesian_list(lst1, lst2)), 9)
        self.assertEqual(cartesian_list(lst1, lst2)[0], (1,4))

    def test_intersection(self):
        start = 'q1'
        final = 'q1'
        states = ['q1', 'q2']
        sigma = [0, 1]
        ttable = [[states[0], states[1]], [states[1], states[0]]]
        auto1 = Automata(states, sigma, ttable, start, final)
        ttable2 = [[states[1], states[0]], [states[0], states[1]]]
        auto2 = Automata(states, sigma, ttable2, start, final)
        inter_auto = intersection(auto1, auto2)
        for idx, elem in enumerate(inter_auto._get_full_ttable()):
            pp.pprint(inter_auto._get_full_ttable()[idx])
        final = inter_auto._get_final()

        self.assertEqual(4, len(inter_auto._get_states()))
        self.assertEqual(final, inter_auto._get_ttable()[1][0])
        self.assertEqual(final, inter_auto._get_ttable()[2][1])


if __name__ == "__main__":
    unittest.main()
