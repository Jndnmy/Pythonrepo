# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 22:00:46 2021

@author: Jason
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind',
 'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'],
 'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics',
 'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths',
 'Physics', 'Chemistry'],
 'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70]
 }
## Convert dictionary to a DataFrame

df= pd.DataFrame.from_dict(student_details)
## Create a new column with Marks
## ranked in descending order
#
#df['Mark_Rank'] = df['Marks'].rank(ascending = 0)
## Set index to newly created column and print the df

df['Mark_Rank']= df['Marks'].rank(ascending = 0, method = 'min')
df.set_index('Mark_Rank', inplace=True, drop=True)
df= df.sort_index()
print(df)
## Rank the marks using the following methods: default, max, bottom. Print the df
#df['Mark_Rank']= df['Marks'].rank(method = 'average')

#df['Mark_Rank']= df['Marks'].rank(method = 'max')

#df['Mark_Rank']= df['Marks'].rank(method = 'min')

Array1 = ['Geek1', 'Geek2', 'Geek3', 'Geek4',
 'Geek5', 'Geek6', 'Geek7', 'Geek8']
Array2 = [15, 23, 25, 9, 67, 54, 42, np.NaN]
Array3 = []
for i in range(len(Array1)):
   if Array2[i] > 17:
       Array3.append('yes')
   elif Array2[i] <= 17:
       Array3.append('no')
   else:
       Array3.append('maybe')

voters = {'Voter_name':Array1,'Voter_age':Array2,'Vote':Array3}
df = DataFrame.from_dict(voters)
#print(df)

# df['Vote'] = 'maybe'
# df.loc[df['Voter_age'] >= 18, ['Vote']] = 'yes'
# df.loc[df['Voter_age'] < 18, ['Vote']] = 'no'

