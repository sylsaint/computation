#!/usr/bin/env python
#!coding:utf-8

"""
NFA to DFA by subset construction

Given: one NFA
Goal: convert NFA to an equivalent DFA
Approach: Consider simulating a NFA

Representation of NFA, N = {Q, \Sigma, \delta, q_0, F}, transition table is used for \delta.

|      | 0          | 1     | \epsilon |
+--------------------------------------+
|->q_0 | {q_0, q_1} | {q_1} | {}       |
+--------------------------------------+
| *q_1 | {q_0, q_1} | {q_1} | {}       |
+--------------------------------------+

For any transition in NFA,
1. e-close(s) is used for single state s
2. e-close(S) is used for set of states S

recursively using this method until there is no new state found.

Work with sets of states.
IDEA: each state in the DFA will correspond to a set of states in NFA
Time-complexity:
    worst case is O(2^n), but in the normal circumstance, states will be much less than it.
"""

class NFA(object):

    EPSILON = 'epsilon'

    def __init__(self, Q, sigma, ttable, q0, F):
        self.Q = Q
        self.sigma = sigma
        self.ttable = ttable
        self.q0 = q0
        self.F = F
        self.current = {self.q0}

    def _states(self):
        return self.Q

    def _sigma(self):
        return sigma

    def _start(self):
        return self.q0

    def _final(self):
        return self.F

    def transition(self, q, a):
        # TODO add logic
        # if a is not epsilon, but get_ttable_elem is empty set, we
        # should not add q to the result set.
        if a == self.EPSILON:
            final_set = self._eclose(q)
            self.current = final_set
            return final_set
        else:
            trans_set = set()
            ep_set = self._eclose(q)
            trans_set = trans_set.union(self._get_ttable_set(ep_set, a))
            final_set = self._eclose_set(trans_set)
            self.current = final_set
            return final_set

    def transitions(self, qs, a):
        trans_set = set()
        for q in qs:
            trans_set = trans_set.union(self.transition(q, a))
        self.current = trans_set
        return trans_set

    def _get_ttable_elem(self, q, a):
        st_index = self.Q.index(q)    # make sure q is in the self.Q
        ep_index = self.sigma.index(a)
        return self.ttable[st_index][ep_index]

    def _get_ttable_set(self, qs, a):
        trans_set = set()
        for q in qs:
            trans_set = trans_set.union(self._get_ttable_elem(q, a))
        return trans_set

    # epsilon set for single state
    # epsilon transition should include itself
    def _eclose(self, q):
        epsilon_set = self._get_ttable_elem(q, self.EPSILON)
        ep_set = set()
        if bool(epsilon_set):
            self._depth_first_search(epsilon_set, ep_set)
        ep_set.add(q)
        return ep_set

    def _eclose_set(self, qs):
        ep_set = set()
        self._depth_first_search(qs, ep_set)
        return ep_set

    # epsilon set for state set
    def _depth_first_search(self, qs, ep_set):
        if not bool(qs):
            return set()
        for q in qs:
            ep_set.add(q)
            epsilon_set = self._get_ttable_elem(q, self.EPSILON)
            if bool(epsilon_set):
                self._depth_first_search(epsilon_set, ep_set)
        return ep_set

    def handle(self, w):
        for char in w:
            self.transitions(self.current, char)
        return self.current

    def reset(self):
        self.current = {self.q0}

    # @return {set}
    def current(self):
        return self.current

    def is_accepted(self):
        intersect = self.current.intersection(self.F)
        return bool(intersect)
