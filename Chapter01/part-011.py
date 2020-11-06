#!/usr/bin/env python3
""" Printing the current time from the internet time server """

import ntplib
from time import ctime 


def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print(ctime(response.tx_time))

if __name__ == '__main__':
    print_time()
