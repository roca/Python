#!/usr/bin/python 

def featureScaling(arr):
    
    scale = 1.0
    if len(arr) >= 3:
        try:
            scale = (float(arr[1]) - float(arr[0])) / (float(arr[2]) - float(arr[0]))
        except divide-by-zero:
            print "divide-by-zero"
        
    return scale

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
