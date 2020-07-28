"""
Exercise 7.1 Exceptions
Ex7_1.py
"""


def print_ftoc(temps):
    for temp in temps:
        try:
            ctemp = (float(temp) - 32) * 5.0 / 9.0
            print('Farenheit temperature {0} is Celsius {1:.2f}'.format(temp, ctemp))
        except:
            print("Variable temp value is not numeric")


temps1 = ['123.0', '34.0', '5', '85']
temps2 = ['123.0', '34.0', 'five', '85',None,34]
temps3 = []

# print_ftoc(temps1)
print_ftoc(temps2)
