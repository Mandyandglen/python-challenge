import pandas as pd
import numpy as np
import os
os.getcwd()
import glob
from datetime import datetime


glob.glob('*csv')

all_data = pd.DataFrame()
for f in glob.glob('*csv'):
    df = pd.read_csv(f)
    all_data = all_data.append(df,ignore_index=True)

    us_state_abbrev=dict()
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

all_data[['Name','Lastname']] = all_data.Name.str.split(' ',expand=True)

all_data['DOB2']=""

def SecSSN(row):
    last4 = row[-4:-1]
    return "***-**-" + last4
all_data['MaskedSSN']=all_data['SSN'].map(SecSSN)
all_data['StateAbb'] = all_data.State.map(us_state_abbrev)

for index, row in all_data.iterrows():
    
    
    Original_DOB=datetime.strptime(row[2],'%Y-%m-%d')
    new_DOB=Original_DOB.strftime('%m/%d/%Y')
    
    
    all_data.at[index,'DOB2']= new_DOB

    ordered=['Emp ID', 'Name','Lastname','DOB2', 'MaskedSSN', 'StateAbb']
all_data2=all_data.reindex(columns=ordered)

print (all_data2)





