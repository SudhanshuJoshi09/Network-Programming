#!/usr/bin/env python3

import requests
import sys
import multiprocessing
import argparse
from urllib.request import urlopen


def get_args():
    """ Command line arguments """

    parser = argparse.ArgumentParser(
        description='Get Info for socket creation')
    parser.add_argument('-u', '--url', action='store', required=True)
    parser.add_argument('-p', '--parallelconnections',
                        type=int, action='store', required=True)
    given_args = parser.parse_args()
    url = given_args.url
    conn = given_args.parallelconnections

    print(f'url: {url}\t No of parallel connections : {conn}')
    return url, conn


def checkProtocol(url):
    """ Check's the protocol used by the link """

    if url.find('http://') == -1 and url.find('https://'):
        return 'https://' + url
    return url


def get_content_len(url):
    """ Get's the Content Length """

    url = checkProtocol(url)
    print(url)
    op = urlopen(url)
    print(op)
    content_len = int(op.headers['content-length'])
    print(f"The content length of given url is {content_len}")
    if op.headers['Accept-Ranges'] == 'bytes':
        flag = True
        return flag, content_len
    else:
        flag = False
        print("given ulr does not support partial content")
        return flag, content_len

    return content_len
#computing ranges


def comp_ranges(content_len, con):
    """computing ranges"""
    div = content_len//con
    ls = []
    for i in range(0, content_len, div):
        ls.append(i)
    diff = content_len-ls[len(ls)-1]
    b = ls[len(ls)-1]+diff
    if len(ls) == con+1:
        ls.pop()
        ls.append(b)
    else:
        ls.append(b)
    ranges = list(zip(ls, ls[1:] + ls[:1]))
    ranges.pop()
    print(
        f"The computed ranges for given content length {content_len } and no of parallel connections {con} is {ranges}")
    return ranges
#geting partial  and writing into a file


def get(con, ranges):
    start = ranges[0]
    end = ranges[1]
    headers = {"Range": f"bytes={start}-{end}", "Accept-Encoding": None}
    r = requests.get(url, stream=True, headers=headers)
    content = r.content
    with open('output', 'a+') as outputfile:
        outputfile.write(str(content.decode()))


#creating parallel connections
def create_conn(con, values, true):

    if true:
        processes = []
        for _ in range(con):
            proces = multiprocessing.Process(target=get, args=[con, values])
            proces.start()
            processes.append(proces)
        for pro in processes:
            pro.join()
        print("the Total content is present in output file")


def main():
    """ Program execution start's here """

    url, conn = get_args()
    flag, content_len = get_content_len(url)
    values = comp_ranges(content_len, conn)
    create_conn(conn, values, flag)


if __name__ == '__main__':
    main()
