# №59 kompege

m = []


def f(x):
    return ((x % 2 == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0)


for a in range(1, 5000):
    if all(f(x) for x in range(1, 5000)):
        m.append(a)
        break
print(min(m))

# Ответ: 16
