#!coding:utf-8

from intersection import *

# automata recognizes even a's
states1 = ['q0', 'q1']
sigma1 = ['a', 'b']
start1 = states1[0]
final1 = states1[0]
ttable1 = [['q1', 'q0'], ['q0', 'q1']]

auto1 = Automata(states1, sigma1, ttable1, start1, final1)

# automata recognizes odd a's
states2 = ['q0', 'q1', 'q2']
sigma2 = ['a', 'b']
start2 = states2[0]
final2 = states2[1]
ttable2 = [['q0', 'q1'], ['q1', 'q2'], ['q2', 'q1']]

auto2 = Automata(states2, sigma2, ttable2, start2, final2)

combined_auto = intersection(auto1, auto2)

print('start', combined_auto._get_start())
print('final', combined_auto._get_final())
for idx, elem in enumerate(combined_auto._get_full_ttable()):
    print(elem)
