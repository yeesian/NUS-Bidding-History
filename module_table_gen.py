# this file opens the raw data file, generates a table of module names and their id
# and saves them in a another csv file

f = open('data.csv')
i = 1

f.readline()
first_mod = f.readline()

last_mod = first_mod.split(',')[0];

w = open('modules.csv', 'w');
w.write('mod_id,module_name\n')

for line in f:
  arr = line.split(',')
  curr_mod = arr[0]
  if curr_mod != last_mod:
    print ('Saving id ' + str(i) + ': ' + last_mod + '...')
    w.write(str(i) + ',' + last_mod + '\n')
    i+=1
    last_mod = curr_mod

print ('Saving id ' + str(i) + ': ' + last_mod + '...')
w.write(str(i) + ',' + last_mod + '\n')

f.close()
w.close()  

