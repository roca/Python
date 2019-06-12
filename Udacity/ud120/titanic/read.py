#!/usr/bin/python

# Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
# survival Survival (0 = No; 1 = Yes)
# name Name
# sex Sex
# age Age
# sibsp Number of Siblings/Spouses Aboard
# parch Number of Parents/Children Aboard
# ticket Ticket Number
# fare Passenger Fare (British pound)
# cabin Cabin
# embarked Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
# boat Lifeboat
# body Body Identification Number
# home.dest Home/Destination

import csv
import numpy as np
import sys
sys.path.append("./utils/")

from time import time
from utils import convertString, convertArray

with open('train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    people = list(csv_reader)
    columns_headers = people[0]
    people = np.array(people[1:])

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 0,1,2,3,4,5,6,7,8,9,10,11

features = ['Pclass','Sex','Age','Cabin']
feature_indices = []
for feature in features:
    feature_indices.append(columns_headers.index(feature))

feature_data = people[:,feature_indices]
print feature_data[0]

feature_data =  convertArray(feature_data)



labels = ['Survived']
label_indices = []
for label in labels:
    label_indices.append(columns_headers.index(label))

label_data = people[:,label_indices]
print label_data[0]

label_data =  convertArray(label_data)



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