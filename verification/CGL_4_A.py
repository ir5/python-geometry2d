from geometry2d import *


def get():
    a, b = input().split()
    return complex(float(a), float(b))


n = int(input())
g = [get() for _ in range(n)]
res = convex_hull(g)
k = len(res)
start = min(list(range(k)),
            key=lambda i: (res[i].imag, res[i].real))

print(k)
for i in range(k):
    p = res[(start + i) % k]
    print('{} {}'.format(int(p.real), int(p.imag)))
