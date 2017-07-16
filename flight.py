class Flight():
    def __init__(self):
        self.departure_date = None
        self.return_date = None
        self.cheapest_price = 0
        self.cheapest_duration = None
        self.bestdeal_price = 0
        self.bestdeal_duration = None

    def __repr__(self):
        return 'Flight '+str(self)

    def __str__(self):
        dep_date = self.departure_date.strftime('%d-%m-%Y')
        ret_date = self.return_date.strftime('%d-%m-%Y')
        cheap_pri = str(self.cheapest_price)
        cheap_dur = str(self.cheapest_duration)
        bd_pri = str(self.bestdeal_price)
        bd_dur = str(self.bestdeal_duration)
        return 'From '+dep_date+' to '+ret_date+': Cheapest['+cheap_pri+';'+cheap_dur+']'+' BestDeal['+bd_pri+';'+bd_dur+']'
