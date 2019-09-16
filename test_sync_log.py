from synchronization_logical import G
from synchronization_logical import synchronization_logical
import numpy as np
from line_profiler import LineProfiler
g1_1 = G(
    n=2,
    sigma={2, 3},
    ndelta=np.array([1, 1], int),
    delta=np.mat([[2, 2]], int),
    sigma_delta=np.mat([[2, 3]], int),
    init=np.array([1], int),
    lmd=np.array([1, 2])
)

g1_2 = G(
    n=2,
    sigma={3, 4},
    ndelta=np.array([1, 1], int),
    delta=np.mat([[2, 2]], int),
    sigma_delta=np.mat([[3, 4]], int),
    init=np.array([1], int),
    lmd=np.array([1, 2])
)

g2_1 = G(
    n=2,
    sigma={2, 3, 4},
    ndelta=np.array([0, 0], int),
    delta=np.mat([[0, 0]], int),
    sigma_delta=np.mat([[0, 0]], int),
    init=np.array([1, 2], int),
    lmd=np.array([1, 2])
)

g2_2 = G(
    n=3,
    sigma={2, 3, 4},
    ndelta=np.array([2, 0, 0], int),
    delta=np.mat([[2, 0, 0], [2, 0, 0]], int),
    sigma_delta=np.mat([[2, 0, 0], [3, 0, 0]], int),
    init=np.array([], int),
    lmd=np.array([2, 1])
)

g3_1 = G(
    n=2,
    sigma={2, 3, 4},
    ndelta=np.array([0, 0], int),
    delta=np.mat([[0, 0]], int),
    sigma_delta=np.mat([[0, 0]], int),
    init=np.array([1, 2], int),
    lmd=np.array([1, 1])
)

g3_2 = G(
    n=3,
    sigma={2, 3, 4},
    ndelta=np.array([2, 0, 0], int),
    delta=np.mat([[2, 0, 0], [2, 0, 0]], int),
    sigma_delta=np.mat([[2, 0, 0], [3, 0, 0]], int),
    init=np.array([1, 3], int),
    lmd=np.array([1, 2, 1])
)

