from itertools import *

# №1984 kompege

c = 0
for x in permutations("ИГРОК"):
    s = "".join(x)
    if s[0] != "К" and "РОК" not in s:
        c += 1

print(c)

# Ответ: 90
