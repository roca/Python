"""
Exercise 5.1 Classes and Initialization
Ex5_1.py
"""
# Part A


# Sample data for Trip
depcity = 'CUR'
arrcity = 'HNL'
deptime = '12:00'
depday = 'Sunday'
arrtime = '20:00'
arrday = 'Sunday'

class Trip:
    def __init__(self,
        departcity = 'None',
        arrivecity = 'None',
        departtime = 'None',
        departday = 'None',
        arrivetime = 'None',
        arriveday = 'None',
    ):
        self.departcity = depcity
        self.arrivecity = arrcity
        self.departtime = deptime
        self.departday = depday
        self.arrivetime = arrtime
        self.arriveday = arrday
    cariblist = ['GCM', 'CUR']
    hawaiilist = ['ITO', 'HNL']

    def is_round_trip(self):
        return (self.departcity == self.arrivecity)

mytrip = Trip(departcity=depcity, arrivecity=arrcity, departtime=deptime, departday=depday, arrivetime=arrtime, arriveday=arrday)
print(mytrip.departday)

print(Trip.hawaiilist)
print(Trip.cariblist)
print(mytrip.is_round_trip())


# Part B

alltrips = [Trip(departcity="HNL", arrivecity="ITO", departtime="8:00", departday="Monday",
             arrivetime="14:00", arriveday="Monday"),
            Trip(departcity="HKG", arrivecity="HNL", departtime="6:00", departday="Monday",
             arrivetime="11:00", arriveday="Monday"),
            Trip(departcity="CDG", arrivecity="GCM", departtime="12:00", departday="Monday",
             arrivetime="20:00", arriveday="Monday"),
            Trip(departcity="ARN", arrivecity="CDG", departtime="17:00", departday="Tuesday",
             arrivetime="7:00", arriveday="Wednesday")]

def print_trip(trp):
    print('Trip from', trp.departcity, 'to', trp.arrivecity,
            'Departs at', trp.departtime, 'on', trp.departday,
            'Arrives at', trp.arrivetime, 'on', trp.arriveday, end=' ')



# Part C
# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# citycity is Honolulu
