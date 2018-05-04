from typing import List
from typing import Tuple


def dot(a: complex, b: complex) -> complex:
    """Inner product of two vectors.

    Args:
        a (complex): First vector.
        b (complex): Second vector.

    Returns:
        complex: Inner product: a.x * b.x + a.y * b.y
    """
    return (a.conjugate() * b).real


def cross(a: complex, b: complex) -> complex:
    """2D cross product (a.k.a. wedge product) of two vectors.

    Args:
        a (complex): First vector.
        b (complex): Second vector.

    Returns:
        complex: 2D cross product: a.x * b.y - a.y * b.x
    """
    return (a.conjugate() * b).imag


def ccw(a: complex, b: complex, c: complex) -> int:
    """The sign of counter-clockwise angle of points abc.

    Args:
        a (complex): First point.
        b (complex): Second point.
        c (complex): Third point.

    Returns:
        int: If the three points are not colinear, then returns the sign of
            counter-clockwise angle of abc. That is, if the points abc make
            counter-clockwise turn, it returns +1. If clockwise turn, returns
            -1.
            If they are colinear, returns one of +2, -2, or 0. This depends on
            the order of points on the line.
    """
    b -= a
    c -= a
    if cross(b, c) > 0:
        # counter-clockwise
        return +1
    elif cross(b, c) < 0:
        # clockwise
        return -1
    elif dot(b, c) < 0:
        # c--a--b on line
        return +2
    elif abs(b) < abs(c):
        # a--b--c on line
        return -2
    else:
        # b--c--a on line
        return 0


def projection(s: Tuple[complex, complex], p: complex) -> complex:
    """Projection of a point onto a line.

    Args:
        s (Tuple of complexes): A line.
        p (complex): A point.

    Returns:
        complex: Projection point.
    """
    t = dot(p - s[0], s[0] - s[1]) / abs(s[0] - s[1]) ** 2
    return s[0] + t * (s[0] - s[1])


def reflection(s: Tuple[complex, complex], p: complex) -> complex:
    """Reflection of a point onto a line.

    Args:
        s (Tuple of complexes): A line.
        p (complex): A point.

    Returns:
        complex: Reflection point.
    """
    return 2 * projection(s, p) - p


def dist_lp(s: Tuple[complex, complex], p: complex) -> float:
    """Distance between a line and a point.

    Args:
        s (Tuple of complexes): A line.
        p (complex): A point.

    Returns:
        complex: Distance between s and p.
    """
    return abs(p - projection(s, p))


def dist_sp(s: Tuple[complex, complex], p: complex) -> float:
    """Distance between a segment and a point.

    Args:
        s (Tuple of complexes): A segment.
        p (complex): A point.

    Returns:
        complex: Distance between s and p.
    """
    if dot(p - s[0], s[1] - s[0]) >= 0 and dot(p - s[1], s[0] - s[1]) >= 0:
        return dist_lp(s, p)
    else:
        return min(abs(p - s[0]), abs(p - s[1]))


def dist_ss(s: Tuple[complex, complex], t: Tuple[complex, complex]) -> float:
    """Distance between two segments.

    Args:
        s (Tuple of complexes): First segment.
        t (Tuple of complexes): Second segment.

    Returns:
        complex: Distance between s and t.
    """
    if does_intersect_ss(s, t):
        return 0
    else:
        return min(dist_sp(s, t[0]), dist_sp(s, t[1]),
                   dist_sp(t, s[0]), dist_sp(t, s[1]))


def intersection_ll(s: Tuple[complex, complex],
                    t: Tuple[complex, complex]) -> complex:
    """Intersection point of two lines s and t.

    Note that you have to ensure the lines are not parallel. When parallel
    lines are given, zero division error might occur.

    Args:
        s (Tuple of complexes): First line.
        t (Tuple of complexes): Second line.

    Returns:
        complex: Intersection of s and t.
    """
    sv = s[1] - s[0]
    tv = t[1] - t[0]
    return s[0] + sv * cross(tv, t[0] - s[0]) / cross(tv, sv)


