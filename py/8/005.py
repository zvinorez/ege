from itertools import *

# №1983 kompege

c = 0
for x in product("САЛО", repeat=6):
    s = "".join(x)
    if 0 < s.count("О") <= 3:
        c += 1
print(c)

# Ответ: 3213
