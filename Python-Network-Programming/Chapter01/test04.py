#!/usr/bin/env python3

import socket
from urllib.parse import quote_plus

request_text = """\
GET / \r\n\
HTTP/1.1\r\n\
Host: www.google.com\r\n\
User-Agent: This code was written by sudhanshu Joshi\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
    sock = socket.socket()
    sock.connect(('www.google.com', 80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    rawreply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        rawreply += more

    print(rawreply.decode('unicode_escape'))

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')