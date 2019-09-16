import numpy as np
from BBS_logical import bbs_abstraction
from BBS_logical import G


def t_2_n_sigma(t):
    if np.size(t) == 0:
        n = 0
        sigma = np.array([], int)
    else:
        sigma = np.unique(t[:, 1])
        n = max(max(t[:, 0], max(t[:, 2])))
    return n, sigma


def ts_model(model, a, n_cap, mark):
    if model == 1:
        t = np.array([[1, a, 2], [2, a + 1, 1]], int)
        sigma_local = np.array(a, int)
    elif model == 2:
        t = np.array([], int)
        for i in range(n_cap):
            if np.size(t) == 0:
                t = np.array([[i + 1, a, i + 2], [i + 2, a + 1, i + 1]], int)
            else:
                t = np.append(t, [[i + 1, a, i + 2], [i + 2, a + 1, i + 1]], axis=0)
        sigma_local = np.array(a, int)
    elif model == 3:
        t = np.array([[1, a, 2], [2, a + 1, 1]], int)
        sigma_local = np.array(a, int)
    elif model == 4:
        t = np.array([[1, a, 2], [2, a + 1, 1]], int)
        sigma_local = np.array([], int)
    elif model == 5:
        t = np.array([[1, a, 2], [2, a + 1, 1], [2, a + 2, 1]])
        sigma_local = np.array([a, a + 1, a + 2], int)

    init = 1
    n, sigma = t_2_n_sigma(t)
    lmd = np.ones(n, int)
    if mark == 1:
        lmd[0] = 2
    return n, sigma, t, init, lmd, sigma_local


def event_labels():
    tau = 1
    eps = 0
    fail = 4
    return tau, eps, fail


def bbs(sigma, t, init, lmd, sigma_local):
    tau = event_labels()[0]
    if np.size(sigma_local) != 0:
        t[np.in1d(t[:, 1], sigma_local), 1] = tau
        sigma = np.union1d(sigma, tau)
    g = G(transition=t, initial=init, block=lmd, tau=tau)
    n_pi, t_pi, i_pi, lmd_pi, pi, iteration = bbs_abstraction(g)
    sigma_pi = np.setdiff1d(sigma, sigma_local)
    return n_pi, sigma_pi, t_pi, i_pi, lmd_pi, pi, iteration


def trans2delta(n, t, backward=False):
    if backward:
        i_source = 3
        i_target = 1
    else:
        i_source = 1
        i_target = 3

    n_delta = np.zeros(n, int)
    delta = np.zeros(n, int)
    sigma_delta = np.zeros(n, int)

    if np.size(t) == 0:
        return n_delta, delta, sigma_delta
    for i in range(len(t[:, 0])):
        q = t[i, i_source]
        n_delta[q - 1] = n_delta[q - 1] + 1
        delta[n_delta[q - 1] - 1, q - 1] = t[i, i_target - 1]
        sigma_delta[n_delta[q - 1] - 1, q - 1] = t[i, 1]
        
    return n_delta, delta, sigma_delta



def inc_sync_buffer(n_cap, n_buff, inc_bbs):
    a = 5
    mark = 1
    model = 1
    n, sigma, t, init, lmd, sigma_local = ts_model(model, a, n_cap, mark)
    a += 1
    if inc_bbs:
        n, sigma, t, init, lmd, pi, iteration = bbs(sigma, t, init, lmd, sigma_local)

    n_delta, delta, sigma_delta = trans2delta

