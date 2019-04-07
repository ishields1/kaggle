# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:45:21 2019

@author: Isaac Shields
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

wd = os.getcwd()
file = wd + '\\titanic\\test.csv'

test = pd.read_csv(file, engine='python')

file = wd + '\\titanic\\train.csv'
train = pd.read_csv(file, engine='python')

print(list(train.columns.values))
print(train.head())
print(train.tail())

# dropping all cols that don't have 'useful' data
# PassengerID tells us nothing
# Cabin has missing data and over lap
# Name might be usable for a Title but I don't think it will be highly impact
#   Might circle back on that idea
# Ticket has lots of missing data
train = train.drop(['PassengerId', 'Cabin', 'Name', 'Ticket'], axis=1)
test = test.drop(['PassengerId', 'Cabin', 'Name', 'Ticket'], axis=1)

# I want to print tables of each categorical variable to see how they effect survival rates
train_cat = train[['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']]
print(train_cat.columns)


for col in train_cat.columns.tolist():
    ave_death = train[['Survived', col]].groupby([col]).mean()
#   ave_death = train[['Survived', 'Sex']]
    print(ave_death)


# TODO histogram of survival based on age

plt.hist(train['Age'], 25, range=[0, 100])


plt.show()