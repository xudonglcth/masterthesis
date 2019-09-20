import numpy as np


def reach_log(ndelta, delta, init):
	n = max(init)
	x = np.array([i for i in range(1, len(ndelta) + 1)])
	b = np.array([False for i in range(1, len(ndelta) + 1)])
	b[(init - 1)] = True
	bd = b
	d_max = len(ndelta)
	BD_False = np.array([False for i in range(0, d_max)])
	delta = delta.T

	while bd.any():
		BD1 = BD_False
		for q in x[bd]:
			for i in range(0, ndelta[q - 1]):
				BD1[delta[q - 1, i] - 1] = True
				# l.append(delta[i, q-1])
		bd = BD1 & ~b
		b = b | bd
	# n1 = max(l)
	# n = max(n, n1)
	# n = len(ndelta)
	# x = x[0: n]
	r = x[b]
	return r
