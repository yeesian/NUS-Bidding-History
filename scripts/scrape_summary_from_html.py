from bs4 import BeautifulSoup
import os
import re

data_format = 'Module|Group|Quota|No_of_Bidders|Lowest_Bid|Lowest_Succ_Bid|Highest_Bid|Faculty|Student_Type|Bid_Round|Acad_Yr|Semester'

def fetch_entry_from_row(row):
  for td in row.findAll('td'):
    text = td.find(text=True)
    if text == u'\xa0':
      yield '|' # missing info: colspan=2
    else:
      yield text

def fetch_summary_from_html(html):
  soup = BeautifulSoup(html)
  table = soup.findAll('table')
  if len(table) > 1: # some years, they display 2 tables
    table = table[1]
  else: # other years, they display 1
    table = table[0]
  for tr in table.findAll('tr'):
    yield [e for e in fetch_entry_from_row(tr)]

def main():
  folder = 'Bidding_Summary'
  print(data_format)
  for filename in os.listdir(folder):
    f = open(folder + '/' + filename, 'r')
    match = re.match(r'successbid_(\w\w)_(\d+)s(\d).html',filename)
    if match:
      bid_rd,yr,sem = match.group(1), match.group(2), match.group(3)
      for summary in fetch_summary_from_html(f.read()):
        print('|'.join(summary + [bid_rd,yr,sem]))
    f.close()

if __name__ == "__main__":
  main()