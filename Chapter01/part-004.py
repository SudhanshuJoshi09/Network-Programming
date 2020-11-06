#!/usr/bin/env python3

import socket


def find_service_name():
    """ Print's the service assosicted with the given port """

    protocolname = 'tcp'
    for port in [80, 25]:
        print('Port No: %s ==> Service Name: %s' \
            %(port, socket.getservbyport(port, protocolname)))

if __name__ == '__main__':
    find_service_name()