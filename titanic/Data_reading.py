# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:45:21 2019

@author: Isaac Shields
"""

import pandas as pd
import os


wd = os.getcwd()
file = wd + '\\test.csv'

test = pd.read_csv(file, engine='python')

file = wd + '\\train.csv'
train = pd.read_csv(file, engine='python')

print(list(train.columns.values))


ave_death = train.groupby(by=['Sex', 'Survived']).sum()
print(ave_death)



