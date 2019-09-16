from BBS_logical import G
from BBS_logical import bbs_abstraction
import time
import numpy as np
from line_profiler import LineProfiler

G1 = G(transition=np.array([[1, 1, 2], [2, 1, 3], [3, 2, 3]]), block=[1, 1, 1], tau=1, initial=1)
G1b = G(transition=np.array([[1, 1, 2], [2, 1, 3]]), block=[1, 1, 1], tau=1, initial=1)
G2 = G(transition=np.array([(1, 2, 2), (2, 3, 3), (3, 2, 3)]),
       block=[1, 1, 1],
       tau=1,
       initial=1)
G2b = G(transition=np.array([(1, 2, 2), (2, 3, 3)]),
        block=[1, 1, 1],
        tau=1,
        initial=1)
G3 = G(transition=np.array([(1, 0, 2), (2, 0, 3), (3, 0, 3)]),
       block=[1, 1, 1],
       tau=0,
       initial=1)
G3b = G(transition=np.array([(1, 0, 2), (2, 0, 3)]),
        block=[1, 1, 2],
        tau=0,
        initial=1)
G4 = G(transition=np.array([(1, 0, 2), (2, 0, 3), (2, 0, 4),
                            (3, 0, 3), (4, 0, 4)]),
       block=[0, 0, 1, 1],
       tau=0,
       initial=1)
G4b = G(transition=np.array([(1, 0, 2), (2, 0, 3), (2, 0, 4)]),
        block=[0, 0, 1, 1],
        tau=0,
        initial=1)
G5 = G(transition=np.array([(1, 0, 2), (2, 0, 1), (2, 0, 4),
                            (1, 0, 3), (3, 0, 4), (4, 0, 4)]),
       block=[2, 2, 0, 2],
       tau=0,
       initial=1)
G6 = G(transition=np.array([(1, 0, 2), (2, 0, 1), (2, 0, 4),
                            (4, 0, 2), (1, 0, 3), (3, 0, 4),
                            (4, 0, 5), (5, 0, 5)]),
       block=[2, 2, 0, 2, 3],
       tau=0,
       initial=1)
G7 = G(transition=np.array([(1, 0, 2), (2, 0, 1), (2, 0, 3),
                            (3, 0, 4), (4, 0, 5), (5, 0, 3),
                            (5, 0, 6), (6, 0, 6)]),
       block=[2, 2, 3, 3, 3, 1],
       tau=0,
       initial=1)
G8 = G(transition=np.array([(3, 3, 3), (4, 3, 4)]),
       block=[1, 1, 0, 0],
       tau=1,
       initial=1)
G_notrans = G(transition=np.array([]),
              block=[2],
              tau=1,
              initial=1)
G_oneivtrans = G(transition=np.array([(1, 1, 1)]),
                 block=[0],
                 tau=1,
                 initial=1)
G9 = G(transition=np.array([(1, 0, 1), (1, 2, 1)]),
       block=[2],
       tau=0,
       initial=1)

G10 = G(transition=np.array([(1, 0, 2), (2, 2, 3), (3, 3, 3)]),
        block=[2, 2, 2],
        tau=0,
        initial=1)
G11 = G(transition=np.array([(1, 0, 2), (2, 0, 2), (1, 0, 3), (3, 0, 3)]),
        block=[2, 1, 2],
        tau=0,
        initial=1)
G12 = G(transition=np.array([(1, 0, 2), (2, 2, 3), (1, 0, 3), (3, 3, 3)]),
        block=[1, 1, 1],
        tau=0,
        initial=1)
G13 = G(transition=np.array([(1, 0, 2), (2, 2, 3), (1, 0, 4),
                             (4, 2, 3), (3, 3, 3)]),
        block=[2, 2, 2, 1],
        tau=0,
        initial=1)
G14 = G(transition=np.array([(1, 0, 2), (2, 2, 3), (1, 0, 3),
                             (3, 0, 4), (4, 3, 4)]),
        block=[2, 2, 2, 1],
        tau=0,
        initial=1)
G15 = G(transition=np.array([(1, 2, 2), (2, 0, 4), (1, 0, 3), (3, 0, 4)]),
        block=[2, 2, 2, 2],
        tau=0,
        initial=1)
G15b = G(transition=np.array([(1, 2, 2), (2, 0, 4), (1, 0, 3), (3, 0, 4)]),
         block=[2, 2, 1, 2],
         tau=0,
         initial=1)
G16 = G(transition=np.array([(1, 2, 2), (2, 0, 3), (3, 0, 3),
                    (1, 0, 4), (4, 0, 5), (5, 0, 5)]),
        block=[2, 2, 2, 1, 1],
        tau=0,
        initial=1)

G16b = G(transition=np.array([(1, 2, 2), (2, 0, 3), (3, 0, 3),
                              (1, 0, 4), (4, 0, 5), (5, 0, 5)]),
         block=[2, 2, 2, 2, 2],
         tau=0,
         initial=1)

G17 = G(transition=np.array([(1, 0, 2), (1, 0, 3), (2, 2, 2), (3, 3, 3)]),
        block=[2, 2, 2],
        tau=0,
        initial=1)

