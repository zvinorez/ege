# #4964 kompege
def f(y):
    try:
        n1 = int(f"12{y}{x}9", 21)
        n2 = int(f"36{y}99", 21)
        return (n1 + n2) % 18 == 0
    except:
        ...


for x in range(21):
    if all(f(y) for y in range(21)):
        a = int(f"12{5}{x}9", 21) + int(f"36{5}99", 21)
        print(a // 18)
        break
# Ответ: 47594

# чисто на смекалочке бредик накалякал, kompege предлагает такое решение:
# for x in range(21):
#     for y in range(21):
#         a = 4 * 21 ** 4 + 8 * 21 ** 3 + 2 * 21 ** 2 + (x + 9) * 21 + 18
#         if a % 18 == 0:
#             print(x, y, a // 18)
#
