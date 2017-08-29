#!/usr/bin/python


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
        error = 100.0 * math.abs((net_worths[index] - predictions[index])) / net_worths[index]
        print 'Ages, NetWorthActual NetWorthPredicted Error: ', index, ages[index], ",", net_worths[index], ",", predictions[index], ",", error
        cleaned_data.append((ages[index], net_worths[index], error))

    ### your code goes here

    
    return cleaned_data

