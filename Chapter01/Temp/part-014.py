#!/usr/bin/env python3
""" This is the client appliction """

import socket, sys, argparse

host = 'localhost'

def echo_client(port):
    """ A simple client """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connet the socket to the server
    server_address = (host, port)
    print(f'Connecting to : {server_address}')
    sock.connect(server_address)

    # Send data
    try:
        # Send data
        message = "Text message. This will be echoed"
        print(f'Send {message}')
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_expected > amount_received:
            data = sock.recv(15)
            amount_received += len(data)
            print(f'received: {data.decode()}')
    except socket.error as e:
        print(f'Socket Error: {e}')
    except Exception as e:
        print(f'Other exception: {e}')
    finally:
        print('Closing connection to the server')
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)


