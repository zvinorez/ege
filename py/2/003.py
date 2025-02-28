# №79 kompege

from itertools import *


def f(x, y, z, w):
    return (not w) and ((y or z) <= ((not x) and y))


for a in product([0, 1], repeat=8):
    table = [(a[0], a[1], a[2], 1),
             (a[3], a[4], 1, a[5]),
             (a[6], 1, 1, a[7])]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p, sep="")

# Ответ: wzyx
