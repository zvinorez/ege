# #83 kompege
from itertools import *


def f(x, y, z, w):
    return (x and (not y)) or (x == z) or w


for a in product([0, 1], repeat=6):
    table = [(1, a[0], a[1], 1), (a[2], 0, a[3], 0), (1, a[4], 1, a[5])]
    for p in permutations("xyzw"):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            print(*p, sep="")

# Ответ: ywzx
