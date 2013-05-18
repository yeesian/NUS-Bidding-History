# usage: python scrape_module_links.py [url] >

# url: 'https://sit.aces01.nus.edu.sg/cors/jsp/report/GlobalBidHistDetails.jsp'
# prints all links to module_bidding_history pages in the url above to stdout

# 

from lxml.html import iterlinks
from bs4 import BeautifulSoup
import urllib3
import re
import sys
http = urllib3.PoolManager()

unsuccessful_queue = []

def iter_find_module_round(url):
  r = http.request('GET', url)
  for link in iterlinks(r.data):
    if link[2][:6] == 'Global': # a quick hack, to match the head of the string
      match = re.search('MOD_C=(\w+)&ROUND_N=(\w+)',link[2])
      if match:
        yield match.group(1), match.group(2)

def fetch_bid_from_url(url):
  r = http.request('GET', url)
  if r.status != 200:
    print("Unsuccessful http quest for " + url)
    unsuccessful_queue.append(url)
  else:
    html = BeautifulSoup(r.data).find_all(class_="tableframe")
    if len(html) > 1: # the table may not be unique
      print("The code may be faulty for " + url)
      unsuccessful_queue.append(url)
    else:
      entries = html[0].find_all("td")
      student_type = 'Student Type'
      length = 0
      bid = [student_type] + [entry.text.strip()
                              for entry in entries[1:5]] # header row
      for entry in entries[5:]: #discard header
        if entry.attrs.get('colspan') == '4': # new batch/type of students
          if length > 0:
            length = 0
            yield bid
          student_type = entry.text.strip()
          bid = []
        elif length == 4:
          length = 1
          yield bid
          bid = [student_type]
        else:
          length += 1
        bid.append(entry.text.strip())
      if length == 4: # last entry may sometimes be left out
        yield bid
      
def main():
  url = 'https://sit.aces01.nus.edu.sg/cors/jsp/report/GlobalBidHistDetails.jsp'
  print('Module_Code,Bid_Round,Student,Bid_Amount,Bid_ID,Time_of_Bid,Bid_Status')
  for mod,rd in iter_find_module_round(url):
    query = '?MOD_C={0}&ROUND_N={1}'.format(mod,rd)
    fetch_bid_from_url(url+query) # discard headers
    for bid in fetch_bid_from_url(url+query):
      print(','.join([mod,rd]+bid))
  if len(unsuccessful_queue) > 0:
    print("Unsuccessful:")
    print(unsuccessful_queue)

if __name__=="__main__":
  main()