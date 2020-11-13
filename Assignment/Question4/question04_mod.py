#!/usr/bin/env python3 

import request
from urllib.parse import urlparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('--u', '--url', action="store", dest="url", required=False)
given_args = parser.parse_args()
url = given_args.url

file = {}
try:
    with open('file.json', 'r') as data_file:
        file = json.load(data_file)
except:
    with open('file.json', 'w+') as data_file:
        pass

def store_data(url, date=None):
    """ Maps url with the last-modified header """

    if date:
        for link in CACHE.keys():
            if parse_url(url) == parse_url(link) and \
                parse_url(url, type='path') == parse_url(link, type='path'):
                break
        else:
            CACHE[url] = {'last-modified': date}
            with open('cache.json', 'w') as outputfile:
                json.dump(CACHE, outputfile)
    else:
        for link in CACHE.keys():
            if parse_url(url) == parse_url(link) and \
                parse_url(url, type='path') == parse_url(link, type='path'):
                return CACHE[url]['last-modified']
        else:
            return None
# This is for when we create the file.
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
        resp_write(location, http_resp)
    elif status_code == 304:
        print(f'HTTP/1.1 304 Not Modified\nDate: {date}')


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
        Path(f'{base_dir}' + '/'.join(d for d in file_name[:len(file_name) - 1]))\
            .mkdir(parents=True, exist_ok=True)
        os.chdir(f'{base_dir}'+'/'.join(d for d in file_name[:len(file_name) - 1]))
        if file_name[-1] == '':
            file_name[-1] = 'index'
        with open(file_name[-1], 'w+') as outputfile:
            outputfile.write(http_resp)

    
# -----------------------------------------------------------------------------
def main():
    """ main Funtion """
    

if __name__ == '__main__':
    main()