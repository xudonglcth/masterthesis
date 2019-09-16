import numpy as np
import copy as cp
import profile


class G(object):
    def __init__(self, transition, block, tau, initial):
        self.transition = transition
        self.block = block
        self.tau = tau
        self.initial = initial


def rearrange(a):
    d = dict()
    k = 0
    for i in range(len(a)):
        if not a[i] in d:
            k += 1
            d[a[i]] = k
    for i in range(len(a)):
        a[i] = d[a[i]]
    return a


def bbs_abstraction(g):
    if len(g.transition) == 0:
        return rearrange(g.block)
    n = len(g.block)
    pi = np.array(g.block, int)
    pi_0 = cp.copy(pi)
    pi_0 += 1
    X = np.array(range(1, n + 1))
    BF = np.array([False for i in range(n)])
    BT_tau = g.transition[:, 1] == g.tau

    ndelta_c = np.zeros(n, dtype=int)
    delta_c = np.zeros((len(g.transition), n), dtype=int)
    delta_c = np.asmatrix(delta_c)
    if len(g.transition) != 0:
        for i in g.transition:
            if i[1] == g.tau:
                q = i[2]
                ndelta_c[q - 1] += 1
                delta_c[ndelta_c[q - 1] - 1, q - 1] = i[0]
                # delta_c = np.asarray(delta_c)
    iteration = 0
    while not list(pi_0) == list(pi):

        iteration += 1
        BT_iv = BT_tau & (pi[g.transition[:, 0] - 1] == pi[g.transition[:, 2] - 1])
        T_iv = g.transition[BT_iv]
        T_v = g.transition[np.logical_not(BT_iv)]
        B_ivt = cp.copy(BF)
        B_ivt[g.transition[BT_iv, 2] - 1] = True
        if len(T_v) == 0:
            return rearrange(pi)
        else:
            Gam = np.zeros((n*int(max(T_v[:, 1])) + max(n, max(pi)), n), int)
        for i in range(0, len(T_v)):
            B = cp.copy(BF)
            index = T_v[i, 0]
            B[T_v[i, 0] - 1] = True
            BD = cp.copy(B)

            # originally: max(list(map(int, BD)))
            while BD.any():
                BD1 = cp.copy(BF)
                for q in X[BD & B_ivt]:
                    test = q
                    for j in range(0, ndelta_c[q - 1]):
                        if pi[delta_c[j, q - 1] - 1] == pi[q - 1]:
                            BD1[delta_c[j, q - 1] - 1] = True
                BD = BD1 & np.logical_not(B)
                B = B | BD
            aPi = n*T_v[i, 1] + pi[T_v[i, 2] - 1]
            Gam[aPi - 1, B] = True
        pi_0 = cp.copy(pi)
        pi = np.zeros(n, int)
        k = 0
        for q in range(0, n):
            if pi[q] == 0:
                k += 1
                X1 = X[pi_0 == pi_0[q]]
                pi[q] = k

                for i in X1[1:]:
                    # originally: list(Gam[:, i - 1]) = list(Gam[:, q])
                    if Gam[:, i - 1].all == Gam[:, q].all:
                        pi[i - 1] = k

    x_pi = np.unique(pi)
    n_pi = len(x_pi)
    i_pi = np.unique(pi[g.initial - 1])
    if len(T_v[:, 0]):
        T_pi = np.unique(np.column_stack((
            pi[T_v[:, 0] - 1], T_v[:, 1], pi[T_v[:, 2] - 1])), axis=0)
    else:
        T_pi = np.array([], int)
    k = 0
    lmd_pi = np.zeros(len(x_pi), int)
    max_pi = pi[0]
    lmd_pi[0] = g.block[0]
    for i in range(1, n):
        if pi[i] > max_pi:
            k += 1
            max_pi = k
            lmd_pi[k] = g.block[i]

    return pi






