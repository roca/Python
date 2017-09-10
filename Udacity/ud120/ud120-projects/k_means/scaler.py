#!/usr/bin/python 

def featureScaling(arr):
    
    arr_sorted = sorted(arr)
    scaled_arr = []

    for  i in range(len(arr_sorted)):
        scale = 1.0
        if len(arr) >= 3:
            try:
                scale = (float(arr[i]) - float(arr[0])) / (float(arr[len(arr_sorted) - 1]) - float(arr[0]))
            except ZeroDivisionError:
                print "ZeroDivisionError"
        scaled_arr.append(scale)
    return  scaled_arr

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
data_salary = [477,200000,1111258]
data_exercised_stock_options = [3285,1000000,4348384]
# print featureScaling(data)
print featureScaling(data_salary)
print featureScaling(data_exercised_stock_options)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
print(scaler.fit_transform([[477.0],[200000.0],[1111258.0]]))
print(scaler.fit_transform([[3285.0],[1000000.0],[34348384.0]]))
