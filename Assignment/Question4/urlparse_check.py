from urllib.parse import urlparse
import socket, json

#val = input().lower()
def parse_url(url, type='hostname'):
    """ Parses the url into domain and request path """

    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = "//" + url
    res = urlparse(url)

    if type == 'hostname':
        return res.netloc
    elif type == 'path':
        return res.path
    elif type == 'ip':
        return socket.gethostbyname(res.netloc)

data = {'url': 'www.google.com', 'www.google.com': {'last-modified': 1999}}

with open('cache.json', 'w') as filename:
    json.dump(data, filename)


with open('cache.json') as json_file:
    data = json.load(json_file)
    print(data)