#!/usr/bin/python

# From: https://www.kaggle.com/sinakhorami/titanic-best-working-classifier
# To Colab: https://colab.research.google.com/drive/1KyyXbKL766PKfZqJXFhMJ9bB5AK7Wv9J

import numpy as np
import pandas as pd
import re as re


train = pd.read_csv('./train.csv', header = 0, dtype={'Age': np.float64})
test  = pd.read_csv('./test.csv' , header = 0, dtype={'Age': np.float64})
full_data = [train, test]

line_break = "----------------------------------"

print (train.info())
print (line_break)

print (train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean())
print (line_break)


print (train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean())
print (line_break)

for dataset in full_data:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
print (train[['FamilySize', 'Survived']].groupby(['FamilySize'], as_index=False).mean())
print (line_break)