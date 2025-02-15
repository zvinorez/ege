from itertools import *

# №1985 kompege

c = 0
for x in permutations("АБИКОЛУН"):
    s = "".join(x)
    s = s.replace("И", "А").replace("О", "А").replace("У", "А") \
        .replace("К", "Б").replace("Л", "Б").replace("Н", "Б")
    if "АА" not in s and "ББ" not in s:
        c += 1
print(c)

# Ответ: 1152
