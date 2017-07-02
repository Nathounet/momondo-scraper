class Flight():
    def __init__(self):
        self.cheapest_price = 0
        self.cheapest_duration = ''
        self.bestdeal_price = 0
        self.bestdeal_duration = ''
        self.departure = None
        self.arival = None

    def __repr__(self):
        return 'Flight '+str(self)

    def __str__(self):
        return 'From '+str(self.departure)+' to '+str(self.arrival)+': Cheapest['+str(self.cheapest_price)+';'+str(self.cheapest_duration)+']'+' BestDeal['+str(self.bestdeal_price)+';'+str(self.bestdeal_duration)+']'
