# №627 kompege

m = []


def f(x, y):
    return (x * y > a) and (x > y) and (x < 8)


for a in range(500):
    if all(f(x, y) == 0 for x in range(500) for y in range(500)):
        m.append(a)
        break
print(min(m))

# Ответ: 42
