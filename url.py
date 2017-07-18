class URL():
    def __init__(self, config_parameters):
        # Fixed
        self.TripType = '&TripType=2'
        self.SegNo = '&SegNo=2'
        self.AD = '&AD=1'
        self.TK = '&TK=ECO'

        # Set config
        self.SO0 = '&SO0=' + config_parameters.departure
        self.SD0 = '&SD0=' + config_parameters.arrival
        self.SO1 = '&SO1=' + config_parameters.arrival
        self.SD1 = '&SD1=' + config_parameters.departure
        self.DO = '&DO=' + config_parameters.direct
        self.NA = '&NA=' + config_parameters.nearby

        # Will be set later
        self.SDP0 = '&SDP0=' + config_parameters.dep_date_min.strftime('%d-%m-%Y')
        self.SDP1 = '&SDP1=' + config_parameters.ret_date_max.strftime('%d-%m-%Y')

    def __repr__(self):
        return 'URL '+str(self)

    def __str__(self):
        return self.getFullUrl()

    def setDates(self, dep_date, ret_date):
        print '%s > %s' % (dep_date, ret_date)
        self.SDP0 = '&SDP0=' + dep_date
        self.SDP1 = '&SDP1=' + ret_date

    def getFullUrl(self):
        url = 'https://www.momondo.fr/flightsearch?Search=true'
        url += self.TripType + self.SegNo + self.SO0 + self.SD0 + self.SDP0 + self.SO1 + self.SD1 + self.SDP1 + self.AD + self.TK + self.DO + self.NA
        return url

#TODO: Add every search parameter (1 way, 2 ways, multi-destination with only 2 segments)
#TODO: Add custum number of segments
