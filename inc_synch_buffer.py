import numpy as np
import copy
from BBS_logical import bbs_abstraction, G_bbs_abstraction
from synchronization_logical import synchronization_logical, G_sync
from BBS import bbs_org, G
from line_profiler import LineProfiler


def t_2_n_sigma(t):
    if np.size(t) == 0:
        n = 0
        sigma = np.array([], int)
    else:
        sigma = np.unique(t[:, 1])
        n = max(max(t[:, 0]), max(t[:, 2]))
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
    g = G_bbs_abstraction(transition=t, initial=init, block=lmd, tau=tau)
    t1 = copy.copy(g.transition)
    t1[:, 1] = t1[:, 1] - 1
    g_org = G(list(map(tuple, t1)), list(lmd))
    n_pi, t_pi, i_pi, lmd_pi, pi, iteration = bbs_abstraction(g)
    bbs_org(g_org)
    sigma_pi = np.setdiff1d(sigma, sigma_local)
    """
    lp = LineProfiler()
    lp_wrapper = lp(bbs_abstraction)
    lp_wrapper(g)
    lp.print_stats()

    lp = LineProfiler()
    lp_wrapper = lp(bbs_org)
    lp_wrapper(g_org)
    lp.print_stats()

    """

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
    delta = np.asmatrix(delta)
    sigma_delta = np.zeros(n, int)
    sigma_delta = np.asmatrix(sigma_delta)

    if np.size(t) == 0:
        return n_delta, delta, sigma_delta
    for i in range(len(t[:, 0])):
        q = t[i, i_source - 1]
        n_delta[q - 1] = n_delta[q - 1] + 1
        if n_delta[q - 1] > np.shape(delta)[0]:
            delta = np.row_stack((delta, np.zeros(np.shape(delta)[1], int)))
        delta[n_delta[q - 1] - 1, q - 1] = t[i, i_target - 1]
        if n_delta[q - 1] > np.shape(sigma_delta)[0]:
            sigma_delta = np.row_stack((sigma_delta, np.zeros(np.shape(sigma_delta)[1], int)))
        sigma_delta[n_delta[q - 1] - 1, q - 1] = t[i, 1]

    return n_delta, delta, sigma_delta


def delta2trans(n, n_delta, delta, sigma_delta):
    k = 0
    t = np.zeros([sum(n_delta), 3], int)
    for q in range(n):
        m = n_delta[q]
        for i in range(m):
            t[k, 0] = q + 1
            t[k, 1] = sigma_delta[i, q]
            t[k, 2] = delta[i, q]
            k += 1
    return t


def inc_sync_buffer(n_cap, n_buff, inc_bbs):
    a = 5
    mark = 1
    model = 1
    n, sigma, t, init, lmd, sigma_local = ts_model(model, a, n_cap, mark)
    a += 1
    if inc_bbs:
        n, sigma, t, init, lmd, pi, iteration = bbs(sigma, t, init, lmd, sigma_local)

    n_delta, delta, sigma_delta = trans2delta(n, t)

    for k in range(n_buff):
        model = 2
        n_1, sigma_1, t_1, init_1, lmd_1, sigma_local = ts_model(model, a, n_cap, mark)
        a += 1
        n_delta_1, delta_1, sigma_delta_1 = trans2delta(n_1, t_1)
        g = G_sync(
            n=n,
            sigma=set(sigma),
            ndelta=n_delta,
            delta=delta,
            sigma_delta=sigma_delta,
            init=np.array([init], int),
            lmd=lmd)
        g1 = G_sync(
            n=n_1,
            sigma=set(sigma_1),
            ndelta=n_delta_1,
            delta=delta_1,
            sigma_delta=sigma_delta_1,
            init=np.array([init_1], int),
            lmd=lmd_1)
        n, sigma, n_delta, delta, sigma_delta, init, lmd = synchronization_logical(g, g1)
        if inc_bbs:
            t = delta2trans(n, n_delta, delta, sigma_delta)
            n, sigma, t, init, lmd, pi, iteration = bbs(sigma, t, init, lmd, sigma_local)
            n_delta, delta, sigma_delta = trans2delta(n, t)

        model = 3
        if k + 1 == n_buff:
            model = 4
        n_1, sigma_1, t_1, init_1, lmd_1, sigma_local = ts_model(model, a, n_cap, mark)
        if k + 1 < n_buff:
            a += 1
        n_delta_1, delta_1, sigma_delta_1 = trans2delta(n_1, t_1)
        g = G_sync(
            n=n,
            sigma=set(sigma),
            ndelta=n_delta,
            delta=delta,
            sigma_delta=sigma_delta,
            init=np.array([init], int),
            lmd=lmd)
        g1 = G_sync(
            n=n_1,
            sigma=set(sigma_1),
            ndelta=n_delta_1,
            delta=delta_1,
            sigma_delta=sigma_delta_1,
            init=np.array([init_1], int),
            lmd=lmd_1)
        n, sigma, n_delta, delta, sigma_delta, init, lmd = synchronization_logical(g, g1)
        if (inc_bbs) & (k + 1 < n_buff):
            t = delta2trans(n, n_delta, delta, sigma_delta)
            n, sigma, t, init, lmd, pi, iteration = bbs(sigma, t, init, lmd, sigma_local)
            n_delta, delta, sigma_delta = trans2delta(n, t)

    model = 5
    n_1, sigma_1, t_1, init_1, lmd_1, sigma_local = ts_model(model, a, n_cap, mark)
    n_delta_1, delta_1, sigma_delta_1 = trans2delta(n_1, t_1)
    g = G_sync(
        n=n,
        sigma=set(sigma),
        ndelta=n_delta,
        delta=delta,
        sigma_delta=sigma_delta,
        init=np.array([init], int),
        lmd=lmd)
    g1 = G_sync(
        n=n_1,
        sigma=set(sigma_1),
        ndelta=n_delta_1,
        delta=delta_1,
        sigma_delta=sigma_delta_1,
        init=np.array([init_1], int),
        lmd=lmd_1)
    n, sigma, n_delta, delta, sigma_delta, init, lmd = synchronization_logical(g, g1)
    if inc_bbs:
        t = delta2trans(n, n_delta, delta, sigma_delta)
        n, sigma, t, init, lmd, pi, iteration = bbs(sigma, t, init, lmd, sigma_local)
    else:
        t = delta2trans(n, n_delta, delta, sigma_delta)
        n, sigma, t, init, lmd, pi, iteration = bbs(sigma, t, init, lmd, sigma)

    return n, sigma, t, init, lmd


inc_sync_buffer(5, 5, 1)

