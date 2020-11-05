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

def create_file(path, ):
    """
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

        if len(buf) == 0:
            break

        out_file.write(buf)
    pass
    """
    basename = "mylogfile"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix]) # e.g. 'mylogfile_120508_171442'
    print(filename)

def parse_http_headers():
    filename = open('file', 'rb')
    content = filename.read()
    content = content.decode("utf-8") 
    headers, *html_resp = content.split('\n\n')
    print(headers)
    print()
    html_resp = '\n\n'.join(html_resp)
    print(html_resp)
    header_list = headers.split('\n')
    status = header_list[0].split(' ')
    print(int(status[1]))

def main():
    """ This is the main function """

    #create_file('text')
    parse_http_headers()
    

if __name__ == '__main__':
    main()