#!/usr/bin/env python3

import socket, argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--h', '--host', action='store', dest='host', required=False)
    arguements = parser.parse_args()
    host = arguements.host
    print(socket.gethostbyname(host))
