#!/usr/bin/python

import csv
import numpy as np
from time import time


def convertArray(array):
    rows = len(array)
    columns = len(array[0])
    for i in range(rows):
        for j in range(columns):
            if array[i][j] == '':
                array[i][j] = 0.0
            elif array[i][j] == 'male':
                array[i][j] = 0.0
            elif array[i][j] == 'female':
                array[i][j] = 1.0
            else:
                try:
                    array[i][j] = float(int(array[i][j]))
                except:
                    array[i][j] = float(array[i][j])     
    return array

with open('train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    people = list(csv_reader)
    columns_headers = people[0]
    people = np.array(people[1:])

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 0,1,2,3,4,5,6,7,8,9,10,11

features = ['Sex','Age','SibSp','Parch']
feature_indices = []
for feature in features:
    feature_indices.append(columns_headers.index(feature))

feature_data = people[:,feature_indices]

feature_data =  convertArray(feature_data)


print feature_data

labels = ['Survived']
label_indices = []
for label in labels:
    label_indices.append(columns_headers.index(label))

label_data = people[:,label_indices]

label_data =  convertArray(label_data)

print label_data


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(feature_data, label_data, test_size=0.3, random_state=42)


from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
predicted = clf.predict(features_test) 
print "prediction time:", round(time()-t1, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(predicted, labels_test)

print(accuracy)