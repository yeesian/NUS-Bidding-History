##This script helps to flatten all the other indivdual files. 
##Must be placed in the same directory. 

faculty_lookup = {
			'SCHOOL OF BUSINESS': 1,
			'ENGINEERING': 2,
			'SCHOOL OF COMPUTING': 3,
			'JOINT MULTI-DISCIPLINARY PROGRAMMES': 4,
                        'UNIVERSITY SCHOLARS PROGRAMME': 4,
			'NUS': 5,
                        'NON-FACULTY-BASED DEPARTMENTS': 5,
                        'UNIVERSITY ADMINISTRATION': 5,
			'SCIENCE': 6,
			'SCHOOL OF DESIGN AND ENVIRONMENT': 7,
			'ARTS & SOCIAL SCIENCES': 8,
			'YONG LOO LIN SCHOOL OF MEDICINE': 9,
			'YONG SIEW TOH CONSERVATORY OF MUSIC': 10,
                        'LAW': 11,
                        'SAW SWEE HOCK SCHOOL OF PUBLIC HEALTH': 12
			}

#Semester List and Bid Point Generator
def name_generator():
    list_all = []
    for year in ['0809','0910','1011','1112','1213']:
        for bid_round in ['1A','1B','1C','2A','2B','3A','3B']:
            #Semester 1
            list_all.append(year+'S1'+bid_round+'.csv')
        if year == ['0809','0910','1011']:
            for bid_round in ['1A','1B','2A','2B','2C','3A','3B']:
                #Semester 2
                list_all.append(year+'S2'+bid_round+'.csv')
        else:
            for bid_round in ['1A','1B','2A','2B','3A','3B']:
                #Semester 2
                list_all.append(year+'S2'+bid_round+'.csv')

    return list_all

outfile = open('summary.csv','w')
outfile.write('Module,Group,AY,Semester,Round,Quota,No,Lowest,Lowest,Highest,Faculty,Student Type\n')
filelist = name_generator()

for filename in filelist:
    infile = open(filename,'r')
    for row in infile:
        summary = row.split(',')

        #Ignore Header Row
        if summary[0] == 'Module':
            continue

        #Plug in some gaps due to merged rows
        #Example - ACC1002X for Engine, for Science Quota
        #Earlier Parse did not account for some missing values
        if summary [0] == '':
            summary[0] = last_module
            summary[1] = last_lecture
        last_module = summary[0]
        last_lecture = summary[1]

        #Compress Faculty to a number. See above for reference
        summary[7] = str(faculty_lookup[summary[7]])

        #Insert Bidround, then Semester, then Academic Year
        summary.insert(2,filename[6:8])
        summary.insert(2,filename[5:6])
        summary.insert(2,filename[0:4])
               
        outfile.write(','.join(summary))

    print filename + ' done!'
outfile.close()
