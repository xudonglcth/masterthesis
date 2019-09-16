import numpy as np
import copy
import math


class G_sync:
    def __init__(self, n, sigma, ndelta, delta, sigma_delta, init, lmd):
        self.n = n
        self.sigma = sigma
        self.ndelta = ndelta
        self.delta = delta
        self.sigma_delta = sigma_delta
        self.init = init
        self.lmd = lmd


def synchronization_logical(g1, g2):
    tau = 1
    eps = 0

    sigma = np.array(list(g1.sigma | g2.sigma), int)
    sigma_s = (g1.sigma & g2.sigma) - {tau, eps}
    sigma_l1 = np.array(list(g1.sigma - sigma_s), int)
    sigma_l2 = np.array(list(g2.sigma - sigma_s), int)
    sigma_s = np.array(list(sigma_s), int)

    m = len(sigma)
    i_sigma = np.zeros(max(sigma), int)
    i_sigma[sigma - 1] = [i for i in range(1, len(sigma) + 1)]

    b_sigma_f = np.array([False for i in range(m)])
    b_sigma_s = copy.copy(b_sigma_f)
    b_sigma_l1 = copy.copy(b_sigma_f)
    b_sigma_l2 = copy.copy(b_sigma_f)

    b_sigma_s[i_sigma[sigma_s - 1] - 1] = True
    b_sigma_l1[i_sigma[sigma_l1 - 1] - 1] = True
    b_sigma_l2[i_sigma[sigma_l2 - 1] - 1] = True

    b_sigma_delta1 = np.zeros([g1.n, m], int)
    b_sigma_delta2 = np.zeros([g2.n, m], int)
    for i in range(0, g1.n):
        b_sigma_delta1[i] = b_sigma_f
        b_sigma_delta1[i, i_sigma[g1.sigma_delta[0:g1.ndelta[i], i] - 1] - 1] = True
        b_sigma_delta1 = b_sigma_delta1.astype(bool)
    for j in range(0, g2.n):
        b_sigma_delta2[j] = b_sigma_f
        b_sigma_delta2[j, i_sigma[g2.sigma_delta[0:g2.ndelta[j], j] - 1] - 1] = True
        b_sigma_delta2 = b_sigma_delta2.astype(bool)
    nx = g1.n * g2.n
    x = np.array(list(range(1, nx + 1)))
    delta12 = np.zeros(nx, int)
    delta12 = np.asmatrix(delta12)
    ndelta12 = np.zeros(nx, int)
    sigma_delta12 = np.zeros(nx, int)
    sigma_delta12 = np.asmatrix(sigma_delta12)
    lmd_12 = np.zeros(nx, int)

    k = 0
    init = np.zeros(len(g1.init)*len(g2.init), int)
    for q1 in g1.init:
        for q2 in g2.init:
            k += 1
            q = q1 + g1.n*(q2 - 1)
            init[k - 1] = q

    b = np.array([False for i in range(0, nx)])
    bf = copy.copy(b)
    b[init - 1] = True
    bd = copy.copy(b)

    while bd.any():
        dr_next = np.array([], int)
        for q in x[bd]:
            q2 = math.floor((q - 1)/g1.n) + 1
            q1 = q - g1.n*(q2 - 1)
            k = 0

            for a in sigma[b_sigma_s & b_sigma_delta1[q1 - 1] & b_sigma_delta2[q2 - 1]]:
                for i in range(0, g1.ndelta[q1 - 1]):
                    for j in range(0, g2.ndelta[q2 - 1]):
                        if (a == g1.sigma_delta[i, q1 - 1]) & (a == g2.sigma_delta[j, q2 - 1]):
                            k += 1
                            q_next = g1.delta[i, q1 - 1] + g1.n * (g2.delta[j, q2 - 1] - 1)
                            if k > np.shape(sigma_delta12)[0]:
                                sigma_delta12 = np.append(
                                    sigma_delta12, [np.zeros(np.shape(sigma_delta12)[1], int)], axis=0)
                            sigma_delta12[k - 1, q - 1] = a
                            if k > np.shape(delta12)[0]:
                                delta12 = np.append(delta12, [np.zeros(np.shape(delta12)[1], int)], axis=0)
                            delta12[k - 1, q - 1] = q_next
                            dr_next = np.append(dr_next, q_next)

            for a in sigma[b_sigma_l1 & b_sigma_delta1[q1 - 1]]:
                for i in range(0, g1.ndelta[q1 - 1]):
                    if a == g1.sigma_delta[i, q1 - 1]:
                        k += 1
                        q_next = g1.delta[i, q1 - 1] + g1.n * (q2 - 1)
                        if k > np.shape(sigma_delta12)[0]:
                            sigma_delta12 = np.append(sigma_delta12, [np.zeros(np.shape(sigma_delta12)[1], int)], axis=0)
                        sigma_delta12[k - 1, q - 1] = a
                        if k > np.shape(delta12)[0]:
                            delta12 = np.append(delta12, [np.zeros(np.shape(delta12)[1], int)], axis=0)
                        delta12[k - 1, q - 1] = q_next
                        dr_next = np.append(dr_next, q_next)

            for a in sigma[b_sigma_l2 & b_sigma_delta2[q2 - 1]]:
                for j in range(0, g2.ndelta[q2 - 1]):
                    if a == g2.sigma_delta[j, q2 - 1]:
                        k += 1
                        q_next = q1 + g1.n * (g2.delta[j, q2 - 1] - 1)
                        if k > np.shape(sigma_delta12)[0]:
                            sigma_delta12 = np.append(sigma_delta12, [np.zeros(np.shape(sigma_delta12)[1], int)], axis=0)
                        sigma_delta12[k - 1, q - 1] = a
                        if k > np.shape(delta12)[0]:
                            delta12 = np.append(delta12, [np.zeros(np.shape(delta12)[1], int)], axis=0)
                        delta12[k - 1, q - 1] = q_next
                        dr_next = np.append(dr_next, q_next)
            ndelta12[q - 1] = k
            lmd_12[q - 1] = min(g1.lmd[q1 - 1], g2.lmd[q2 - 1])
        bd = copy.copy(bf)
        bd[dr_next - 1] = True
        bd = bd & ~b
        b = b | bd

    r = x[b]
    n = len(r)
    ix = np.zeros(nx, int)
    ix[r - 1] = list(range(1, n + 1))

    k = 0
    m = np.shape(delta12)[0]
    ndelta = np.zeros(n, int)
    delta = np.zeros([m, n], int)
    delta = np.asmatrix(delta)
    sigma_delta = copy.copy(delta)
    lmd = np.zeros(n, int)

    for i in r:
        k += 1
        ndelta[k - 1] = ndelta12[i - 1]
        delta[0:ndelta[k - 1], k - 1] = ix[delta12[0:ndelta12[i - 1], i - 1] - 1]
        sigma_delta[0:ndelta[k - 1], k - 1] = sigma_delta12[0:ndelta12[i - 1], i - 1]
        lmd[k - 1] = lmd_12[i - 1]
    init = ix[init - 1]
    return n, sigma, ndelta, delta, sigma_delta, init, lmd





