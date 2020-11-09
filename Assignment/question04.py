#!/usr/bin/env python3 

import sys, argparse, socket, datetime, select, re, os

# class RedirectResponse:
def get_args():
    """ Getting in the arguements """

    parser = argparse.ArgumentParser(description='Socket error examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    given_args = parser.parse_args()
    host = given_args.host

    return host

def parse_url(url, hostname = True):
    """ Parsing url into hostname and formated url """

    if hostname:
        result = re.sub(r'(.*://)?([^/?]+).*', '\g<1>\g<2>', url)
        result = result.strip('http://')
        result = result.strip('https://')
    else:
        result = url
        result = result.replace("http://","")
        result = result.replace("https://","")
        if result[-1] == '/':
            result = result[:len(result) - 1]
        if result[:3] != 'www':
            result = 'www.' + result

    return result


def soc_connect(host_name, port=80):
    """ Socket Creation """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Error Creating socket: {e}')
        print('Check one')
        sys.exit(1)

    try:
        ip_address = socket.gethostbyname(parse_url(host_name))
    except socket.gaierror as e:
        print(e)
        sys.exit(1)

    try:
        s.connect((ip_address, port))
    except socket.gaierror as e:
        print(f'Address relating error: {e}')
        print('Check two')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error: {e}')
        print('Check three')
        sys.exit(1)

    return s

def extract_req(url_name):
    """ Extracts the request """
    
    args = url_name.split('.com')
    if len(args) == 2:
        return args[1] + '/'


def get_data(url_name, s, port=80):
    """ This is for getting data """

    try:
        if not extract_req(url_name):
            data = (f'GET / HTTP/1.1\r\nHost: {parse_url(url_name, hostname=False)}\r\n\r\n'.encode())
        else:
            data = f'GET {extract_req(url_name)} HTTP/1.0\r\nHost: {parse_url(url_name)}\r\n\r\n'.encode()
        s.send(data)
    except socket.error as e:
        print(f'Error sending data: {e}')
        print('Check four')
        sys.exit(1)
    
    response = ''
    try:
        buf = s.recv(4096)
    except socket.error as e:
        print(f'Error reciveing data: {e}')
        print('Check five')
        sys.exit(1)
    response += buf.decode('cp1252')

    while buf:
        try:
            buf = s.recv(10000)
        except socket.error as e:
            print(f'Error reciveing data: {e}')
            print('Check five')
            sys.exit(1)
        response += buf.decode('cp1252')

    return response, parse_url(url_name)


def resp_write(path, http_resp):
    """ Wrting on to the file """

    file_name = extract_req(path)
    file_name = file_name.replace('/', '').strip('/')
    file_path = parse_url(path).replace('/', '')
    file_name = file_path + '-' + file_name
    if not file_name:
        file_name = 'something'
    with open(file_name, 'w+') as outputfile:
        outputfile.write(http_resp)

def parse_http_headers(resp_data, url):
    """ Parse's the http headers """
    
    content = resp_data
    resp_headers, resp_html = content.split('\r\n\r\n')
    resp_headers = resp_headers.split('\n')
    status_code = int(resp_headers[0].split(' ')[1])
    header_maps = {}
    base_url = url

    for i in range(1, len(resp_headers)):
        key, val = resp_headers[i].strip('\r').split(': ')
        header_maps[key.lower()] = val.lower()

    date_created = header_maps['date']

    if 'last-modified' in header_maps.keys():
        date = header_maps['last-modified']

    if status_code == 301 or status_code == 302:
        return (status_code, header_maps['location'], None, None)
    elif status_code == 403:
        return (status_code, None, date_created, None)
    elif status_code == 404:
        return (status_code, None, date_created, None)
    elif status_code == 200:
        return (status_code, base_url, date, content)


def process_resp(status_code, location, date, http_resp):
    if status_code == 301 or status_code == 302:
        print(f'Status Code: {status_code} redirecting to: {location}')
        skt = soc_connect(location, port=80)
        resp_data, url = get_data(location, skt, port=80)
        status_code, url, date, http_resp = parse_http_headers(resp_data, url)
        process_resp(status_code, location, date, http_resp)
    elif status_code == 403:
        print(f'HTTP/1.1 403 Forbidden\nDate: {date}')
    elif status_code == 404:
        print(f'HTTP/1.1 404 Not Found\nDate: {date}')
    elif status_code == 200:
        if date:
            print('Last-Modified: ', date)
        resp_write(location, http_resp)

def main():
    """ This is the main function """

    host_name = get_args()
    skt = soc_connect(host_name)
    resp_data, url = get_data(host_name, skt, port=80)
    status_code, url, date, http_resp = parse_http_headers(resp_data, url)
    process_resp(status_code, url, date, http_resp)
    
if __name__ == '__main__':
    main()