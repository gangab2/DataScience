# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:06:38 2016

@author: gangab2
"""

import pandas as pd
data = ''' Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.split('\n')
#print data

data = [i.split(',') for i in data]
#print data
column_names = data[0] # This is the first row
data_rows = data[1::] # these are all the following rows of data
df =pd.DataFrame(data_rows,columns=column_names)

print df

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print df['Alcohol'].mean()
print df['Tobacco'].mean()
print df['Alcohol'].median()
print df['Tobacco'].median()

max(df['Alcohol']) - min(df['Alcohol'])
print df['Alcohol'].std()
print df['Alcohol'].var()

max(df['Tobacco']) - min(df['Tobacco'])
print df['Tobacco'].std()
print df['Tobacco'].var()
