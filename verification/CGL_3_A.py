from geometry2d import *


def get():
    a, b = input().split()
    return complex(float(a), float(b))


n = int(input())
g = [get() for _ in range(n)]
res = area(g)
print('{:.1f}'.format(res))
