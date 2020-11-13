#!/usr/bin/env python3 

import sys, argparse, socket, datetime, select, re, os, json, ssl
from urllib.parse import urlparse
from pathlib import Path

CACHE = {}
GET_REQ = """\
GET {} HTTP/1.1\r\n\
Host: {}\r\n\
Accept: text/html\r\n\
Connection: close\r\n\
\r\n\
"""

# Utility Functions -----------------------------------------------------------
def get_cache():
    """ Retrives cache from json to dict format """

    global CACHE
    try:
        with open('cache.json') as json_file:
            CACHE = json.load(json_file)
    except:
        print('Cache file not present')
        with open('cache.json', 'w+') as json_file:
            pass


def update_cache(url, date):
    """ Maps url with the last-modified header """

    for link in cache.keys():
        if parse_url(url).hostname == parse_url(link).hostname and \
            parse_url(url).path == parse_url(link).path:
            break
    else:
        cache[url] = {'last-modified': date}
        with open('cache.json', 'w') as outputfile:
            json.dump(cache, outputfile)
    


def get_args():
    """ Getting in the arguements """

    parser = argparse.ArgumentParser(description='Socket error examples')
    parser.add_argument('--u', '--url', action="store", dest="url", required=False)
    given_args = parser.parse_args()
    url = given_args.url

    return url


def parse_url(url, type='hostname'):
    """ Parses the url into domain and request path """

    if type == 'protocol':
        if url.find('https://') != -1:
            return 443
        else:
            return 80

    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = "//" + url
    res = urlparse(url)

    if type == 'hostname':
        return res.netloc
    elif type == 'path':
        if res.path == '':
            return '/'
        return res.path
    elif type == 'ip':
        return socket.gethostbyname(res.netloc)

# -----------------------------------------------------------------------------


# --------------------------- Socket Functions --------------------------------
def soc_connect(host_name, port=80):
    """ Socket Creation """

    try:
        ip_address = socket.gethostbyname(parse_url(host_name, type='ip'))
        port = parse_url(host_name, 'protocol')
        print(port)
    except socket.gaierror as e:
        print('Error decoding the ip')
        sys.exit(1)
    print(ip_address)
    print(type(port))

    try:
        if port == 80:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)  
    except socket.error as e:
        print(f'Error Creating socket: {e}')
        sys.exit(1)

    try:
        if port == 80:
            s.connect((ip_address, port))
        else:
            ss.connect((ip_address, port))
    except socket.gaierror as e:
        print(f'Address relating error: {e}')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error: {e}')
        sys.exit(1)

    if port == 80:
        return s
    return ss


def get_data(url_name, s, port=80):
    """ This is for getting data """

    try:
        # data = (f'GET {parse_url(url_name, type="path")} HTTP/1.1\r\nContent-Type: text/html\r\nHost: {parse_url(url_name)}\r\n\r\n'.encode())
        data = GET_REQ.format(parse_url(url_name, type='path'), parse_url(url_name)).encode()
        print(data)
        s.send(data)
    except socket.error as e:
        print(f'Error sending data: {e}')
        sys.exit(1)
    
    response = ''
    try:
        buf = s.recv(4096)
    except socket.error as e:
        print(f'Error reciveing data: {e}')
        sys.exit(1)
    #response += buf.decode('cp1252')
    response += buf.decode('cp437')

    while buf:
        try:
            buf = s.recv(10000)
        except socket.error as e:
            print(f'Error reciveing data: {e}')
            sys.exit(1)
        response += buf.decode('cp437')
        #response += buf.decode('cp1252')

    print(response)
    return response, url_name
# -----------------------------------------------------------------------------


# ----------------------- Data Processing Functions ---------------------------
def parse_http_headers(resp_data, url):
    """ Parse's the http headers and html data """
    
    content = resp_data
    resp_headers, resp_html = content.split('\r\n\r\n', 1)
    resp_headers = resp_headers.split('\n')
    status_code = int(resp_headers[0].split(' ')[1])
    header_maps = {}
    base_url = url

    for i in range(1, len(resp_headers)):
        key, val = resp_headers[i].strip('\r').split(': ')
        header_maps[key.lower()] = val.lower()

    date_created = header_maps['date']
    date = None

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
    """ Response to the data recvd. """

    if status_code == 301 or status_code == 302:
        print(f'Status Code: {status_code} redirecting to: {location}')
        skt = soc_connect(location, port=80)
        resp_data, url = get_data(location, skt, port=80)
        status_code, url, date, http_resp = parse_http_headers(resp_data, url)
        process_resp(status_code, url, date, http_resp)
    elif status_code == 403:
        print(f'HTTP/1.1 403 Forbidden\nDate: {date}')
    elif status_code == 404:
        print(f'HTTP/1.1 404 Not Found\nDate: {date}')
    elif status_code == 200:
        if date:
            pass
            #map_urls(url, date)
        resp_write(location, http_resp)


def resp_write(path, http_resp):
    """ Wrting on to the file """

    file_name = parse_url(path, type='path')
    if file_name == '/':
        file_name = ''
    base_dir = parse_url(path)

    if file_name == '':
        file_name = base_dir
        with open(file_name, 'w+') as outputfile:
            outputfile.write(http_resp)
    else:
        file_name = file_name.split('/')
        Path(f'{base_dir}' + '/'.join(d for d in file_name[:len(file_name) - 1])).mkdir(parents=True, exist_ok=True)
        os.chdir(f'{base_dir}'+'/'.join(d for d in file_name[:len(file_name) - 1]))
        if file_name[-1] == '':
            file_name[-1] = 'index'
        with open(file_name[-1], 'w+') as outputfile:
            outputfile.write(http_resp)
    

    
# -----------------------------------------------------------------------------


def main():
    """ This is the main function """

    host_name = get_args()
    skt = soc_connect(host_name)
    resp_data, url = get_data(host_name, skt, port=80)
    status_code, url, date, http_resp = parse_http_headers(resp_data, url)
    process_resp(status_code, url, date, http_resp)
    

if __name__ == '__main__':
    main()