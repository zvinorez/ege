# №1929 kompege
from itertools import *

c = 0
for p in permutations("ДЕЙКСТРА", 6):
    s = "".join(p)
    s = s.replace("К", "Д").replace("С", "Д").replace("Т", "Д") \
        .replace("Р", "Д")
    if s.count("Й") == 1 and "ЙД" in s:
        c += 1
print(c)
# Ответ: 9000
