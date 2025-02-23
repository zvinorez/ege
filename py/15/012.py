# №1968 kompege
from itertools import *

m = []


def f(x):
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


Ox = [i / 4 for i in range(16 * 4, 79 * 4)]
for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        m.append(a2 - a1)
print(min(m))

# Ответ: 12
