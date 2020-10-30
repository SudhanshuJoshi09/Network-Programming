import urllib2
response = urllib2.urlopen('http://workshops.rprustagi.com')
html = response.info()
print html