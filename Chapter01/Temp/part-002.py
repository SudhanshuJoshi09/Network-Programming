#!/usr/bin/env python3


import socket


def get_machine_details(host_name):
    """ Prints the ip from the given host_name """

    try:
        print(f'The IP addr of host is: {socket.gethostbyname(host_name)}')
    except socket.error as e:
        print(f'{socket.error} and {e}')

if __name__ == '__main__':
    get_machine_details('google.com')