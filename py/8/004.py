from itertools import *

# №1982 kompege

c = 0
for x in product("ЛОДКА", repeat=4):
    s = "".join(x)
    if s.count("О") >= 2:
        c += 1
print(c)

# Ответ: 113
