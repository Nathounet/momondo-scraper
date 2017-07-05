class Flight():
    def __init__(self):
        self.cheapest_price = 0
        self.cheapest_duration = None
        self.bestdeal_price = 0
        self.bestdeal_duration = None
        self.departure_date = None
        self.return_date = None

    def __repr__(self):
        return 'Flight '+str(self)

    def __str__(self):
        return 'From '+str(self.departure_date)+' to '+str(self.return_date)+': Cheapest['+str(self.cheapest_price)+';'+str(self.cheapest_duration)+']'+' BestDeal['+str(self.bestdeal_price)+';'+str(self.bestdeal_duration)+']'
