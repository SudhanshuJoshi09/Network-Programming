#!/usr/bin/env python3

import socket

""" Socket timeout function for manipulating TIMEOUT """

def test_socket_timeout():
    # This is a instance of the socket object.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.gettimeout() method is used to get the time out.
    print(f'Default Socket Timeout: {s.gettimeout()}')
    # s.settimeout() method is used to set time out.
    s.settimeout(100)
    print(f'New Socket Timeout: {s.gettimeout()}')


if __name__ == '__main__':
    test_socket_timeout()