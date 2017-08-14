from datetime import datetime
from ConfigParser import ConfigParser

class Config():
    def __init__(self, path_config_file):
            # Get config
            config_file = ConfigParser()
            config_file.read(path_config_file)
            # Get date ranges
            try:
                self.dep_date_min = datetime.strptime(config_file.get('Dates', 'DepartureDate_Min'), '%d-%m-%Y')
                self.dep_date_max = datetime.strptime(config_file.get('Dates', 'DepartureDate_Max'), '%d-%m-%Y')
                if self.dep_date_min > self.dep_date_max:
                    print "ERROR: Departure dates not correct (minimum is after maximum)"
            except:
                print "ERROR: Departure date format is not correct"
            try:
                self.ret_date_min = datetime.strptime(config_file.get('Dates', 'ReturnDate_Min'), '%d-%m-%Y')
                self.ret_date_max = datetime.strptime(config_file.get('Dates', 'ReturnDate_Max'), '%d-%m-%Y')
                if self.ret_date_min > self.ret_date_max:
                    print "ERROR: Return dates not correct (minimum is after maximum)"
            except:
                print "ERROR: Return date format is not correct"
            # Get airports preferences
            self.departure = config_file.get('Airports', 'AirportOfDeparture')
            self.arrival = config_file.get('Airports', 'AirportOfArrival')
            self.nearby = config_file.get('Airports', 'AlsoSearchNearbyAirports')
            self.direct = config_file.get('FlightOptions', 'OnlyDirect')

#TODO: Improve error handling: add exceptions
