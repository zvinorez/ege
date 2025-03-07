# №1184 kompege
from itertools import *

s1 = "1457 2567 345 4135 5123467 625 7125"
s2 = "АБВД БДАЕ ВАГД ГДВ ДЖГЕБАВ ЖЕД ЕЖБД"
s2 = {x[0]: set(x[1:]) for x in s2.split()}
for p in permutations("АБВГДЖЕ"):
    s3 = s1
    for x, y in zip("1234567", p):
        s3 = s3.replace(x, y)
    s3 = {x[0]: set(x[1:]) for x in s3.split()}
    if s2==s3:
        print("1 2 3 4 5 6 7")
        print(*p)
# Ответ:17
