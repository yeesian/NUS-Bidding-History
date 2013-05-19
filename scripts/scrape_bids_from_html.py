from bs4 import BeautifulSoup
import os
import re

faculties = ['ARTS & SOCIAL SCIENCES',
             'ENGINEERING',
             'JOINT MULTI-DISCIPLINARY PROGRAMMES',
             'NUS',
             'SCHOOL OF BUSINESS',
             'SCHOOL OF COMPUTING',
             'SCHOOL OF DESIGN AND ENVIRONMENT',
             'SCIENCE',
             'YONG LOO LIN SCHOOL OF MEDICINE',
             'YONG SIEW TOH CONSERVATORY OF MUSIC']

data_format = 'Bid_Amount|Bid_ID|Time_of_Bid|Bid_Status|Group|Faculty|Student_Type|Account|Module|Bid_Round|Acad_Yr|Semester'

def extract_faculty_student_account(field):
  expression = r'(\b(' + '|'.join(faculties) + r')\b)'
  match = re.search(expression + ' null',field)
  if match:
    return [match.group(1),'null','null']
  else:
    match = re.search(expression + r'.+',field)
    fields = field.strip().split(' ')
    if match:
      faculty = match.group(1)
      student_type = fields[fields.index('Students')-1]
      account = fields[fields.index('from')+1]
      if faculty == 'NUS':
        student_type = 'null'
      return [faculty, student_type, account]
    return []

def split_header(header):
  match = re.search('(.+) \((.+)\)',header)
  if match:
    class_type, sub_header = match.group(1), match.group(2)
    faculty, student, account = extract_faculty_student_account(sub_header)
    return [class_type, faculty, student, account]
  else:
    return []

def fetch_bid_from_html(html):
  table = BeautifulSoup(html).find(class_='tableframe')
  entries = table.find_all('td')
  header = split_header(entries[5].text.strip())
  entries = entries[6:] # discard header(s)
  if entries:
    bid = []
    i = 0
    while i < len(entries):
      if entries[i].attrs.get('colspan') == '4':
        header = split_header(entries[i].text.strip())
        i += 1
      else:
        yield [e.text.strip() for e in entries[i:i+4]] + header
        i += 4

def main():
  folder = 'Bidding_Activity'
  print(data_format)
  print
  for filename in os.listdir(folder):
    match = re.match(r'.+MOD_C=(.+)&ROUND_N=(.+)',filename)
    if match:
      f = open(folder + '/' + filename,'r')
      module, bid_round = match.group(1), match.group(2)
      for bid in fetch_bid_from_html(f.read()):
        print('|'.join(bid+[module, bid_round, '20122013', '2']))
      f.close()

if __name__ == "__main__":
  main()