import requests

API = "https://api.sheety.co/f4caf79cbf9296ce0534a3fd80edc5fc/flightDeals/prices"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.get_details = requests.get(API).json()

    def my_data(self):
        data = self.get_details["prices"]
        return data
