#!/usr/bin/env python
#!coding:utf-8

import unittest
import sys

import set_path
from nfa import NFA


class TestNFA(unittest.TestCase):

    EPSILON = 'epsilon'

    start = 'q0'
    final = {'q0'}
    sigma = ['0', '1', 'epsilon']
    states = ['q0', 'q1', 'q2']
    ttable = [[{}, {'q1'}, {'q2'}],
              [{'q1', 'q2'}, {'q2'}, {}],
              [{'q0'}, {}, {}]]
    nfa = NFA(states, sigma, ttable, start, final)

    def test_e_transition(self):
        self.nfa.transition('q0', self.EPSILON)
        self.assertEqual(self.nfa.is_accepted(), True)

    def test_1_transition(self):
        self.nfa.transition('q0', '1')
        self.assertEqual(self.nfa.is_accepted(), False)

    def test_multi_transition(self):
        self.nfa.transitions({'q0', 'q2'}, '1')
        self.assertEqual(self.nfa.is_accepted(), False)
        self.assertSetEqual(self.nfa.current, {'q1'})

    def test_sequence_110(self):
        self.nfa.reset()
        self.nfa.handle('110')
        self.assertEqual(self.nfa.is_accepted(), True)
        self.assertSetEqual(self.nfa.current, {'q0', 'q2'})

    def test_sequence_100(self):
        self.nfa.reset()
        self.nfa.handle('100')
        self.assertEqual(self.nfa.is_accepted(), True)
        self.assertSetEqual(self.nfa.current, {'q0', 'q1', 'q2'})

    def test_sequence_000(self):
        self.nfa.reset()
        self.nfa.handle('000')
        self.assertEqual(self.nfa.is_accepted(), True)
        self.assertSetEqual(self.nfa.current, {'q0', 'q2'})

    def test_sequence_111(self):
        self.nfa.reset()
        self.nfa.handle('111')
        self.assertEqual(self.nfa.is_accepted(), False)
        self.assertSetEqual(self.nfa.current, set())

if __name__ == "__main__":
    unittest.main()
