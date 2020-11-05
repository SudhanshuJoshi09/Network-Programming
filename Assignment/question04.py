#!/usr/bin/env python3 


"""
WORK is UNDER PROGRESS !!!
THIS PROGRAM IS NOT FINISHED YET !!!
"""



import sys, argparse, socket, datetime, select
#from urllib.parse import urlparse

# class RedirectResponse:
def get_args():
    """ Getting in the arguements """

    parser = argparse.ArgumentParser(description='Socket error examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    given_args = parser.parse_args()
    host = given_args.host

    return host

def soc_connect(host_name, port=80):
    """ Socket Creation """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Error Creating socket: {e}')
        print('Check one')
        sys.exit(1)

    try:
        #parsed_url = urlparse(host_name)
        #result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
        #print(result)
        #s.connect((result, port))
        s.connect((host_name, port))
    except socket.gaierror as e:
        print(f'Address relating error: {e}')
        print('Check two')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error: {e}')
        print('Check three')
        sys.exit(1)

    return s

def get_data(host_name, s, port=80):
    """ This is for getting data """

    try:
        data = (f"GET ./workshops/workshops.html HTTP/1.1\r\n\r\n").encode()
        s.send(data)
    except socket.error as e:
        print(f'Error sending data: {e}')
        print('Check four')
        sys.exit(1)
    
    response = ''

    while True:
        try:
            buf = s.recv(10000)
        except socket.error as e:
            print(f'Error reciveing data: {e}')
            print('Check five')
            sys.exit(1)
        
        response += buf.decode()
        print(response)

    return response


def resp_write(path, http_resp):
    with open(path, 'ab') as outputfile:
        outputfile.write(http_resp)

def parse_http_headers(resp_data):
    content = resp_data
    #content = content.decode("utf-8") 
    headers, *html_resp = content.split('\\n\\n')
    html_resp = '\n\n'.join(html_resp)
    header_list = headers.split('\n')
    status = header_list[0].split(' ')
    status_code = int(status[1])
    header_maps = {}
    print(headers)

    '''

    for i in range(1, len(header_list)):
        key, val = header_list[i].split(': ')
        header_maps[key.lower()] = val
    '''

    '''
    if status_code == 301 or status_code == 302:
        return status_code, header_maps['location'], None, None
    elif status_code == 403:
        return status_code, None, header_maps['date'], None
    elif status_code == 404:
        return status_code, None, header_maps['date'], None
    elif status_code == 200:
        return status_code, base_url, header_maps['date'], content
    '''

def process_resp(status_code, location, date, http_resp, skt):
    if status_code == 301 or status_code == 302:
        print(f'Status Code: {status_code} redirecting to: {location}')
        get_data(location, skt, port=80)
    elif status_code == 403:
        print(f'HTTP/1.1 403 Forbidden\nDate: {date}')
    elif status_code == 404:
        print(f'HTTP/1.1 404 Not Found\nDate: {date}')
    elif status_code == 200:
        resp_write(location, http_resp)

def main():
    """ This is the main function """

    host_name = get_args()
    skt = soc_connect(host_name)
    resp_data = get_data(host_name, skt, port=80)
    parse_http_headers(resp_data)
    # status_code, location, date, http_resp = parse_http_headers(resp_data)
    # process_resp(status_code, location, date, http_resp, skt)
    

if __name__ == '__main__':
    main()