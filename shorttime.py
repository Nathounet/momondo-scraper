class Time():
    def __init__(self, s):
        # '19h30m (Moyenne)'
        self.hours = int(s.split('h')[0])
        self.minutes = int(s.split('h')[1].split('m')[0])
        self.totalMinutes = self.hours*60 + self.minutes

    def __repr__(self):
        return 'Time '+str(self)

    def __str__(self):
        return '%02d:%02d' % (self.hours, self.minutes)

    def toFloat(self):
        return '%.2f' % (self.hours + (self.minutes * 0.01))
