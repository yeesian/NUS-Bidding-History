import urllib2
from bs4 import BeautifulSoup


def parse_table(year, semester, bid_round):

    outfile = open('output.txt','w')
    url = 'http://www.cors.nus.edu.sg/Archive/200607_Sem1/successbid_3C_20062007s1.html'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    outfile.write(response.read())
    soup.BeautifulSoup(response.read())
    outfile.close()
    response.close()

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

    



