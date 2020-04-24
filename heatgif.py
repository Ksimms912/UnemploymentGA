#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:41:35 2020

@author: kaitlynsimmons
"""

import pandas as pd 
import glob
import imageio

df= pd.read_csv('realunemployforga.csv')

#had to get lowest and highest unemployment rate to make legend for heatmap on GIS
highestrate = df.loc[df['Unemployment Rate (%)'].idxmax()]
print(highestrate)

lowestrate = df.loc[df['Unemployment Rate (%)'].idxmin()]
print(lowestrate)

#credit to superfluoussextant.com and stackoverflow for instructions on making this script


filenames = glob.glob('*.png')
list.sort(filenames, key=lambda x: int(x.split('_' )[1].split('.png')[0]))

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('readableheatmap.gif',images, duration=.75)
