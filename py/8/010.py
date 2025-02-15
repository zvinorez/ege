from itertools import *

# №10090 kompege

c = 0
for x in permutations("0234567", 5):
    s = "".join(x)
    if s[0] != "0":
        s = s.replace("2", "0").replace("4", "0").replace("6", "0") \
            .replace("3", "1").replace("5", "1").replace("7", "1")
        if "00" not in s and "11" not in s:
            c += 1
print(c)

# Ответ: 180
