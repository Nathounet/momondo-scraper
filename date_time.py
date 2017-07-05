class Time():
    def __init__(self, s):
        # '19h30m (Moyenne)'
        l = s.strip('m (Moyenne)').split('h')
        self.hours = int(l[0])
        self.minutes = int(l[1])
        self.totalMinutes = self.hours*60 + self.minutes

    def __repr__(self):
        return 'Time '+str(self)

    def __str__(self):
        return "%02dh%02dm" % (self.hours, self.minutes)

class Date():
    def __init__(self, s):
        l = s.split('-')
        self.day = int(l[0])
        self.month = int(l[1])
        self.year = int(l[2])

    def __repr__(self):
        return 'Date '+str(self)

    def __str__(self):
        return "%02d-%02d-%02d" % (self.day, self.month, self.year)

    def incDay(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            if self.day == 31:
                self.incMonth()
                self.day = 1
            else:
                self.day += 1
        elif self.month == 2:
            if self.day == 28:
                self.incMonth()
                self.day = 1
            else:
                self.day += 1
        else:
            if self.day == 30:
                self.incMonth()
                self.day = 1
            else:
                self.day += 1

    def incMonth(self):
        if self.month == 12:
            self.year += 1
            self.month = 1
        else:
            self.month += 1

    def exceeds(self, d):
        if (self.day > d.day) and (self.month == d.month) and (self.year == d.year):
            return True
        elif (self.month > d.month) and (self.year == d.year):
            return True
        elif (self.year > d.year):
            return True
        else:
            return False
