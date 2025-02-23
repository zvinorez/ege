# №948 kompege

m = []


def f(x):
    return (((x % 4 != 3)) or (x % 6 != 1)) <= (x % 36 != a)


for a in range(1, 5000):
    if all(f(x) for x in range(1, 5000)):
        m.append(a)
        break
print(min(m))

# Ответ: 7
