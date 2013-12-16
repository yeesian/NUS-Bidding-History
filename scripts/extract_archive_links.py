from lxml.html import iterlinks
import urllib3

http = urllib3.PoolManager()
url = 'http://www.nus.edu.sg/cors/archive.html'
r = http.request('GET', url)

for link in iterlinks(r.data):
  if 'Archive/' in link[2]:
    if link[2][:2] == './':
      print('http://www.cors.nus.edu.sg/'+link[2][2:])
    else:
      print(link[2])

url2 = 'http://www.nus.edu.sg/cors/useful-info.html'
r = http.request('GET', url2)
for link in iterlinks(r.data):
  if link[2][2:9] == 'Reports':
    print('http://www.nus.edu.sg/cors/Reports/'+link[2][10:])