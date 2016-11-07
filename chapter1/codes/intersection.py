#!coding:utf-8

from util import cartesian_list

class Automata(object):
    """Now, dfa supports only single final state
    besides, dfa use transition table to represent itself

    1. states and sigma are ordered lists, because they wil be 
       used by transition table;
    2. transition table is like below:
       1). row is for states, and state order is from states
       2). column is for inputs, and its order is from sigma
       3). table below represents the dfa which accepts even number
           of 1's, states={q1, q2}, sigma={0,1}:
        +-----+-----+-----+
        |     |  0  |  1  |
        +-----+-----+-----+
        | q1  | q1  |  q2 |
        +-----+-----+-----+
        | q2  | q2  |  q1 |
        +-----+-----+-----+
        but, in our automata, we only use
        +-----+-----+
        | q1  |  q2 |
        +-----+-----+
        | q2  |  q1 |
        +-----+-----+
        to represent transition table for brevity
    3. now, it only support the same sigma for two dfa's intersection
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

    def _get_full_ttable(self):
        thead = [' ']
        thead.extend(self.sigma)
        full_tbl = [thead]
        for idx, elem in enumerate(self.ttable):
            tmp = [self.states[idx]]
            tmp.extend(elem)
            full_tbl.append(tmp)
        return full_tbl

    def _get_start(self):
        return self.start

    def _get_final(self):
        return self.final

    def _delta(self, state, input):
        si = self.states.index(state)
        ii = self.sigma.index(input)
        return self.ttable[si][ii]


def intersection(auto1, auto2):
    states = cartesian_list(auto1._get_states(), auto2._get_states())
    sigma = []
    sigma.extend(auto1._get_sigma())
    start = (auto1._get_start(), auto2._get_start())
    final = (auto1._get_final(), auto2._get_final())

    ttable = []
    for idx, st in enumerate(states):
        ttable.append([])
        for ids, sig in enumerate(sigma):
            ttable[idx].insert(ids, (auto1._delta(states[idx][0], sig), auto2._delta(states[idx][1], sig)))
    revised_states = ['q' + str(i) for i, _ in enumerate(states)]
    revised_ttable = []
    for idx, _ in enumerate(ttable):
        revised_ttable.append([])
        for ids, _ in enumerate(ttable[idx]):
            revised_ttable[idx].insert(ids, revised_states[states.index(ttable[idx][ids])])
    revised_start = revised_states[states.index(start)]
    revised_final = revised_states[states.index(final)]
    return Automata(revised_states, sigma, revised_ttable, revised_start, revised_final)