def does_intersect_ss(s: Tuple[complex, complex],
                      t: Tuple[complex, complex]) -> bool:
    """Determine if two segments have a common point, including end points.

    Args:
        s (Tuple of complexes): First segment.
        t (Tuple of complexes): Second segment.

    Returns:
        bool: True if s and t have a common point. False otherwise.
    """
    if ccw(s[0], s[1], t[0]) * ccw(s[0], s[1], t[1]) == -1 and\
       ccw(t[0], t[1], s[0]) * ccw(t[0], t[1], s[1]) == -1:
        return True
    if ccw(s[0], s[1], t[0]) == 0 or ccw(s[0], s[1], t[1]) == 0 or\
       ccw(t[0], t[1], s[0]) == 0 or ccw(t[0], t[1], s[1]) == 0:
        return True
    return False


def contains(g: List[complex], p: complex) -> int:
    """Determine if a polygon contains a point.

    Time complexity is O(N), where N = len(g).

    Args:
        g (List of complexes): A simple polygon. This does not have to be
            convex.The order of vertices can be either clockwise or
            counter-clockwise.
        p (complex): A point.

    Returns:
        int: +1 if the polygon strictly contains the point.
            0 if the point is on the border of the polygon.
            -1 otherwise.
    """
    res = -1
    n = len(g)
    for i in range(n):
        a = g[i] - p
        b = g[(i + 1) % n] - p
        if a.imag > b.imag:
            a, b = b, a
        if a.imag <= 0 and 0 < b.imag:
            if cross(a, b) < 0:
                res = -res

        if cross(a, b) == 0 and dot(a, b) <= 0:
            return 0

    return res


def area(g: List[complex]) -> float:
    """Area of a polygon.

    Time complexity is O(N), where N = len(g).

    Args:
        g (List of complexes): A simple polygon. This does not have to be
            convex. The order of vertices can be either clockwise or
            counter-clockwise.
        p (complex): A point.

    Returns:
        float: Area.
    """
    res = 0
    n = len(g)
    for i in range(n):
        res += cross(g[i], g[(i + 1) % n])
    return abs(res) / 2.0


def convex_hull(g: List[complex]) -> List[complex]:
    """Convex hull of given points.

    Time complexity is O(N log N), where N = len(g).

    Args:
        g (List of complexes): A set of points. The order of points
            can be arbitrary.

    Returns:
        List of complexes: The vertices of the convex hull polygon.
            The order of this list will be counter-clockwise.
            The first vertex will be the leftmost vertex in the hull.
    """
    n = len(g)
    g = sorted(g, key=lambda p: (p.real, p.imag))
    k = 0
    ch = [None] * (2 * n)
    for i in range(n):
        while k >= 2 and ccw(ch[k - 2], ch[k - 1], g[i]) == -1:
            k -= 1
        ch[k] = g[i]
        k += 1
    t = k + 1
    for i in range(n - 2, -1, -1):
        while k >= t and ccw(ch[k - 2], ch[k - 1], g[i]) == -1:
            k -= 1
        ch[k] = g[i]
        k += 1
    ch = ch[:k-1]

    return ch


def convex_cut(g: List[complex], s: Tuple[complex, complex]) -> List[complex]:
    """Cuts a convex polygon by a line into two parts, and leave one of them.

    Time complexity is O(N), where N = len(g).

    Args:
        g (List of complexes): A convex polygon. The order of vertices must be
            counter-clockwise.
        s (Tuple of complexes): A line.

    Returns:
        List of complexes: After cutting the polygon by the line s, there will
            be two parts. (One part may be an empty set.)
            Seeing from an arrow s[0]s[1], left-hand side one will be returned.
            Note that returned polygon is also convex.
    """
    res = []
    n = len(g)
    for i in range(n):
        a, b = g[i], g[(i + 1) % n]
        ca = ccw(s[0], s[1], a)
        cb = ccw(s[0], s[1], b)
        if ca != -1:
            res.append(a)
        if ca * cb == -1:
            res.append(intersection_ll((a, b), s))

    return res
