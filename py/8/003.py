from itertools import *

# №1981 kompege

c = 0
for x in product("ПУЛЯ", repeat=6):
    s = "".join(x)
    if s.count("У") == 2:
        c += 1
print(c)

# Ответ: 1215
