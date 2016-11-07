#!/usr/bin/env python
#!coding:utf-8

import unittest
import sys

import set_path
from nfa2dfa import NFA


class TestNFA(unittest.TestCase):

    EPSILON = 'epsilon'

    start = 'q0'
    final = {'q1'}
    sigma = ['0', '1', 'epsilon']
    states = ['q0', 'q1', 'q2']
    ttable = [[{'q0', 'q1'}, {'q0'}, {}],
                       [{'q2'}, {'q2'}, {}],
                       [{'q2'}, {'q2'}, {}]]
    nfa = NFA(states, sigma, ttable, start, final)

    def test_transition(self):
        self.nfa.transition('q0', '1')
        self.assertTrue(self.nfa.is_accepted(), True)

if __name__ == "__main__":
    unittest.main()
