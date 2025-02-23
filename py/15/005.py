# №216 kompege

m = []


def f(x):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))


for a in range(1, 5000):
    if all(f(x) for x in range(1, 5000)):
        m.append(a)
print(min(m))

# Ответ: 2
