#!/usr/bin/env python3

import ipaddress

# This is for validating the type of ip address. (ipv4/ipv6)
# ipv4
print('-'*100)
print('IPV4')
print('-'*100)
try:
    print (ipaddress.ip_address(u'192.168.0.255'))
except ValueError as e:
    print('This is not a valid IP')

try:
    print (ipaddress.ip_address(u'192.168.0.256'))
except ValueError as e:
    print('This is not a valid IP')

#ipv6
print('-'*100)
print('IPV6')
print('-'*100)
try:
    print (ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:112D'))
except ValueError as e:
    print('This is not a valid IP')

try:
    print (ipaddress.ip_address(u'FFFF:10000:2:FDE:257:0:2FAE:112D'))
except ValueError as e:
    print('This is not a valid IP')
print('-'*100)


print('IP type')
print(type(ipaddress.ip_address(u'192.168.0.255')))
print(type(ipaddress.ip_address(u'2001:db8::')))
print(ipaddress.ip_address(u'192.168.0.255').reverse_pointer)
print(ipaddress.ip_network(u'192.168.0.0/28'))
print('-'*100)