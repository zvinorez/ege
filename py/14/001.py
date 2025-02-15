# №58 kompege

x = 64 ** 30 + 2 ** 300 - 4
a = []
while x > 0:
    a = [x % 8] + a
    x //= 8
print(a.count(7))

# Ответ: 59
