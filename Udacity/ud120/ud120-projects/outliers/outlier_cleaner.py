#!/usr/bin/python

import math 


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    for index in range(len(ages)):
        error = math.pow((net_worths[index] - predictions[index]), 2.0)
        #print 'Ages, NetWorthActual NetWorthPredicted Error: ', index, ages[index], ",", net_worths[index], ",", predictions[index], ",", error
        cleaned_data.append((ages[index], net_worths[index], error))

    ### your code goes here
    sorted_cleaned_data = sorted(cleaned_data, key=lambda tuple: tuple[2], reverse = True)

    ten_percent = int(len(sorted_cleaned_data) * .10)

    print "Removing ten_percent of records: ", ten_percent , " out of ", len(sorted_cleaned_data)

    slice_sorted_cleaned_data = sorted_cleaned_data[ten_percent:]

    print "New record count: ", len(slice_sorted_cleaned_data)

    
    return slice_sorted_cleaned_data

