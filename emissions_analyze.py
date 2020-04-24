#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:12:35 2020

@author: kaitlynsimmons
"""

import pandas as pd 
import numpy as np

emissions= pd.read_excel('georgia (1).xlsx')

x = emissions.loc[[40]]
years=emissions.loc[[2]]
years = years.values.tolist()
years = years[0]

intyear= []
for y in years :
    if np.isnan(y) == True:
        intyear.append(y)
    else :
        intyear.append(str(int(y)))
    
x.columns = intyear


print(x['2005'])
print(x['2006'])
print(x['2007'])
print(x['2008'])
print(x['2009'])
print(x['2010'])
print(x['2011'])
print(x['2012'])     
print(x['2013'])
print(x['2014'])
print(x['2015'])



