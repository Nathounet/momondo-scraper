class Flight():
    def __init__(self):
        self.date_departure = None
        self.date_return = None
        self.date_this_way = None # Points on either date_departure or date_return
        self.date_other_way = None # Points on either date_return or date_departure
        self.cheapest_price = 0
        self.cheapest_duration = None
        self.bestdeal_price = 0
        self.bestdeal_duration = None

    def __repr__(self):
        return 'Flight '+str(self)

    def __str__(self):
        dep_date = self.date_departure.strftime('%d-%m-%Y')
        ret_date = self.date_return.strftime('%d-%m-%Y')
        cheap_pri = str(self.cheapest_price)
        cheap_dur = str(self.cheapest_duration)
        bd_pri = str(self.bestdeal_price)
        bd_dur = str(self.bestdeal_duration)
        return 'From '+dep_date+' to '+ret_date+': Cheapest['+cheap_pri+';'+cheap_dur+']'+' BestDeal['+bd_pri+';'+bd_dur+']'