g4_1 = G(
    n=3,
    sigma={2, 3, 4},
    ndelta=np.array([3, 0, 0], int),
    delta=np.mat([[2, 0, 0], [2, 0, 0], [3, 0, 0]], int),
    sigma_delta=np.mat([[2, 0, 0], [4, 0, 0], [3, 0, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 2])
)

g4_2 = G(
    n=2,
    sigma={2, 3, 4},
    ndelta=np.array([2, 0, 0], int),
    delta=np.mat([[2, 0, 0], [2, 0, 0]], int),
    sigma_delta=np.mat([[2, 0, 0], [3, 0, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 2])
)

g5_1 = G(
    n=2,
    sigma={2, 3},
    ndelta=np.array([1, 1], int),
    delta=np.mat([[2, 1]], int),
    sigma_delta=np.mat([[2, 3]], int),
    init=np.array([1], int),
    lmd=np.array([1, 2])
)

g5_2 = G(
    n=2,
    sigma={3, 4},
    ndelta=np.array([1, 1], int),
    delta=np.mat([[2, 1]], int),
    sigma_delta=np.mat([[3, 4]], int),
    init=np.array([1], int),
    lmd=np.array([1, 2])
)

g6_1 = G(
    n=2,
    sigma={2, 3},
    ndelta=np.array([2, 0], int),
    delta=np.mat([[1, 0], [2, 0]], int),
    sigma_delta=np.mat([[2, 0], [3, 0]], int),
    init=np.array([1, 2], int),
    lmd=np.array([2, 2])
)

g6_2 = G(
    n=3,
    sigma={2, 3},
    ndelta=np.array([1, 1, 0], int),
    delta=np.mat([[2, 3, 0]], int),
    sigma_delta=np.mat([[2, 3, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 2])
)

g7_1 = G(
    n=3,
    sigma={5, 6, 3},
    ndelta=np.array([1, 1, 1], int),
    delta=np.mat([[2, 3, 3]], int),
    sigma_delta=np.mat([[5, 6, 3]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 2])
)

g7_2 = G(
    n=3,
    sigma={6, 8, 3},
    ndelta=np.array([1, 1, 1], int),
    delta=np.mat([[2, 3, 3]], int),
    sigma_delta=np.mat([[6, 8, 3]], int),
    init=np.array([1], int),
    lmd=np.array([1, 2, 2])
)

g8_1 = G(
    n=2,
    sigma={3, 6},
    ndelta=np.array([1, 1], int),
    delta=np.mat([[2, 2]], int),
    sigma_delta=np.mat([[6, 3]], int),
    init=np.array([1], int),
    lmd=np.array([1, 2])
)

g8_2 = G(
    n=3,
    sigma={6, 8},
    ndelta=np.array([1, 1, 0], int),
    delta=np.mat([[2, 3, 0]], int),
    sigma_delta=np.mat([[6, 8, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 2])
)

g9_1 = G(
    n=5,
    sigma={2, 3, 4, 5},
    ndelta=np.array([1, 1, 1, 1, 1], int),
    delta=np.mat([[2, 3, 4, 5, 1]], int),
    sigma_delta=np.mat([[2, 3, 4, 5, 4]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 1, 2, 1])
)

g9_2 = G(
    n=4,
    sigma={2, 3, 60},
    ndelta=np.array([1, 1, 2, 0], int),
    delta=np.mat([[2, 3, 4, 0], [0, 0, 1, 0]], int),
    sigma_delta=np.mat([[2, 3, 60, 0], [0, 0, 60, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 2, 1])
)

g10_1 = G(
    n=10,
    sigma={2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13},
    ndelta=np.array([2, 2, 1, 1, 1, 1, 1, 1, 1, 0], int),
    delta=np.mat([[2, 3, 4, 5, 6, 7, 8, 9, 10, 0], [2, 4, 0, 0, 0, 0, 0, 0, 0, 0]], int),
    sigma_delta=np.mat([[2, 3, 4, 5, 6, 7, 8, 9, 10, 0], [12, 13, 0, 0, 0, 0, 0, 0, 0, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
)

g10_2 = G(
    n=10,
    sigma={2, 3, 4, 5, 6, 7, 8, 9, 10},
    ndelta=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0], int),
    delta=np.mat([[2, 3, 4, 5, 6, 7, 8, 9, 10, 0]], int),
    sigma_delta=np.mat([[2, 3, 4, 5, 6, 7, 8, 9, 10, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
)

g11_1 = G(
    n=4,
    sigma={6, 10},
    ndelta=np.array([1, 0, 1, 0], int),
    delta=np.mat([[3, 0, 4, 0]], int),
    sigma_delta=np.mat([[6, 0, 10, 0]], int),
    init=np.array([1], int),
    lmd=np.array([1, 1, 2, 1])
)

g11_2 = G(
    n=4,
    sigma={6, 7},
    ndelta=np.array([0, 1, 0, 1], int),
    delta=np.mat([[0, 4, 0, 3]], int),
    sigma_delta=np.mat([[0, 7, 0, 6]], int),
    init=np.array([2], int),
    lmd=np.array([1, 1, 2, 1])
)

g12_1 = G(
    n=5,
    sigma={16, 14, 15, 18},
    ndelta=np.array([0, 3, 1, 0, 0], int),
    delta=np.mat([[0, 1, 2, 0, 0], [0, 4, 0, 0, 0], [0, 5, 0, 0, 0]], int),
    sigma_delta=np.mat([[0, 14, 16, 0, 0], [0, 15, 0, 0, 0], [0, 18, 0, 0, 0]], int),
    init=np.array([3], int),
    lmd=np.array([1, 1, 2, 1, 1])
)

g12_2 = G(
    n=7,
    sigma={13, 19, 16, 18},
    ndelta=np.array([0, 1, 0, 1, 2, 0, 1], int),
    delta=np.mat([[0, 5, 0, 5, 1, 0, 6], [0, 0, 0, 0, 7, 0, 0]], int),
    sigma_delta=np.mat([[0, 13, 0, 19, 16, 0, 18], [0, 0, 0, 0, 16, 0, 0]], int),
    init=np.array([2, 4], int),
    lmd=np.array([1, 1, 1, 1, 2, 1, 1])
)
lp = LineProfiler()
lp_wrapper = lp(synchronization_logical)
lp_wrapper(g12_1, g12_2)
lp.print_stats()
print(synchronization_logical(g12_1, g12_2))
