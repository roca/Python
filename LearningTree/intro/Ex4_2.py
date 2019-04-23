"""
Exercise 4.2 Lambda and Generator Functions
Ex4_2.py
"""

# Part A
paris_temp = 25
honolulu_temp = 81

def CTOF(C):
    return C * 9.0 / 5.0 + 32

temp_converter = { 
    'ctof': lambda C: CTOF(C) , 
    'ftoc': lambda F: (F - 32) * 5.0 / 9.0
}
print(temp_converter['ctof'](paris_temp))
print(temp_converter['ftoc'](honolulu_temp))



# Part B
def nextid(start):
    resletters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # no I and no O
    resindex = 0
    while True:
        yield(str(start) + resletters[resindex])
        start += 1
        if resindex == len(resletters) - 1:
            resindex = 0
        else:
            resindex += 1


reservation = nextid(99)

for i in range(30):
    print(i,next(reservation))

# Part C   
city_fees_dict = {'HNL': lambda price, tax: price * tax}
price = 200
tax = .10

# Part D
shapelist = ['square', 'rectangle', 'triangle', 'circle']
arealist = [lambda: side ** 2,
            lambda: width * height,
            lambda: width * height / 2,
            lambda: 3.14 * radius ** 2]
side = 3.0
width = 3.0
height = 4.5
radius = 2.5
