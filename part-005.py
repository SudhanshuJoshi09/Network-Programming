#!/usr/bin/env python3
""" Interger Conversion function"""

import socket


def convert_integer():
    data = 1234
    # 32-bits
    print('Orignal: %s\nLong Host byte order: %s\nNetwork Byte Order: %s' \
        % (data, socket.ntohl(data), socket.htonl(data)))
    # 16-bits
    print('Orignal: %s\nShort Host byte order: %s\nNetwork Byte Order: %s' \
        % (data, socket.ntohs(data), socket.htons(data)))

if __name__ == '__main__':
    convert_integer()