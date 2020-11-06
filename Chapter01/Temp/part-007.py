#!/usr/bin/env python3 

import sys, argparse, socket
"""
1. Address relating error: [Errno 8] nodename nor servname provided, or not
   known
This happens when the hostname is not correct or does not exists.

2. Connection error: [Errno 60] Operation timed out
This happens if the server is not listening on the port provided.
"""


def main():
    """ This is the main function """

    # This is for setting up argparse
    parser = argparse.ArgumentParser(description='Socket error examples')
    # Adding the arguements.
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    # parsing the arguments
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    i = 1

    # This try block is for creating the socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Error Creating socket: {e}')
        print(f'section {i}')
        i += 1
        sys.exit(1)


    # This second block here connect you to given host and port.
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f'Address relating error: {e}')
        print(f'section {i}')
        i += 1
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error: {e}')
        print(f'section {i}')
        sys.exit(1)
    
    # This is the third block for sending data.
    try:
        s.sendall(f'GET {filename} HTTP/1.0\r\n\n\n'.encode())
    except socket.error as e:
        print(f'Error sending data: {e}')
        print(f'section {i}')
        i += 1
        sys.exit(1)


    while True:
        # This is the forth block for reciveing data.
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print(f'Error reciveign data: {e}')
            print(f'section {i}')
            i += 1
            sys.exit(1)

        if not len(buf):
            break

        # write the recived data.
        sys.stdout.write(buf.decode())


if __name__ == '__main__':
    main()