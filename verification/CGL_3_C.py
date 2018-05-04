from geometry2d import *


def get():
    a, b = input().split()
    return complex(float(a), float(b))


n = int(input())
g = [get() for _ in range(n)]
q = int(input())
for _ in range(q):
    x, y = [float(v) for v in input().split()]
    p = complex(x, y)
    res = contains(g, p)
    print(res + 1)
