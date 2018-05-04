from geometry2d import *

x1, y1, x2, y2 = [float(v) for v in input().split()]
p1 = complex(x1, y1)
p2 = complex(x2, y2)
q = int(input())
for _ in range(q):
    x3, y3 = [float(v) for v in input().split()]
    p3 = complex(x3, y3)
    res = ccw(p1, p2, p3)
    if res == 1:
        print('COUNTER_CLOCKWISE')
    elif res == -1:
        print('CLOCKWISE')
    elif res == +2:
        print('ONLINE_BACK')
    elif res == -2:
        print('ONLINE_FRONT')
    else:
        print('ON_SEGMENT')
