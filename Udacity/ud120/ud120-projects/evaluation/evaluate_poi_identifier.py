#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
#sort_keys = '../tools/python2_lesson14_keys.pkl'



### your code goes here 
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
from time import time

clf = tree.DecisionTreeClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
predicted = clf.predict(features_test) 
print "prediction time:", round(time()-t1, 3), "s"
print "predicted ", predicted
print "actual: ", labels_test

x = []
x[:len(features_test)] = [0] * len(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(predicted, labels_test)

print(accuracy)

for index, item in enumerate(predicted):
    if item == features_test[index]:
        print "y"



