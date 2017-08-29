#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    for index in range(len(ages)):
       print 'Ages, NetWorth: ', index, ages[index], ",", net_worths[index]
    
    cleaned_data = []

    ### your code goes here

    
    return cleaned_data

