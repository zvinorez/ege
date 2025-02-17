# №2033 kompege

x = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
a = []
while x > 0:
    a = [x % 12] + a
    x //= 12
print(a.count(11))

# Ответ: 51
