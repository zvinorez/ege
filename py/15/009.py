# №1015 kompege

m = []


def f(x, y):
    return (x > 39) or (y > 26) or (2 * x + 4 * y < a)


for a in range(500):
    if all(f(x, y) for x in range(500) for y in range(500)):
        m.append(a)
        break
print(min(m))

# Ответ: 183
