import urllib3
import requests
http = urllib3.PoolManager()

resp = http.request('GET', 'http://cse.ksit.edu.in')
print resp.data

# get the status of the response
print resp.status