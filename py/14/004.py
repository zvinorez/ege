# №387 kompege

x = 51 * 7 ** 12 - 7 ** 3 - 22
a = []
while x > 0:
    a = [x % 7] + a
    x //= 7
print(sum(a))

# Ответ: 70
