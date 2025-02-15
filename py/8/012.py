from itertools import *

# №1961 kompege

c = 0
for x in product(sorted("ЛЕМУР"), repeat=4):
    s = "".join(x)
    c += 1
    if s[0] == "Л":
        break
print(c)

# Ответ: 126
