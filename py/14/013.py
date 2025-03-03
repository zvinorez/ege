# №1222 kompege

n = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
a = []
while n > 0:
    a = [n % 6] + a
    n //= 6
print(a.count(5) - a.count(0))

#Ответ: 1182