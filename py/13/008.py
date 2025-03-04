# №10579 kompege
from ipaddress import *

c = 0

net = ip_network("192.168.240.0/255.255.255.0")
a = list(net.hosts())
for ip in a:
    b = f"{ip:b}"
    if b.count("0") == b.count("1"):
        c += 1
print(c)
# Ответ: 8
