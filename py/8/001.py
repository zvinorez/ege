from itertools import *

# №1979 kompege

c = 0
for x in product("КРСЛ", "КРЕСЛО", "КРЕСЛО", "ЕО"):
    c+=1
print(c)

# Ответ: 288