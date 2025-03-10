# #1409 kompege

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
r = {12, 24, 36, 48, 60}
a = set()


def f(x):
    P = x in p
    Q = x in q
    R = x in r
    A = x in a
    return (not A) <= ((P and Q) <= R)


for x in range(10000):
    if f(x) == 0:
        a.add(x)

c = 1
for n in a:
    c *= n
print(c)

# Ответ: 108