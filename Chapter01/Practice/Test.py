#!/usr/bin/env python3

import socket, sys, requests

def main():
    if sys.argv[1].find('http://') or sys.argv[1].find('https://'):
        valid_url = 'http://' + sys.argv[1]

    ip_addr = socket.gethostbyname(sys.argv[1])
    print(ip_addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.bind((ip_addr, 80))
    x = requests.head(valid_url)
    print(x.headers)
    con_leng=int(x.headers['Content-Length'])
    print(con-leng)

    #sock.send()

if __name__ == '__main__':
    main()