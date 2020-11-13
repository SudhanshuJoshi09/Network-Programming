#!/usr/bin/env python3

import requests

def geocode(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)

    answer = response.json()
    try:
        print(answer['results'][0]['geometry']['location'])
    except:
        print(answer)

if __name__ == '__main__':
    geocode('Tilak Marg, Mandi House, New Delhi, Delhi 110001')