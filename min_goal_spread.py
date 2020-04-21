#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# Program to output the team name with the smallest spread of 
# goals scored by and against the team.

# NOTE - My assumption is that a negative spread is valid for reporting purposes
##################################################
# Author: Ian Bouton
# Maintainer: Ian Bouton
# Email: greybouton@gmail.com
##################################################

import pandas as pd
import re

FILE_PATH = 'soccer.dat'

with open(FILE_PATH,'r') as raw:
    all_data = raw.readlines()

# generate list of lists with all data
all_data = [i.split() for i in all_data]


# generate another list of only the needed records 
rcrds_needed = [rcrd for rcrd in all_data if len(rcrd)>=8]

# apply filter to remove elements from each record having non alphanumeric 
# characters with the exception of '_'
normalized_rcrds =\
[[item for item in rcrd if re.match('^[\w_]+$', item)] for rcrd in rcrds_needed]

# Create dataframe from list of lists in normalized_rcrds
soccer = pd.DataFrame(normalized_rcrds[1:], columns = normalized_rcrds[0])[["Team","F","A"]]

# Set the index as the "Team" column
soccer.set_index("Team",inplace = True)

# cast columns to int type
for col in soccer.columns:
    soccer[col] = soccer[col].astype(int)
    
# Display the Team with the minimum spread in "for" and "against" points.
print("The team with the minumum spread in 'for' and 'against' points is: "\
      + (soccer.F-soccer.A).idxmin())
f = soccer.loc[(soccer.F-soccer.A).idxmin()].F
a = soccer.loc[(soccer.F-soccer.A).idxmin()].A
print('For: '+ str(f))
print('Against: '+ str(a))
print('Spread: ' +str(f-a))

# OUTPUT
#The team with the minumum spread in 'for' and 'against' points is: Leicester
#For: 30
#Against: 64
#Spread: -34
