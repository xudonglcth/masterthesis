import numpy as np
from reach_log import reach_log
import time
import profile
class G(object):
	def __init__(self, ndelta, delta, init):
		self.ndelta = ndelta
		self.delta = delta
		self.init = init


G1 = G(ndelta=np.array([2, 3, 3, 1, 1, 1, 1, 1, 1, 1]),
	   delta=np.mat([[2, 4, 7, 4, 5, 6, 7, 8, 9, 2],
					 [3, 5, 8, 0, 0, 0, 0, 0, 0, 0],
					 [0, 6, 9, 0, 0, 0, 0, 0, 0, 0]]),
	   init=np.array([10]))

G2 = G(ndelta=np.array([2, 1, 1, 2, 1, 1, 1]),
	   delta=np.mat([[2, 3, 4, 5, 6, 7, 7], [3, 0, 0, 7, 0, 0, 0]]),
	   init=np.array([1]))

G3 = G(ndelta=np.array([2, 1, 1, 2, 1, 1, 1]),
	   delta=np.mat([[2, 3, 4, 5, 6, 7, 7],
					 [3, 0, 0, 7, 0, 0, 0],]),
	   init=np.array([2]))

G4 = G(ndelta=np.array([2, 1, 1, 2, 1, 1, 4, 0, 0, 0]),
	   delta=np.mat([[2, 3, 4, 5, 6, 7, 2, 0, 0, 0],
					 [3, 0, 0, 7, 0, 0, 8, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 10, 0, 0, 0]]),
	   init=np.array([6]))

q = 0
print(reach_log(G4.ndelta, G4.delta, G4.init))





