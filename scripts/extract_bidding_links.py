from lxml.html import iterlinks
import urllib3
import re
import sys

url = 'https://sit.aces01.nus.edu.sg/cors/jsp/report/GlobalBidHistDetails.jsp'

def main():
  http = urllib3.PoolManager()
  r = http.request('GET', url)
  for link in iterlinks(r.data):
      if link[2][:6] == 'Global': # a quick hack, to match the head of the string
        print(r'https://sit.aces01.nus.edu.sg/cors/jsp/report/'+link[2])

if __name__=="__main__":
  main()