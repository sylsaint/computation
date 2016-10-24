#!coding:utf-8

class Automata(object):
    """Now, dfa supports only single final state
    besides, dfa use transition table to represent itself
    """
    def __init__(self, states, sigma, ttable, start, final):
        self.start = start
        self.final = final
        self.states = states
        self.sigma = sigma
        self.ttable = ttable

    def _get_states(self):
        return self.states

    def _get_sigma(self):
        return self.sigma

    def _get_ttable(self):
        return self.ttable

    def _get_start(self):
        return self.start

    def _get_final(self):
        return self.final

    def _delta(self, state, input):
        si = self.states.index(state)
        ii = self.sigma.index(input)
        return self.ttable[si][ii]
