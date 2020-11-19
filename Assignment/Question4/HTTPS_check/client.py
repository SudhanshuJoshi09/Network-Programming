#!/usr/bin/env python3
# Client.py
import os
import requests

def get_secret_msg():
    url = os.environ['SECRET_URL']
    response = requests.get(url)
    print(f'The secret msg is {response.text}')


if __name__ == '__main__':
    get_secret_msg()