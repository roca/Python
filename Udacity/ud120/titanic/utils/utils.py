#!/usr/bin/python


def convertString(stringData):
    chars = list(stringData[::-1])
    sum = 0
    for i in range(len(chars)):
        sum = sum + (ord(chars[i])*(10**i))
    return sum

def convertArray(array):
    rows = len(array)
    columns = len(array[0])
    for i in range(rows):
        for j in range(columns):
            array[i][j] = convertString(array[i][j])
            # if array[i][j] == '':
            #     array[i][j] = 0.0
            # elif array[i][j] == 'male':
            #     array[i][j] = 0.0
            # elif array[i][j] == 'female':
            #     array[i][j] = 1.0
            # else:
            #     try:
            #         array[i][j] = float(int(array[i][j]))
            #     except:
            #         array[i][j] = float(array[i][j])     
    return array
