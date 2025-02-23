# №2081 kompege

from itertools import *

bit = ["".join(i) for i in product("01", repeat=8)]


def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not A) <= (P or (not Q))


a = set()
p = {i for i in bit if i[0] + i[1] == "11"}
q = {i for i in bit if i[-1] == "0"}

for x in bit:
    if f(x) == 0:
        a.add(x)
print(len(a))

# Ответ: 96
