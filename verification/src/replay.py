"""Exact finite checks for the preference likelihood, scaling and worked example."""

from fractions import Fraction as F
from itertools import product


def dot(left, right):
    return sum(a*b for a, b in zip(left, right))


def squared_distance(left, right):
    return sum((a-b)**2 for a, b in zip(left, right))


def check_label_loss():
    checked = 0
    for a, i, j in product((F(1, 10), F(1, 4), F(1)), range(-6, 7), range(-4, 5)):
        b, t = F(i, 3), F(j, 5)
        if b == t or b == 0:
            continue
        z = 1 if t > b else -1
        scaled = z*b/a
        # The common nonlinear term is log(1+exp(-abs(scaled))).
        # Compare its argument and the remaining term by rational arithmetic.
        assert abs(scaled) == abs(b)/a
        flip = min(0, t) < b < max(0, t)
        assert max(0, scaled) == (abs(b)/a if flip else 0)
        checked += 1
    assert checked == 324
    print(f"{checked} exact logistic log-loss decompositions")


def check_risk_scales():
    checked = 0
    for d in range(1, 31):
        for n in (1, d, max(1, d*d-1), d*d, d*d+1, 10*d**3):
            a2 = min(F(1, n), F(d*d, n*n))
            assert n*a2 <= 1 and n*n*a2 <= d*d
            assert d*a2 == min(F(d, n), F(d**3, n*n))
            assert (F(d, n) <= F(d**3, n*n)) == (n <= d*d)
            checked += 1
    print(f"{checked} exact information scale and crossover checks")


def check_worked_cube():
    offset = F(1, 16)
    zero = (F(0),)*3
    normals = [tuple(F(sign if j == axis else 0) for j in range(3))
               for axis in range(3) for sign in (-1, 1)]
    pairs = []
    for u in normals:
        midpoint = tuple(offset*x for x in u)
        x = tuple(m+v/2 for m, v in zip(midpoint, u))
        y = tuple(m-v/2 for m, v in zip(midpoint, u))
        assert squared_distance(zero, x) > squared_distance(zero, y)
        pairs.append((x, y))

    coordinates = (-1, -2*offset, -offset, F(0), offset, 2*offset, 1)
    for h in product(coordinates, repeat=3):
        for u, (x, y) in zip(normals, pairs):
            margin = dot(u, h)-offset
            assert squared_distance(h, y)-squared_distance(h, x) == 2*margin
        consistent = all(squared_distance(h, y) <= squared_distance(h, x) for x, y in pairs)
        assert consistent == all(abs(x) <= offset for x in h)
    assert 3*offset**2 == F(3, 256) < F(1, 4)
    # The cut is among the proof's small offsets at radius t=1/2.
    assert offset**2 < F(1, 4)/48
    for removed in normals:
        h = tuple(F(3, 4)*x for x in removed)
        assert dot(removed, h) > offset
        assert all(dot(u, h) <= offset for u in normals if u != removed)
        assert squared_distance(h, zero) > F(1, 4)
    print("343 exact geometry fixtures and six released-face witnesses")


if __name__ == "__main__":
    check_label_loss()
    check_risk_scales()
    check_worked_cube()
