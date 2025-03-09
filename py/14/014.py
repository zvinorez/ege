# #256 kompege
def f(x, cc):
    a = []
    while x > 0:
        a = [x % cc] + a
        x = x // cc
    return a


for n in range(1000):
    if len(f(n, 6)) == 2 and len(f(n, 5)) == 3 and f(n, 11)[-1] == 1:
        print(n)
# Ответ: 34
