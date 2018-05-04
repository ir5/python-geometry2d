from geometry2d import *

x1, y1, x2, y2 = [float(v) for v in input().split()]
s = (complex(x1, y1), complex(x2, y2))
q = int(input())
for _ in range(q):
    x, y = [float(v) for v in input().split()]
    p = complex(x, y)
    res = projection(s, p)
    print('{:.9f} {:.9f}'.format(res.real, res.imag))
