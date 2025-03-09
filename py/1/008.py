# №1417 kompege
from itertools import *

s1 = "12356 215 31456 436 5123 6134"
s2 = "АВБГ БАГДЕ ВАГ ГВАБД ДГБЕ ЕДБ"
s2 = {x[0]: set(x[1:]) for x in s2.split()}
for p in permutations("АБВГДЕ"):
    s3 = s1
    for x, y in zip("123456", p):
        s3 = s3.replace(x, y)
    s3 = {x[0]: set(x[1:]) for x in s3.split()}
    if s3 == s2:
        print("1 2 3 4 5 6")
        print(*p)
# Ответ:56
