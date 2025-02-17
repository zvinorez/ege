# 1071 № kompege

for x in range(1000):
    n = 125 ** 200 - 5 ** x + 74
    a = []
    while n > 0:
        a = [n % 5] + a
        n //= 5
    if a.count(4)==100:
        print(x)

# Ответ: 502
