#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
sorted_data = sorted(data, key=lambda tuple: tuple[1])

sorted_data = sorted_data[:len(sorted_data)-1]
for point in sorted_data:
    salary = point[0]
    bonus = point[1]
    for key, value in data_dict.items():
        if value['salary'] == salary and value['bonus'] == bonus:
            print "Person ",point,key,value['bonus']
    
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



