# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Cleaning NUS Bidding Activities
# ---
# (this is a continuation of the instructions (from step 7 onwards) at the [NUS-Bidding-History](https://github.com/yeesian/NUS-Bidding-History) repository)

# <codecell>

import pandas as pd
print('pandas',pd.version.version)

# <codecell>

bid_activity = pd.read_csv('bidding_activity.csv',sep='|')
bid_activity

# <codecell>

print(bid_activity.head())
bid_activity.dtypes

# <codecell>

from datetime import datetime
bid_activity['Time_of_Bid'] = bid_activity['Time_of_Bid'].map(lambda date_str: datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S"))

# <codecell>

print(bid_activity.head())

# <codecell>

for c in ['Bid_Status','Faculty','Student_Type','Account','Bid_Round']:
    print(c,set(bid_activity[c]))

# <codecell>

def summarise(s):
    if s == 'null':
        return 'NA'
    else:
        return s[0]

for c in ['Bid_Status','Student_Type','Account']:
    bid_activity[c] = bid_activity[c].map(summarise)
print(bid_activity.head())

# <codecell>

for c in ['Bid_Status','Faculty','Student_Type','Account','Bid_Round']:
    print(c,set(bid_activity[c]))

# <codecell>

bid_activity.to_csv('nus_bidding_activity.csv',index=False)

# <codecell>


