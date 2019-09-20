import numpy as np
from reach_log import reach_log
import time
from delta2trans import delta2trans
from reach import reach
from line_profiler import LineProfiler


def reach_test_large_2(n):
	ndelta = np.zeros(n*n, int)
	delta = np.asmatrix(np.zeros([2, n*n]), int)
	for ir in range(0, n - 1):
		for ic in range(0, n - 1):
			ndelta[n * ir + ic] = 2
			delta[(0, n * ir + ic)] = n * ir + ic + 2
			delta[(1, n * ir + ic)] = n * (ir + 1) + ic + 1
	for i in range(0, n-1):
		ndelta[n * (n - 1) + i] = 1
		delta[(0, n * (n - 1) + i)] = n * (n - 1) + i + 2
		ndelta[n * i + n - 1] = 1
		delta[(0, n*i + n - 1)] = n * (i + 1) + n

	ndelta[n*n - 1] = 0
	return ndelta, delta


ndelta = reach_test_large_2(100)[0]
delta = reach_test_large_2(100)[1]

lp = LineProfiler()
lp_wrapper = lp(reach_log)
lp_wrapper(ndelta, delta, np.array([1]))
lp.print_stats()
# print(len(reach_log(ndelta, delta, np.array([1]))))

start = time.time()
reach_log(ndelta, delta, np.array([1]))
end = time.time()
print("", end - start)

sigma_f, transition, init = delta2trans(ndelta, delta, np.array([1]))
lp = LineProfiler()
lp_wrapper = lp(reach)
lp_wrapper(sigma_f, transition, init)
lp.print_stats()
start = time.time()
reach(sigma_f, transition, init)
end = time.time()
print("", end - start)



