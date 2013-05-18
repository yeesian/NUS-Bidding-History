from bs4 import BeautifulSoup

infile = open('test.txt','r')
soup = BeautifulSoup(infile.read())
infile.close()

table = soup.findAll('table')



rows = table[1].findAll('tr')
for tr in rows:
        cols = tr.findAll('td')
        outstring = ''
        for td in cols:
                text = td.find(text=True)
                if text == u'\xa0':
                    text = ','
                ##text = text.encode('utf-8')
                outstring += text + ','
        print outstring[0:len(outstring)-1]+'\n'

