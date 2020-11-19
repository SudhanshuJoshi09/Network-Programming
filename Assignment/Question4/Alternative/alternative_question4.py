#!/usr/bin/env python3
import requests, argparse, os
import pathlib
#COMMAND-LINE-ARGUMENTS
parser = argparse.ArgumentParser()
parser.add_argument('-u', '-url', action="store", dest="url", required=True)
given_args = parser.parse_args()
url = given_args.url
file = {}
#LOADING DATA
def load_file():
    global file
    try:
        with open('file.txt', 'r+') as filename:
            lines = filename.readlines()
            for line in lines:
                url, get_date = str(line).split('\t')
                file[url] = get_date.strip('\n')
    except:
        with open('file.txt', 'w+') as filename:
            pass
#STORING DATA
def store_url(url, date):
    if url and date:
        with open('file.txt', 'a+') as filename:
            filename.write(f'{url}\t{date}\n')
load_file()
#GETTING PAGE
def recv_data(url):
    new_url = url
    last_modified = None
    if url in file.keys():
        last_modified = file[url]
    if url.find('http://') == -1 and url.find('https://') == -1:
        new_url = 'http://' + url
    if last_modified:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',  'If-Modified-Since': last_modified, 'Connection': 'closed'}
    else:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Connection': 'closed'}
    result = requests.get(new_url, headers=headers, allow_redirects=False)
    if result.status_code == 301:
        print('Status 301 redirecting')
        recv_data(result.headers['Location'])
    elif result.status_code == 403:
        print('status code 403')
    elif result.status_code == 404:
        print('status code 404')
    elif result.status_code == 200:
        print('Status code 200 writing down')
        if 'Last-Modified' in result.headers.keys():
            store_url(url, result.headers['Last-Modified'])
        newfile = url.replace('http://', '')
        newfile = newfile.replace('https://', '')
        newfile = newfile.split('/')
        if len(newfile) == 2 and newfile[1] == '':
            with open(newfile[0], 'w+') as outputfile:
                outputfile.write(http_resp)
        else:
            pathlib.Path(f'{newfile[0]}' + '/'.join(d for d in newfile[1:len(newfile) - 1]))\
                .mkdir(parents=True, exist_ok=True)
            os.chdir(f'{newfile[0]}'+'/'.join(d for d in newfile[1:len(newfile) - 1]))
            if newfile[-1] == '':
                newfile[-1] = 'index'
            with open(newfile[-1], 'w+') as outputfile:
                outputfile.write(result.text)
    elif result.status_code == 304:
        print('File already present 304')
recv_data(url)