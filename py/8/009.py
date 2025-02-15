from itertools import *

# №1216 kompege

c = 0
for x in product("01234", repeat=6):
    s = "".join(x)
    if s[0] != "0" and s[0] != "1" and s[5] != "3" and s[5] != "4":
        c += 1
print(c)

# Ответ: 5625
