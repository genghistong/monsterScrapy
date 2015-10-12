# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:36:23 2015

@author: Jonny
"""

import os
import pandas
import re

path = "C:\\Users\\Jonny\\monster"
os.chdir(path)

data = pandas.read_csv('technologyList.csv')
data['Technology'] = data['Technology'].str.lower()

test = ['Tableau  aaaa Qlikview yyy Microsoft SQL Server Qlikview', 'Qlikview adsfasd SAS']

variable = "Qlikview"

#this one works
blank = []
for y in test:
    y = y.lower()
    y = y.split()
    res = [x for x in y if variable.lower() in x]
    #res = re.match(variable, str(y)
    blank.append(res)
print blank
#output is [['qlikview', 'qlikview'], ['qlikview']]
    
#this one doesn't work
blank = []
for y in test:
    y = y.lower()
    y = y.split()
    for z in data['Technology']:
        res = [x for x in y if z in x]
        blank.append(res)

#now this is outputting in an incorrect format
blank = []
for y in test:
    y = y.lower()
    y = y.split()
    for z in data['Technology']:
        if z in y:
            blank.append(z)

#output looks like:
#['tableau', 'qlikview', 'microsoft', 'qlikview', 'sas', 'sas', 'sas']

blank = [[]] * len(test)
i = 0
for y in test:
    y = y.lower()
    y = y.split()
    for z in data['Technology']:
        if z in y:
            blank[i].append(z)
    i +=1

blank = []
for y in test:
    y = y.lower()
    y = y.split()
    res = [x for x in y if variable.lower() in x]
    #res = re.match(variable, str(y)
    blank.extend(res)
print blank



technology = data['Technology'].values.tolist()
[[word for word in string.split() if word in technology] for string in test]

blank = []
for y in test:
    y = y.lower()
    y = y.split()
    for z in technology:
        res = [x for x in y if z in x]
        blank.append(res)

import csv

with open('technologyList.csv', 'rb') as f:
    reader = csv.reader(f)
    technology = list(reader)