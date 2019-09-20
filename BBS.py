import time
import copy
from line_profiler import LineProfiler


class G(object):
    """
    System G with properties transitions and partition(block),
    as the input of bbs function.
    """
    def __init__(self, transitions, partition):
        self.transitions = transitions
        self.partition = partition

# Test examples, where 0 represents the tao transition


G_test = G(transitions=[(1, 0, 2), (2, 0, 3), (3, 0, 4), (3, 6, 1), (4, 0, 5), (4, 6, 2), (5, 0, 6), (5, 6, 3), (6, 0, 7), (6, 6, 4), (7, 0, 8), (7, 6, 5), (8, 0, 9), (8, 6, 6), (9, 0, 10), (9, 6, 7), (10, 0, 11), (10, 6, 8), (11, 0, 12), (11, 6, 9), (12, 6, 10)],
            partition=[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
Buffer2 = G(transitions=[(1, 0, 2), (2, 2, 1), (2, 0, 3),
                         (3, 3, 2), (3, 0, 4), (4, 4, 3),
                         (4, 0, 5), (5, 5, 4), (5, 0, 6),
                         (6, 6, 5), (6, 0, 7), (7, 7, 6),
                         (7, 0, 8), (8, 8, 7), (8, 0, 9),
                         (9, 9, 8), (9, 0, 10), (10, 10, 9),
                         (10, 0, 11), (11, 11, 10), (11, 0, 12),
                         (12, 12, 11), (12, 0, 13), (13, 13, 12),
                         (13, 0, 14), (14, 14, 13), (14, 0, 15),
                         (15, 15, 14), (15, 0, 16), (16, 16, 15),
                         (16, 0, 17), (17, 17, 16), (17, 0, 18),
                         (18, 18, 17), (18, 0, 19), (19, 19, 18),
                         (19, 0, 20), (20, 20, 19)],
            partition=[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],)
G25 = G([(1, 1, 2), (2, 1, 3), (1, 3, 3),
        (3, 1, 4), (4, 2, 5), (5, 1, 6),
        (6, 2, 7), (4, 4, 7), (7, 3, 7)], [3, 3, 3, 3, 3, 3, 3])

G24 = G([(1, 1, 2), (2, 1, 3), (3, 1, 4),
        (4, 2, 4), (2, 1, 5), (5, 1, 6),
        (6, 1, 7), (7, 2, 7)], [2, 2, 2, 2, 2, 1, 1])

G23 = G([(1, 1, 2), (1, 1, 3), (1, 10, 4),
        (3, 10, 4), (4, 1, 2), (4, 1, 1),
        (2, 10, 2)], [2, 2, 2, 2])

G22 = G([(1, 6, 2), (2, 1, 3), (2, 1, 4),
        (2, 10, 5), (4, 10, 5), (5, 1, 3),
        (5, 1, 1), (3, 10, 3)], [2, 2, 1, 2, 2])

G21 = G([(1, 1, 2), (1, 2, 4), (1, 1, 3),
        (2, 2, 2), (2, 2, 4), (3, 2, 3),
        (4, 1, 1), (4, 1, 3)], [2, 2, 1, 2])

G20 = G([(1, 2, 2), (1, 3, 3), (2, 4, 4),
         (2, 4, 5), (2, 4, 6), (3, 4, 7),
         (3, 4, 8), (3, 4, 9), (4, 5, 4),
         (5, 5, 5), (6, 5, 6), (7, 5, 7),
         (8, 5, 8), (9, 5, 9)], [4, 4, 4, 1, 1, 2, 1, 2, 2])

G19 = G([(1, 1, 2), (2, 2, 3), (1, 2, 3),
         (1, 1, 4), (3, 1, 4), (4, 2, 4)], [2, 2, 2, 1])

G18 = G([(1, 0, 2), (2, 2, 3), (1, 2, 3)], [0, 0, 0])

G17 = G([(1, 0, 2), (1, 0, 3), (2, 2, 2), (3, 3, 3)], [2, 2, 2])

G16_prime = G([(1, 2, 2), (2, 0, 3), (3, 0, 3),
               (1, 0, 4), (4, 0, 5), (5, 0, 5)], [2, 2, 2, 2, 2])

G16 = G([(1, 2, 2), (2, 0, 3), (3, 0, 3),
         (1, 0, 4), (4, 0, 5), (5, 0, 5)], [2, 2, 2, 1, 1])

G15_prime = G([(1, 2, 2), (2, 0, 4), (1, 0, 3), (3, 0, 4)], [2, 2, 1, 2])

G15 = G([(1, 2, 2), (2, 0, 4), (1, 0, 3), (3, 0, 4)], [2, 2, 2, 2])

G14 = G([(1, 0, 2), (2, 2, 3), (1, 0, 3),
         (3, 0, 4), (4, 3, 4)], [2, 2, 2, 1])

G13 = G([(1, 0, 2), (2, 2, 3), (1, 0, 4),
         (4, 2, 3), (3, 3, 3)], [2, 2, 2, 1])

G12 = G([(1, 0, 2), (2, 2, 3), (1, 0, 3), (3, 3, 3)], [1, 1, 1])

G11 = G([(1, 0, 2), (2, 0, 2), (1, 0, 3), (3, 0, 3)], [2, 1, 2])

G10 = G([(1, 0, 2), (2, 2, 3), (3, 3, 3)], [2, 2, 2])

G9 = G([(1, 0, 1), (1, 2, 1)], [2])

G8 = G([(3, 3, 3), (4, 3, 4)], [1, 1, 0, 0])

G_onetrans = G([(1, 1, 1)], [0])

G_notrans = G([], [2])

G7 = G([(1, 0, 2), (2, 0, 1), (2, 0, 3),
        (3, 0, 4), (4, 0, 5), (5, 0, 3),
        (5, 0, 6), (6, 0, 6)], [2, 2, 3, 3, 3, 1])

G6 = G([(1, 0, 2), (2, 0, 1), (2, 0, 4),
        (4, 0, 2), (1, 0, 3), (3, 0, 4),
        (4, 0, 5), (5, 0, 5)], [2, 2, 0, 2, 3])

G5 = G([(1, 0, 2), (2, 0, 1), (2, 0, 4),
        (1, 0, 3), (3, 0, 4), (4, 0, 4)], [2, 2, 0, 2])

G4 = G([(1, 0, 2), (2, 0, 3), (2, 0, 4),
        (3, 0, 3), (4, 0, 4)], [0, 0, 1, 1])

G3 = G([(1, 0, 2), (2, 0, 3), (3, 0, 3)], [1, 1, 1])


G2 = G([(1, 2, 2), (2, 3, 3), (3, 2, 3)], [1, 1, 1])

G1 = G([(1, 0, 2), (2, 0, 3), (3, 2, 3)], [1, 1, 1])

# BBS function


def bbs_org(g):
    start = time.time()
    # Initialize
    pi = g.partition
    pi_0 = set()
    transition_pi = []
    iteration = 0
    # Get all the states in the system
    g.states = [x for x in range(1, len(g.partition) + 1)]
    t = g.states
    # Get pi transitions
    for i in range(0, len(g.transitions)):
        if g.transitions[i][1] == 0:
            transition_pi.append(g.transitions[i])

    while pi != pi_0:
        iteration += 1
        # Get invisible & visible transitions
        transition_inv = []
        for i in range(0, len(transition_pi)):
            if g.partition[transition_pi[i][0] - 1] == g.partition[transition_pi[i][2] - 1]:
                transition_inv.append(transition_pi[i])

        transition_v = list(set(g.transitions) - set(transition_inv))
        # Implementation of line 6-9 of the algorithm
        gamma_pi = [0 for i in range(0, len(g.partition))]

        c1 = [[] for i in range(0, len(g.partition))]

        for i in range(0, len(g.partition)):
            for j in range(0, len(transition_inv)):
                if transition_inv[j][2] == i+1:
                    c1[i] = set(c1[i]) | {transition_inv[j][0]}
            gamma_pi[i] = set()

        # Implementation of line 10-21 in the algorithm
        c = [set() for i in range(0, len(g.partition))]

        delta_c = [set() for i in range(0, len(g.partition))]

        delta_c_prime = [set() for i in range(0, len(g.partition))]

        for i in range(0, len(transition_v)):
            y = transition_v[i][0]
            a = transition_v[i][1]
            y_prime = transition_v[i][2]
            c[y - 1] = {y}
            delta_c[y - 1] = c[y - 1]
            while len(delta_c[y - 1]):
                delta_c_prime[y - 1] = set()
                for j in range(0, len(delta_c[y - 1])):
                    x = list(delta_c[y - 1])[j]
                    gamma_pi[x - 1] = gamma_pi[x - 1] | {(a, g.partition[y_prime - 1])}
                    delta_c_prime[y - 1] = delta_c_prime[y - 1] | set(c1[x - 1])
                delta_c[y - 1] = delta_c_prime[y - 1] - c[y - 1]
                c[y - 1] = c[y - 1] | delta_c[y - 1]
        # Give the empty sets in gamma_pi special marks
        for i in range(0, len(gamma_pi)):
            if not gamma_pi[i]:
                gamma_pi[i] = {(-1, g.partition[i])}
        gamma_pi = list(map(sorted, gamma_pi))
        pi_0 = copy.copy(pi)
        # Build a hash table, using dict
        val = 0
        ht = {}
        # Key in the hash table, block of state added.
        gamma_pi_ht = [[gamma_pi[x], g.partition[x]] for x in range(0, len(gamma_pi))]

        for i in range(0, len(g.states)):
            if not str(gamma_pi_ht[i]) in ht:
                val += 1
                ht[str(gamma_pi_ht[i])] = val
            pi[i] = ht[str(gamma_pi_ht[i])]
    end = time.time()
    # print("\npi_org", pi)
    print("\niter_org", iteration)
    print("time_org", end - start)
    return pi

# Compute execution time.

# The bbs function is called for 1000 times,
# or the time.time() function will return 0 instead.

# So the time can be read as in unit of millisecond.

"""
def test_performance(g):
    for i in range(1000):
        bbs_org(g)


start = time.time()
test_performance(Buffer2)
end = time.time()
print("", end - start)

lp = LineProfiler()
lp_wrapper = lp(bbs_org)
lp_wrapper(Buffer2)
lp.print_stats()
"""
# bbs_org(G_test)








