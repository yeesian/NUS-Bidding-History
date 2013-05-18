import re
import fileinput

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

students = ['New', 'Returning']
accounts = ['Programme', 'General']

def join_words_regex(l):
  return r'\b('+'|'.join(l)+r')\b'

def split_fac_student_acct(line):
  expression = r'(' + join_words_regex(faculties) + r') null'
  match = re.search(expression,line)
  if match:
    return match.group(1),'null','null'
  else:
    expression = r'(' + join_words_regex(faculties) + r').+'
    match = re.search(expression,line)
    if match:
      line = line.strip().split(' ')
      faculty = match.group(1)
      student_type = line[line.index('Students')-1]
      account = line[line.index('from')+1]
      if faculty =='NUS':
        student_type = 'null'
      return match.group(1), student_type, account


def extract_fields_from(line):
  line = line.strip().split(',')
  match = re.search('(.+) \((.+)\)',line[2])
  if match:
    fac, std, acc = split_fac_student_acct(match.group(2))
    line += [match.group(1), fac, std, acc]
    del line[2]
    return ','.join(line)
  else:
    print('failed to match for line: ',line)


def main():
  header = 'Module_Code,Bid_Round,Bid_Amount,Bid_ID,Time_of_Bid,Bid_Status,Class,Faculty,Student_Type,Account'
  for line in fileinput.input():
    if fileinput.lineno() == 1:
      print(header)
    else:
      print(extract_fields_from(line))

if __name__ == "__main__":
  main()