import pandas as pd
import numpy as np
import os
os.getcwd()
import glob
import datetime

glob.glob('*csv')

votersdf = pd.DataFrame()
for f in glob.glob('*csv'):
    df = pd.read_csv(f)
    votersdf = votersdf.append(df,ignore_index=True)


Total_votes = votersdf['Voter ID'].count()
Candidate_votes=votersdf.groupby(['Candidate']).count()
percentage_votes =(Candidate_votes.div(Total_votes, level='Total_votes') * 100)

df2=Candidate_votes
df3=percentage_votes

ordered=['Voter ID']
df2=df2.reindex(columns=ordered)
df2=df2.rename(columns = {'Voter ID':'Vote Count'})

ordered=['Voter ID']
df3=df3.reindex(columns=ordered)
df3=df3.rename(columns = {'Voter ID':'Percentage'})


df4 = pd.concat([df2, df3], axis=1, join='inner')
Winner = df2.loc[df2['Vote Count'].idxmax()]

print ('')
print ('Election Results')
print ('----------------------------------------')
print ('Total Votes: ',Total_votes)
print ('----------------------------------------')
print (df4)
print ('----------------------------------------')
print ('')
print ('Winner:') 
print (Winner)
print ('')
print ('----------------------------------------')


