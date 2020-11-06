#!/usr/bin/env python3

import socket

# Socket's Blocking and Non-Blocking mode.

def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(('127.0.0.1', 0))

    socket_address = s.getsockname()
    print(f'Trivial Sock launched at: {socket_address}')
    while True:
        s.listen(1)

if __name__ == '__main__':
    test_socket_modes()