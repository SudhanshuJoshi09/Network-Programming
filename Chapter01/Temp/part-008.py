#!/usr/bin/env python3

"""
Modifying socket's send/receive buffer sizes
"""

import socket

# setsockopt() method is used.
# Two constants define SEND_BUF_SIZE, RECV_BUF_SIZE

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buffer_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Getting the size of the previous send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(f'Buffer Size [before]: {bufsize}')
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE
    )
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE
    )
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(f'Buffer Size [after]: {bufsize}')


if __name__ == '__main__':
    modify_buffer_size()