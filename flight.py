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
        return 'From '+self.departure_date.strftime('%d-%m-%Y')+' to '+self.return_date.strftime('%d-%m-%Y')+': Cheapest['+str(self.cheapest_price)+';'+self.cheapest_duration.strftime('%H:%M')+']'+' BestDeal['+str(self.bestdeal_price)+';'+self.bestdeal_duration.strftime('%H:%M')+']'
