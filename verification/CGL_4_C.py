from geometry2d import *


def get():
    a, b = input().split()
    return complex(float(a), float(b))


n = int(input())
g = [get() for _ in range(n)]
q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = [float(v) for v in input().split()]
    s = (complex(x1, y1), complex(x2, y2))
    res = area(convex_cut(g, s))
    print('{:.9f}'.format(res))
