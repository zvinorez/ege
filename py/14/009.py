# №1122 kompege

for x in range(1000):
    n = 36 ** 17 - 6 ** x + 71
    a = []
    while n > 0:
        a = [n % 6] + a
        n //= 6
    if sum(a) == 61:
        print(x)

# Ответ: 24
