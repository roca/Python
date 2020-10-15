"""
Exercise 4.1 Creating and Calling Functions
Ex4_1.py
"""
# Data for the exercise
# Please do not modify these dictionaries

# Data description of city_code_dict
#    Airport Code : Airport Name

city_code_dict = {
    'HNL': 'Honolulu',
    'ITO': 'Hilo',
    'LHR': 'London/Heathrow',
    'ARN': 'Stockholm/Arlanda',
    'HKG': 'Hong Kong',
    'YYZ': 'Toronto',
    'CDG': 'Paris/Charles de Gaulle',
    'NRT': 'Tokyo/Narita',
    'GCM': 'Grand Cayman BWI',
    'CUR': 'Curacao Netherland Antilles'}

# Data description of flightdict
# flightnum : [ departcity, arrivecity, departtime, departday,
#                arrivetime, arriveday, cost, code ]


flightdict = {
    102: ['HNL', 'HKG', '4:00', 'Monday', '8:00', 'Monday', 99.95, 4],
    132: ['HNL', 'HNL', '4:00', 'Monday', '8:00', 'Monday', 59.0, 2],
    276: ['HKG', 'CDG', '15:00', 'Monday', '3:00', 'Tuesday', 233.99, 2],
    303: ['HKG', 'ARN', '9:00', 'Monday', '16:00', 'Monday', 233.99, 2],
    498: ['NRT', 'ITO', '14:00', 'Monday', '0:00', 'Tuesday', 159.99, 2],
    390: ['CUR', 'CUR', '4:00', 'Thursday', '8:00', 'Thursday', 599.95, 3],
    465: ['NRT', 'YYZ', '4:00', 'Thursday', '8:00', 'Thursday', 59.0, 3],
    1305: ['ITO', 'ARN', '4:00', 'Thursday', '8:00', 'Thursday', 125.0, 2],
    375: ['HKG', 'HNL', '6:00', 'Friday', '11:00', 'Friday', 299.99, 4],
    444: ['NRT', 'LHR', '15:00', 'Friday', '3:00', 'Saturday', 125.0, 3],
    1572: ['HNL', 'HNL', '4:00', 'Sunday', '8:00', 'Sunday', 125.0, 2]}

# Part A
def list_all_cities():
    for k,v in city_code_dict.items():
        print(k,v)
list_all_cities()

# Part B 

searchcity = 'HNL'
searchcity = 'CUR'
searchcity = 'ITO'

departcity = 'NRT'
arrivecity = 'ITO'

def flights_per_city(codelist):
    codes = [flight_code for flight_code in codelist if flight_code in city_code_dict]
    for code in codes:
        print(city_code_dict[code])

flights_per_city([departcity])