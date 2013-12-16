# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Cleaning NUS Bidding Summary
# ---
# (this is a continuation of the instructions (from step 7 onwards) at the [NUS-Bidding-History](https://github.com/yeesian/NUS-Bidding-History) repository.)
# 
# 
# libraries used:

# <codecell>

import pandas as pd
#print('pandas',pd.version.version)

# <codecell>

bid_summary = pd.read_csv('bidding_summary.csv',sep='|')
#bid_summary # notice how there are missing values in the first 2 columns"

# <codecell>

#print(bid_summary.head())

# <codecell>

bid_summary = bid_summary.fillna(method='pad') # we fill downwards
#bid_summary

# <codecell>

#print(bid_summary.head()) # now, observe the duplicate header rows (eg. row 0)

# <codecell>

bid_summary = bid_summary[bid_summary['Module'] != 'Module'] # filter out [duplicate] headers
#bid_summary

# <codecell>

#print(bid_summary.head())

# <codecell>

#set(bid_summary['Student_Type'])

# the source of a number of problems
# i) "NUS Students [P, G]" has a comma inside
# ii) 'Returning Students [P] and ' was cropped off
# iii) 'Returning Students and ' was also cropped off

# <codecell>

# remove the comma in the field: 'NUS Students [P, G]'
bid_summary.ix[bid_summary.Student_Type == 'NUS Students [P, G]', 'Student_Type'] = 'NUS Students [PG]'
#set(bid_summary['Student_Type']) # doublecheck, so we can save it as comma-separated values later

# <codecell>

bid_summary.ix[bid_summary.Student_Type == 'Returning Students [P] and ', 'Student_Type'] = 'Returning Students [P] and NUS Students [G]'
bid_summary.ix[bid_summary.Student_Type == 'Returning Students and ', 'Student_Type'] = 'Returning Students and New Students [P]'
#set(bid_summary['Student_Type']) # doublecheck

# <codecell>

#set(bid_summary['Acad_Yr']) # some of the years (0405 and 0506) are inconsistent

# <codecell>

bid_summary.ix[bid_summary.Acad_Yr == 405, 'Acad_Yr'] = 20042005
bid_summary.ix[bid_summary.Acad_Yr == 506, 'Acad_Yr'] = 20052006
#set(bid_summary['Acad_Yr']) # some of the years are broken

# <codecell>

#bid_summary.dtypes # let's check the datatype for the rest of the fields

# <codecell>

for header in ['Quota','No_of_Bidders','Lowest_Bid','Lowest_Succ_Bid','Highest_Bid']:
    bid_summary[header] = bid_summary[header].map(int) # convert to Int64
#bid_summary

# <codecell>

#bid_summary.dtypes

# <codecell>

bid_summary.to_csv('nus_bidding_summary.csv',index=False)

# <codecell>

#bid_summary = pd.read_csv('nus_bidding_summary.csv')
#bid_summary # and we're done

