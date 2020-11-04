#!/usr/bin/env python3 

import sys, argparse, socket

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
        data = b"GET / HTTP/1.1\nHost: google.com\n\n"
        s.send(data)
    except socket.error as e:
        print(f'Error sending data: {e}')
        print(f'section {i}')
        i += 1
        sys.exit(1)

    out_file = open('./file', 'ab')

    while True:
        # This is the forth block for reciveing data.
        try:
            print('I came here')
            try:
                buf = s.recv(10000)
                s.setblocking(0)
            except socket.error as e:
                break
        except socket.error as e:
            print(f'Error reciveing data: {e}')
            print(f'section {i}')
            i += 1

        print(len(buf))
        print('cycle')
        print(buf)

        if len(buf) == 0:
            break

        out_file.write(buf)



if __name__ == '__main__':
    main()