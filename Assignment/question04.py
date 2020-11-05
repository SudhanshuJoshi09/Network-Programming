#!/usr/bin/env python3 

import sys, argparse, socket, datetime


def get_args():
    """ Getting in the arguements """

    parser = argparse.ArgumentParser(description='Socket error examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    given_args = parser.parse_args()
    host = given_args.host

def soc_connect(host_name, port=80):
    """ Socket Creation """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Error Creating socket: {e}')
        sys.exit(1)

    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f'Address relating error: {e}')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error: {e}')
        sys.exit(1)

def get_data(host_name, port=80):
    """ This is for getting data """

    try:
        data = b"GET / HTTP/1.1\nHost: google.com\n\n"
        s.send(data)
    except socket.error as e:
        print(f'Error sending data: {e}')
        sys.exit(1)


def create_file(path, s):
    with open(path, 'ab') as outputfile
        while True:
            try:
                try:
                    buf = s.recv(10000)
                    s.setblocking(0)
                except socket.error as e:
                    break
            except socket.error as e:
                print(f'Error reciveing data: {e}')

            outputfile.write(buf)


def parse_http_headers():
    filename = open('file', 'rb')
    content = filename.read()
    content = content.decode("utf-8") 
    headers, *html_resp = content.split('\n\n')
    html_resp = '\n\n'.join(html_resp)
    header_list = headers.split('\n')
    status = header_list[0].split(' ')
    status_code = int(status[1])
    header_maps = {}

    for i in range(1, len(header_list)):
        key, val = header_list[i].split(': ')
        header_maps[key.lower()] = val

    if status_code == 301 or status_code == 302:
        return status_code, header_maps['location'], None, None
    elif status_code == 403:
        return status_code, None, header_maps['date'], None
    elif status_code == 404:
        return status_code, None, header_maps['date'], None
    elif status_code == 200:
        return status_code, None, header_maps['date'], content

def process_resp(status_code, location, date, http_resp):
    if status_code == 301 or status_code == 302:
        print(f'Status Code: {status_code} redirecting to: {location}')
    elif status_code == 403:
        print(f'HTTP/1.1 403 Forbidden\nDate: {date}')
    elif status_code == 404:
        print(f'HTTP/1.1 404 Not Found\nDate: {date}')
    elif status_code == 200:
        create_file(http_resp)
        print(status_code, location, date, html_resp, sep='\n')

def main():
    """ This is the main function """

    status_code, location, date, http_resp = parse_http_headers()
    process_resp(status_code, location, date, http_resp)
    

if __name__ == '__main__':
    main()