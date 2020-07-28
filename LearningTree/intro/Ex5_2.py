"""
Exercise 5.2 Inheritance
Ex5_2.py
"""


# Part A

class Trip:
    def __init__(self, departcity=None, arrivecity=None,
                 departtime=None, departday=None,
                 arrivetime=None, arriveday=None):
        self.departcity = departcity
        self.arrivecity = arrivecity
        self.departtime = departtime
        self.departday = departday
        self.arrivetime = arrivetime
        self.arriveday = arriveday

    cariblist = ['CUR', 'GCM']
    hawaiilist = ['HNL', 'ITO']

    def is_round_trip(self):
        return self.arrivecity == self.departcity

    def is_caribbean(self):
        return self.arrivecity in Trip.cariblist

    def is_hawaiian(self):
        return self.arrivecity in Trip.hawaiilist

    def is_over_night(self):
        return self.arriveday != self.departday

    def is_interisland(self):
        return self.arrivecity in Trip.hawaiilist and self.departcity in Trip.hawaiilist


# Part B
# Add the subclass below
class Flight(Trip):
    def __init__(self,flightnum=-1,
                 departcity=None, arrivecity=None,
                 departtime=None, departday=None,
                 arrivetime=None, arriveday=None,cost=0.0,code=0):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        super().__init__(departcity = departcity, arrivecity = arrivecity, departtime = departtime, departday = departday, arrivetime = arrivetime, arriveday = arriveday)
    
    def discount(self):
            if Trip.is_interisland(self):
                return self.cost * .95
            if Trip.is_hawaiian(self):
                return self.cost * .90
            if Trip.is_caribbean(self):
                return self.cost * .85


# Part C
flight1 = Flight(flightnum=102, departcity="HNL", arrivecity="HKG",
                departtime="4:00",departday="Monday", arrivetime="8:00",
                arriveday="Monday", cost=99.95, code=4)
flight2 = Flight(flightnum=204, departcity="HNL", arrivecity="ITO",
                departtime="8:00", departday="Monday", arrivetime="14:00",
                arriveday="Monday", cost=199.99, code=42)
flight3 = Flight(flightnum=336, departcity="HKG", arrivecity="GCM",
                departtime="12:00", departday="Monday", arrivetime="20:00",
                arriveday="Monday", cost=299.99, code=44)
flight4 = Flight(flightnum=660, departcity="CDG", arrivecity="GCM",
                departtime="14:00", departday="Monday", arrivetime="0:00",
                arriveday="Tuesday", cost=199.99, code=42)
flight5 = Flight(flightnum=681, departcity="CDG", arrivecity="ITO",
                departtime="6:00", departday="Monday", arrivetime="11:00",
                arriveday="Monday", cost=209.89, code=41)
flight6 = Flight(flightnum=753, departcity="LHR", arrivecity="HKG",
                departtime="10:00", departday="Monday", arrivetime="18:00",
                arriveday="Monday", cost=199.99, code=42)

flightlist = [flight1, flight2, flight3, flight4, flight5, flight6]

for flight in flightlist:
    print(flight.cost,flight.discount())

# Part D
#
# cruiselist = [Cruise(cruisenum=201, departcity="HNL", arrivecity="ITO",
#                 departtime="08:00", departday="Monday",arrivetime="23:00",
#                 arriveday="Monday", cost=199.99, code="I"),
#              Cruise(cruisenum=202, departcity="HNL", arrivecity="ITO",
#                 departtime="05:00", departday="Sunday", arrivetime="21:30",
#                 arriveday="Sunday", cost=99.99, code="O"),
#              Cruise(cruisenum=206, departcity="HNL", arrivecity="ITO",
#                 departtime="06:00", departday="Tuesday", arrivetime="22:00",
#                 arriveday="Tuesday", cost=199.99, code="I"),
#              Cruise(cruisenum=208, departcity="HNL", arrivecity="ITO",
#                 departtime="16:00", departday="Thursday", arrivetime="08:00",
#                 arriveday="Friday", cost=299.99, code="I"),
#              Cruise(cruisenum=210, departcity="HNL", arrivecity="ITO",
#                 departtime="15:00", departday="Friday", arrivetime="09:00",
#                 arriveday="Saturday", cost=299.99, code="O")]

# Part E
name1 = "Pat Holder"
name2 = "Peter Smith"
name3 = "Guy Gildersleeve"
name4 = "Janet Rider"
name5 = "Lynn Jasper"
name6 = "Ian Rouselle"
