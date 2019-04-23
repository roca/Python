#!/usr/local/bin/python

codes = {'France': 33, 'Japan': 81,'GreatBritain': 44, 'USA': 1}
caps = {'France': 'Paris', 'Cuba': 'Havana','Japan': 'Tokyo'}
countries = []
for code in codes:
    if code in caps:
        countries.append(code)
        print(id(countries))
print(countries)