from bs4 import BeautifulSoup

infile = open('C:\Documents and Settings\Toh Weiqing\Desktop\CORSInfo\output.txt','r')
soup = BeautifulSoup(infile.read())
infile.close()

outfile = open('abc.csv.','w')
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
	cols = tr.findAll('td')
	outstring = ''
	for td in cols:
		text = td.find(text=True)
		outstring += text + ','
	outfile.write(outstring[0:len(outstring)-1]+'\n')
outfile.close()
