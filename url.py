import ConfigParser

class URL():
    def __init__(self, path_to_config):
        config_file = ConfigParser.ConfigParser()
        config_file.read(path_to_config)
        self.test = config_file.get('Airports', 'AirportOfDeparture')
        print self.test
        # Fixed
        self.TripType = '&TripType=2'
        self.SegNo = '&SegNo=2'
        self.AD = '&AD=1'
        self.TK = '&TK=ECO'
        self.NA = '&NA=false'
        
        # Changeable
        self.SO0 = '&SO0='
        self.SD0 = '&SD0='
        self.SDP0 = '&SDP0='
        self.SO1 = '&SO1='
        self.SD1 = '&SD1='
        self.SDP1 = '&SDP1='
        self.DO = '&DO='
        
        ## Get config
        #self.SO0 += departure
        #self.SD0 += arrival
        #self.SO1 += arrival
        #self.SD1 += departure
        #self.DO += direct

    def __repr__(self):
        return 'URL '+str(self)

    def __str__(self):
        return self.getFullUrl()
        
    def ConfigSectionMap(section):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    def setDates(self, dep_date, ret_date):
        print str(dep_date), '>', str(ret_date)
        self.SDP0 = '&SDP0=' + str(dep_date)
        self.SDP1 = '&SDP1=' + str(ret_date)
        
    def getFullUrl(self):
        url = 'https://www.momondo.fr/flightsearch?Search=true'
        url += self.TripType + self.SegNo + self.SO0 + self.SD0 + self.SDP0 + self.SO1 + self.SD1 + self.SDP1 + self.AD + self.TK + self.DO + self.NA
        return url
