# №10570 kompege
from ipaddress import *

for mask in range(33):
    net = ip_network(f"154.201.208.17/{mask}", 0)
    print(net, net.netmask)

# Ответ: 224
