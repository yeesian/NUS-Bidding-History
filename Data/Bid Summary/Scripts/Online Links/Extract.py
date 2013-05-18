infile = open("URL Extract.txt",'r')
instring = infile.read()
infile.close()

urls = []
while instring.find('href="') != -1:
    instring = instring[instring.find('href="')+6:]
    urls.append(instring[:instring.find('"')])
    instring = instring[instring.find('"')+1:]

urls.reverse()
outfile = open("URLs to Open.txt",'w')

for item in urls:
    if item[0] == '.':
        outstr = "http://www.cors.nus.edu.sg" + item[1:]
    elif item[0] == '#':
        continue
    else:
        outstr = item
    outfile.write(outstr+'\n')
    
outfile.close()