G18 = G(transition=np.array([(1, 1, 2), (2, 2, 3), (1, 2, 3)]),
        block=[0, 0, 0],
        tau=1,
        initial=1)
G19 = G(transition=np.array([(1, 0, 2), (2, 2, 3), (1, 2, 3),
                             (1, 0, 4), (3, 0, 4), (4, 2, 4)]),
        block=[2, 2, 2, 1],
        tau=0,
        initial=1)
G20 = G(transition=np.array([(1, 2, 2), (1, 3, 3), (2, 4, 4),
                             (2, 4, 5), (2, 4, 6), (3, 4, 7),
                             (3, 4, 8), (3, 4, 9), (4, 5, 4),
                             (5, 5, 5), (6, 5, 6), (7, 5, 7),
                             (8, 5, 8), (9, 5, 9)]),
        block=[4, 4, 4, 1, 1, 2, 1, 2, 2],
        tau=1,
        initial=1)
G21 = G(transition=np.array([(1, 0, 2), (1, 2, 4), (1, 0, 3),
                             (2, 2, 2), (2, 2, 4), (3, 2, 3),
                             (4, 0, 1), (4, 0, 3)]),
        block=[2, 2, 1, 2],
        tau=0,
        initial=1)

G22 = G(transition=np.array([(1, 6, 2), (2, 0, 3), (2, 0, 4),
                             (2, 10, 5), (4, 10, 5), (5, 0, 3),
                             (5, 0, 1), (3, 10, 3)]),
        block=[2, 2, 1, 2, 2],
        tau=0,
        initial=1)
G23 = G(transition=np.array([[1, 0, 2], [1, 0, 3], [1, 10, 4],
                             [3, 10, 4], [4, 0, 2], [4, 0, 1],
                             [2, 10, 2]]),
        block=[2, 2, 2, 2],
        tau=0,
        initial=1)
G24 = G(transition=np.array([[1, 10, 2], [2, 10, 3], [3, 10, 4],
                             [4, 2, 4], [2, 10, 5], [5, 10, 6],
                             [6, 10, 7], [7, 2, 7]]),
        block=[2, 2, 2, 2, 2, 1, 1],
        tau=10,
        initial=1)
G25 = G(transition=np.array([[1, 0, 2], [2, 0, 3], [1, 3, 3],
                             [3, 0, 4], [4, 2, 5], [5, 0, 6],
                             [6, 2, 7], [4, 4, 7], [7, 3, 7]]),
        block=[3, 3, 3, 3, 3, 3, 3],
        tau=0,
        initial=1)

Buffer1 = G(transition=np.array([[1, 1, 2], [2, 2, 1], [2, 1, 3],
                                 [3, 2, 2], [3, 1, 4], [4, 2, 3],
                                 [4, 1, 5], [5, 2, 4], [5, 1, 6],
                                 [6, 2, 5], [6, 1, 7], [7, 2, 6],
                                 [7, 1, 8], [8, 2, 7], [8, 1, 9],
                                 [9, 2, 8], [9, 1, 10], [10, 2, 9],
                                 [10, 1, 11], [11, 2, 10], [11, 1, 12],
                                 [12, 2, 11], [12, 1, 13], [13, 2, 12],
                                 [13, 1, 14], [14, 2, 13], [14, 1, 15],
                                 [15, 2, 14], [15, 1, 16], [16, 2, 15],
                                 [16, 1, 17], [17, 2, 16], [17, 1, 18],
                                 [18, 2, 17], [18, 1, 19], [19, 2, 18],
                                 [19, 1, 20], [20, 2, 19]]),
            block=[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            tau=1,
            initial=1)
Buffer2 = G(transition=np.array([[1, 1, 2], [2, 2, 1], [2, 1, 3],
                                 [3, 3, 2], [3, 1, 4], [4, 4, 3],
                                 [4, 1, 5], [5, 5, 4], [5, 1, 6],
                                 [6, 6, 5], [6, 1, 7], [7, 7, 6],
                                 [7, 1, 8], [8, 8, 7], [8, 1, 9],
                                 [9, 9, 8], [9, 1, 10], [10, 10, 9],
                                 [10, 1, 11], [11, 11, 10], [11, 1, 12],
                                 [12, 12, 11], [12, 1, 13], [13, 13, 12],
                                 [13, 1, 14], [14, 14, 13], [14, 1, 15],
                                 [15, 15, 14], [15, 1, 16], [16, 16, 15],
                                 [16, 1, 17], [17, 17, 16], [17, 1, 18],
                                 [18, 18, 17], [18, 1, 19], [19, 19, 18],
                                 [19, 1, 20], [20, 20, 19]]),
            block=[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            tau=1,
            initial=1)
start = time.time()
for i in range(0, 100):
    bbs_abstraction(Buffer2)
end = time.time()

print("", end - start)
print(bbs_abstraction(Buffer2))


def test_performance(g):
    for i in range(100):
        bbs_abstraction(g)


lp = LineProfiler()
lp_wrapper = lp(bbs_abstraction)
lp_wrapper(Buffer2)
lp.print_stats()
