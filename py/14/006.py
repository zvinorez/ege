# №2235 kompege

x = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
a = []
while x > 0:
    a = [x % 15] + a
    x //= 15
print(len(set(a)))

# Ответ: 10
