import numpy as np
from reach_log import reach_log
import time
import profile


def reach_test(n):
	ndelta = np.array([2, 1, 1, 2, 1, 1, 4, 0, 0, 0])
	delta = np.mat([[2, 3, 4, 5, 6, 7, 2, 0, 0, 0],
					[3, 0, 0, 7, 0, 0, 8, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 10, 0, 0, 0]])
	q = 0
	ndeltaq = np.zeros(10 * n, int)
	deltaq = np.asmatrix(np.zeros([4, 10 * n], int))
	init = np.zeros(n, int)
	for k in range(1, n + 1):
		ndeltaq[10 * (k - 1): 10 * (k - 1) + 7] = ndelta[0: 7]
		deltaq[0, 10 * (k - 1): 10 * (k - 1) + 7] = delta[0, 0:7] + q
		deltaq[1, 10 * (k - 1) + 0] = delta[1, 0] + q
		deltaq[1, 10 * (k - 1) + 3] = delta[1, 3] + q
		deltaq[1, 10 * (k - 1) + 6] = delta[1, 6] + q
		deltaq[2, 10 * (k - 1) + 6] = delta[2, 6] + q
		deltaq[3, 10 * (k - 1) + 6] = delta[3, 6] + q
		init[k-1] = 1 + 10 * (k - 1)
		q += 10
	return ndeltaq, deltaq, init
