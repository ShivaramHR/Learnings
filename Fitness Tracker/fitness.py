from dateutil import parser
from gps_helper import gpsDistance

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
            return f"{self.calories:.1f}"
    def get_duration(self):
        return self.end - self.start
    def __str__(self):
        """Return a text-based graphical depiction of the workout"""
        width = 16
        retstr = f"|{'–' * width}|\n"
        retstr += f"|{' ' * width}|\n"
        retstr += f"| {self.icon}{' ' * (width - 3)}|\n"  # assume width of icon is 2 chars - len('🏃🏽‍♀️');  doesn't do what you'd epxect
        retstr += f"| {self.kind}{' ' * (width - len(self.kind) - 1)}|\n"
        retstr += f"|{' ' * width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' ' * (width - len(duration_str) - 1)}|\n"
        cal_str = f"{round(self.get_calories(), 1)}"
        retstr += f"| {cal_str} Calories {' ' * (width - len(cal_str) - 11)}|\n"

        retstr += f"|{' ' * width}|\n"
        retstr += f"|{'_' * width}|\n"

        return retstr
    def __eq__(self, other):
        """Returns true if this workout is equal to another workout, false o.w."""
        # the \ breaks up the line
        return type(self) == type(other) and \
                self.start == other.start and \
                self.end == other.end and \
                self.kind == other.kind and \
                self.get_calories() == other.get_calories()


class RunWorkout(Workout):
    cals_per_km = 100

    def __init__(self, start, end, elev = 0, calories = None, route_gps_points = None):
        super().__init__(start, end, calories) #super() calls the parents innit method
        self.icon = '🏃'
        self.kind = 'Running'
        self.elev = elev
        self.route_gps_points = route_gps_points
    def get_elev(self):
        return self.elev
    def set_elev(self, e):
        self.elev = e
    def get_calories(self):
        if self.route_gps_points is not None:
            dist = 0
            lastP = self.route_gps_points[0]
            for p in self.route_gps_points[1: ]:
                dist += gpsDistance(lastP, p)
                lastP = p
            return dist*RunWorkout.cals_per_km
        else:
            return super().get_calories()
    def __eq__(self,other):
        """Returns true if this workout is equal to another workout, false o.w."""
        return super().__eq__(other) and self.elev == other.elev

# w_1 = Workout("Jan 1 2021 3:30PM", "Jan 1 2021 4PM")
# print(w_1)
# rw_2= RunWorkout("Jan 1 2021 3:30PM", "Jan 1 2021 4PM", 300)
# print(rw_2)

# =============================================================================
# EXAMPLE:  RunWorkout overrides get_calories() to use GPS points
# Uses lec18_helpers.py to find the distance between (lat, long) pairs
# =============================================================================

# points are Boston to Newton
# points = [(42.3601,-71.0589),(42.3370,-71.2092)] # (latitude,longitude) pairs
# run1 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:57 PM', 100, route_gps_points=points)
# print(run1)

# =============================================================================
# EXAMPLE: Workouts override __eq__ to provide equality testing
# =============================================================================

# w1 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM', 500)
# w2 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM') # cal are 200 by default
# w3 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM', 100)
#
# rw1 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 100)
# rw2 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 200)
# rw3 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 100)
#
# print(w1 == w2)  # False since only length of workout is the same
# print(w1 == w3)  # False since only length of workout is the same
# print(w2 == w3)  # True since the length and calories are equal
# print(w1 == rw1)  # False since the types of w1 and rw1 are not the same
# print(rw1 == rw2) # False since the elevation is different
# print(rw1 == rw3) # True since the types, workout length, and elev is the same
