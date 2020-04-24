#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:15:32 2020

@author: kaitlynsimmons
"""

import pandas as pd 
import numpy as np
import zipfile 


#Open up data set for unemployment 

unemploy= 'unemployment-by-county-us.zip'
with zipfile.ZipFile(unemploy, 'r') as zip:
    print(zip.printdir())
    print('Extracting all files')
    zip.extractall()
    print('Done')
    
unemployment= pd.read_csv('output.csv')
print(unemployment)

unemployment= unemployment.sort_values('State')

unemployment_ga = unemployment.loc[unemployment['State']=='Georgia']

unemployment_ga.to_csv('unemploymentforga.csv')

#Somehow GA was left out of the data set so had to find new data set but 
#I wanted to keep the code in here, since it runs if you replace Georgia
#with a state that does exist within the data set 


#Below is the code for the data set that has Georgia in it 


#set up data frame with first spreadsheet
realunemploy= pd.read_excel('laucnty05.xlsx')



# Put all excel files in a list
listy1= ['laucnty06.xlsx', 'laucnty07.xlsx', 'laucnty08.xlsx', 'laucnty09.xlsx', 'laucnty10.xlsx', 'laucnty11.xlsx','laucnty12.xlsx', 'laucnty13.xlsx', 'laucnty14.xlsx', 'laucnty15.xlsx']

#loop through list in order to push them all into one dataset 
for file in listy1:    
    df = pd.read_excel(file)
    dfs = [realunemploy, df]
    realunemploy = pd.concat(dfs)

#extract data only for Georgia by state FIPS code and then write out to CSV     
realunemploy_ga = realunemploy.loc[realunemploy['State FIPS Code']==13]

fips = realunemploy_ga['County FIPS Code']

fips_list = []
for i in fips:
    i_str = str(int(i))
    fips_code = i_str.zfill(3)
    fips_list.append(fips_code)

#make GEOID column
realunemploy_ga['GEOID']= ['13{:03d}'.format(int(n)) for n in fips]
realunemploy_ga.to_csv('realunemployforga.csv')

unemploy_year_list = realunemploy_ga['Year'].unique()


for year in unemploy_year_list:
    df = realunemploy_ga.loc[realunemploy_ga['Year']==year]
    df.to_csv('ga_unemployment_'+str(year)+'.csv')

