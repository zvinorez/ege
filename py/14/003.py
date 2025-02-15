# №234 kompege

x = 2*27**7+3**10-9
a = []
while x > 0:
    a = [x % 3] + a
    x //= 3
print(a.count(0))

# Ответ:13
