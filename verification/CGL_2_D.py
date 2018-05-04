from geometry2d import *

q = int(input())
for _ in range(q):
    vs = [float(v) for v in input().split()]
    s1 = (complex(vs[0], vs[1]), complex(vs[2], vs[3]))
    s2 = (complex(vs[4], vs[5]), complex(vs[6], vs[7]))
    res = dist_ss(s1, s2)
    print('{:.9f}'.format(res))
