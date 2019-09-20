def reach(sigma_f, delta, init):
	"""
	:param sigma_f: feasible events, dict
	:param delta: transition functions, dict
	:param init: initial states, set
	:return: set of reachable states
	"""
	delta_x = []
	k = 0
	x_r = init
	delta_x.append(init)
	while delta_x[k]:
		k += 1
		delta_x.append(set())
		for x in list(delta_x[k - 1]):
			for a in sigma_f[x]:
				delta_x[k] = delta[(x, a)] | delta_x[k]
		delta_x[k] = delta_x[k] - x_r
		x_r = x_r | delta_x[k]
	return x_r


