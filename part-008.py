#!/usr/bin/env python3 

import sys, argparse, socket, uuid
from datetime import datetime


def store_data(host_name, mode='ab'):
    gen_rand_str = str(uuid.uuid4())
    print(gen_rand_str)



def main():
    """ This is the main function """

    """
    out_file = open('./file', 'ab')

    while True:
        # This is the forth block for reciveing data.
        try:
            try:
                buf = s.recv(10000)
                s.setblocking(0)
            except socket.error as e:
                break
        except socket.error as e:
            print(f'Error reciveing data: {e}')
            print(f'section {i}')
            i += 1

        out_file.write(buf)
    """
    store_data('something')

if __name__ == '__main__':
    main()


"""
def get_input():

    parser = argparse.ArgumentParser(description='Socket error examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    given_args = parser.parse_args()
    host_name = given_args.host

    return host_name

def connect(host_name):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Error Creating socket: {e}')
        sys.exit(1)

    try:
        s.connect((host_name, port=80))
    except socket.gaierror as e:
        print(f'Address relating error: {e}')
    except socket.error as e:
        print(f'Connection error: {e}')
        sys.exit(1)

    return s

def get_request(s, host_name):

    try:
        data = b"GET / HTTP/1.1\nHost: {host_name}\n\n"
        s.send(data)
    except socket.error as e:
        print(f'Error sending data: {e}')
        sys.exit(1)

def parse_response():
    pass
"""