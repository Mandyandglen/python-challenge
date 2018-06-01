import pandas as pd
import numpy as np
import os
os.getcwd()
import glob
import datetime
import re

glob.glob('*csv')

budgets = pd.DataFrame()
for f in glob.glob('*csv'):
    df = pd.read_csv(f)
    budgets = budgets.append(df,ignore_index=True)

budgets.info()
budgets['Date'].unique()

print ('Total Revenue: $',sum)

df=df.groupby('Date').nunique()
df.Date.value_counts()
print ('Number of Months: ',df.Date.value_counts())

budgets.Revenue.groupby