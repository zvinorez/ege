# №764 kompege

m = []


def f(x):
    return ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0))


for a in range(1, 5000):
    if all(f(x) for x in range(1, 5000)):
        m.append(a)
        break
print(min(m))

# Ответ: 7
