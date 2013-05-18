import urllib2
from bs4 import BeautifulSoup


def parse_table(year, semester, bid_round):

    year_next = year + 1
    if year < 10: year = '0' + str(year)
    else: year = str(year)
    if year_next < 10: year_next = '0' + str(year_next)
    else: year_next = str(year_next)
        
    url = 'http://www.cors.nus.edu.sg/Archive/20'
    url += year + year_next + '_Sem' + str(semester)
    url += '/successbid_' + bid_round + '_20' + year + '20'
    url += year_next + 's' + str(semester) + '.html'
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    soup = BeautifulSoup(response.read())
    response.close()

    outfile_name = year + year_next + 'S' + str(semester)
    outfile_name += bid_round + '.csv'

    outfile = open(outfile_name,'w')
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
            outfile.write(outstring[0:len(outstring)-1]+'\n')
    outfile.close()


#Semester 1 
for year in range(9,13):
    for bid_round in ['1A','1B','1C','2A','2B','3A','3B']:
        parse_table(year,1,bid_round)
        print '0' + str(year) + '0' + str(year+1) + ' S1 Round ' + bid_round + ' done!'

#Semester 2
for year in range(9,12):
    for bid_round in ['1A','1B','2A','2B','2C', '3A','3B']:
        if (year == 11) and bid_round == '2C':
            continue
        parse_table(year,2,bid_round)
        print '0' + str(year) + '0' + str(year+1) + ' S2 Round ' + bid_round + ' done!'
