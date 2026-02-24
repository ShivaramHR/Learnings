from dateutil import parser

class Workout(object):
    cal_per_hr = 200

    def __init__(self, start, end, calories = None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = '😓'
        self.kind = 'Workout'
    def get_calories(self):
        if (self.calories == None):
            return Workout.cal_per_hr*(self.end - self.start).total_seconds()/3600
        else:
            return self.calories
        
my_workout = Workout('9/30/2021 1:35PM', '9/30/2021 1:57PM', 200)
print(my_workout.__dict__.keys())
print(my_workout.__dict__.values()) 