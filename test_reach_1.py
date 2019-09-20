from test_reach_large import reach_test
from delta2trans import delta2trans
from reach import reach
from reach_log import reach_log
import numpy as np
import time
from line_profiler import LineProfiler

np.set_printoptions(threshold=100000)
ndeltaq = reach_test(100000)[0]
deltaq = reach_test(100000)[1]
init = reach_test(100000)[2]

lp = LineProfiler()
lp_wrapper = lp(reach_log)
lp_wrapper(ndeltaq, deltaq, init)
lp.print_stats()

start = time.time()
reach_log(ndeltaq, deltaq, init)
end = time.time()
print("", end - start)


sigma_f = delta2trans(ndeltaq, deltaq, init)[0]
transition = delta2trans(ndeltaq, deltaq, init)[1]
init = delta2trans(ndeltaq, deltaq, init)[2]

start = time.time()
print(reach(sigma_f, transition, init))
end = time.time()
print("", end - start)

