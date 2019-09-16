import numpy as np


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





def inc_sync_buffer(n_cap, n_buff, inc_bbs):
    a = 5
    mark = 1
    model = 1
    n, sigma, t, init, lmd, sigma_local = ts_model(model, a, n_cap, mark)
    a += 1
    if inc_bbs:
        pass

