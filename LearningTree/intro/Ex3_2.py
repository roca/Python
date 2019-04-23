"""
Exercise 3.2 Dictionaries, Sets, and Looping
Ex3_2.py
"""

# Part A
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

# for key in city_code_dict.keys():
#     print(key)
# for v in city_code_dict.values():
#     print(v)
# for k,v in city_code_dict.items():
#     print(k,v)

# Part B
codelist = ['HNL', 'ITO', 'LHR', 'LGA', 'GCM', 'MSY']
flightlist = ['HNL', 'HKG', '4:00', 'Monday', '8:00', 'Monday', '99.95', 4]

codes = [flight_code for flight_code in codelist if flight_code in city_code_dict]
for code in codes:
    print(id(code))
    print(city_code_dict[code])

# Part C
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



# Part D
airports = (
    "HNL,Honolulu",
    "LHR,London/Heathrow",
    "ARN,Stockholm/Arlanda",
    "HKG,Hong Kong",
    "GCM,Grand Cayman BWI")
