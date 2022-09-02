# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData

flight_data = FlightData()
my_cities = flight_data.my_data()
print(my_cities)