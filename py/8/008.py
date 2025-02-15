from itertools import *

# №1415 kompege

c = 0
for x in product("AB123", repeat=8):
    s = "".join(x)
    s = s.replace("B", "A")
    if s.count("A") == 2:
        c += 1
print(c)

# Ответ: 81648
