# this file cleans up the raw data and compresses them by:
# a. converting the module names into their respective ids
# b. reducing string values to single character shortforms
# c. converting the faculty name into their respective ids

# requires:
# 1. data.csv
# 2. modules.csv

faculty_lookup = {
			'SCHOOL OF BUSINESS': 1,
			'ENGINEERING': 2,
			'SCHOOL OF COMPUTING': 3,
			'JOINT MULTI-DISCIPLINARY PROGRAMMES': 4,
			'NUS': 5,
			'SCIENCE': 6,
			'SCHOOL OF DESIGN AND ENVIRONMENT': 7,
			'ARTS & SOCIAL SCIENCES': 8,
			'YONG LOO LIN SCHOOL OF MEDICINE': 9,
			'YONG SIEW TOH CONSERVATORY OF MUSIC': 10
			}

# create lookup dictionary for modules and their ids

modules_file = open('modules.csv');
modules_file.readline()
modules_lookup = {}

for line in modules_file:
	arr = line.split(',')
	modules_lookup[arr[1].replace('\n', '')] = arr[0]

modules_file.close()

data_file = open('ay1213sem2_bidding_history.csv')

# start writing to compressed data file

compressed_data_file = open('compressed_data.csv', 'w')
compressed_data_file.write(data_file.readline())

for line in data_file:
	arr = line.split(',')
	# module code
	arr[0] = modules_lookup[arr[0]]
	# success
	if arr[5] == 'Successful':
		arr[5] = 'S'
	elif arr[5] == 'Unsuccessful':
		arr[5] = 'U'
	# Class/Faculty
	arr[7] = str(faculty_lookup[arr[7]])
	# Student Type
	if arr[8] == 'New':
		arr[8] = 'N'
	elif arr[8] == 'Returning':
		arr[8] = 'R'
	# Account
	if 'Programme' in arr[9]:
		arr[9] = 'P\n'
	elif 'General' in arr[9]:
		arr[9] = 'G\n'
	compressed_data_file.write(",".join(arr))

compressed_data_file.close()
data_file.close()