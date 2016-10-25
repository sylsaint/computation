from intersection import *

# automata recognizes at least two 0's
states1 = ['q0', 'q1', 'q2']
sigma1 = [0, 1]
start1 = states1[0]
final1 = states1[2]
ttable1 = [['q1', 'q0'], ['q2', 'q1'], ['q2', 'q2']]

auto1 = Automata(states1, sigma1, ttable1, start1, final1)

# automata recognizes at most one  1
states2 = ['q0', 'q1', 'q2']
sigma2 = [0, 1]
start2 = states2[0]
final2 = states2[1]
ttable2 = [['q0', 'q1'], ['q1', 'q2'], ['q2', 'q2']]

auto2 = Automata(states2, sigma2, ttable2, start2, final2)

combined_auto = intersection(auto1, auto2)

print('start', combined_auto._get_start())
print('final', combined_auto._get_final())
for idx, elem in enumerate(combined_auto._get_full_ttable()):
    print(elem)
