from itertools import *

# №1980 kompege

c = 0
for x in product("WXYZ", "ABC", "ABC", "ABC", "ABC", "WXYZ"):
    c += 1
print(c)

# Ответ: 1296
