#!/usr/bin/env python3
import socket

def print_host_details():
    """ This is a demo to show class based utility functions """

    # This get's the hostname.
    host_name = socket.gethostname()
    print(f'Host name: {host_name}')

    # This get's the ip address of the host.
    ip_addr = socket.gethostbyname(host_name)
    print(f'IP address: {ip_addr}')


if __name__ == '__main__':
    print_host_details()