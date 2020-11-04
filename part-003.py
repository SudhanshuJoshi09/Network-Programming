#!/usr/bin/env python3

""" This program deals with conversion of the ipv4 address to bin format """
import socket
# hexadecimal repr of binary data.
from binascii import hexlify

def convert_ip4_address():
    """ Converts the ip4 address format """

    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        # inet_aton converts ip string to hex format.
        packed_ip_addr = socket.inet_aton(ip_addr)
        # This unpacks the hex format to doted reqr.
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address: %s\nPacked: %s\nUnpacked: %s"\
            % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))
        
if __name__ == '__main__':
    convert_ip4_address()