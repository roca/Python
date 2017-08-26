#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print(len(enron_data[enron_data.keys()[0]]))
print("Number of people in dataset: ", len(enron_data.keys()))


sum = 0
for person in enron_data:
    if enron_data[person]["poi"]:
        # print(person)
        sum = sum + 1
print("Number of 'poi': ", sum)

# print(enron_data["PRENTICE JAMES"]["total_stock_value"])
# print(enron_data["COLWELL WESLEY"])
# print(enron_data["SKILLING JEFFREY K"])

# for person in enron_data:
#     if enron_data[person]["poi"]:
#         print(enron_data[person]["exercised_stock_options"])

# )
# print(enron_data["SKILLING JEFFREY K"]["total_payments"])
# print(enron_data["FASTOW ANDREW S"]["total_payments"])
# print(enron_data["LAY KENNETH L"]["total_payments"])
sum = 0
for person in enron_data:
    if enron_data[person]["salary"] != 'NaN':
        sum = sum + 1

sum = 0
for person in enron_data:
    if enron_data[person]["email_address"] != 'NaN':
        sum = sum + 1
print("Number of people that have a 'email_address': ", sum)

sum = 0
for person in enron_data:
    if enron_data[person]["total_payments"] == 'NaN':
        sum = sum + 1
print("Number of people that have 'NaN' for their total payments: ", sum)

t = float(len(enron_data.keys()))
s = float(sum)

print((s/t)*100.)


sum = 0
for person in enron_data:
    if enron_data[person]["poi"] and enron_data[person]["total_payments"] == 'NaN':
        sum = sum + 1
print("Number of 'poi' people that have 'NaN' for their total payments: ", sum)

t = float(len(enron_data.keys()))
s = float(sum)

print((s/t)*100.)