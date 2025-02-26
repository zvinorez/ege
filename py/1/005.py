# №19410 kompege
from itertools import *

s1 = "1245 2136 325 415 5134 62"
s2 = "АДБ БГВА ВЕДБ ГБ ДЕВА ЕВД"
s2 = {x[0]: set(x[1:]) for x in s2.split()}
for p in permutations("АБВГДЕ"):
    s3 = s1
    for x, y in zip("123456", p):
        s3 = s3.replace(x, y)
    s3 = {x[0]: set(x[1:]) for x in s3.split()}
    if s3 == s2:
        print("1 2 3 4 5 6")
        print(*p)

# Ответ: 22