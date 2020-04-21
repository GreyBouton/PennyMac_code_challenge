#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
#  Program to output the day number with the smallest temperature spread.
##################################################
# Author: Ian Bouton
# Maintainer: Ian Bouton
# Email: greybouton@gmail.com
##################################################

import pandas as pd

FILE_PATH = 'w_data (5).dat'

with open(FILE_PATH,'r') as raw:
    all_data = raw.readlines()

# generate list of lists with all data
all_data = [i.split() for i in all_data]
# generate another list of only the data needed (first 3 columns needed)
# We have column 1 (day), 2(max temp), 3(min temp)
wthr_needed = [rcrd[:3] for rcrd in all_data if len(rcrd)>3]

# Create dataframe from list of lists in wthr_needed
wthr = pd.DataFrame(wthr_needed[1:], columns = wthr_needed[0])
# Set the index as the "Dy" column
wthr.set_index("Dy",inplace = True)
# extract non-numeric characters and cast columns to int type
for col in wthr.columns:
    wthr[col] = wthr[col].str.extract('(\d+)')
    wthr[col] = wthr[col].astype(int)
    
# Display the day in the month pertaining to the minimu spread in temperatures.
print("The day with the minumum spread in temperature is: Day "\
      + (wthr.MxT-wthr.MnT).idxmin())
high = wthr.loc[(wthr.MxT-wthr.MnT).idxmin()].MxT
low = wthr.loc[(wthr.MxT-wthr.MnT).idxmin()].MnT
print('Max Temp: '+ str(high))
print('Min Temp: '+ str(low))

# OUTPUT
#The day with the minumum spread in temperature is: Day 14
#Max Temp: 61
#Min Temp: 59