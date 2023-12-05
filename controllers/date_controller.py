#Date controller: here we do all the "changes" of time: advance or go back in time, reset time ect.

from repository.date_repository import Time_repository
from models.superpy_time import SuperpyTime
import datetime as dt

# I made a class where we import the current date with the date that I indicate in the csv, this is called get_current_date
class Date_controller:
    time_repository = Time_repository()
    
    def get_current_date(self):
        return self.time_repository.get_current_time()
    
# here I write methods which allows the advancing, retreat of the time, by adding or removing specific numbers of days
    def advance_days(self, d):
        today: SuperpyTime = self.time_repository.get_current_time()# data that is in the csv
        today.current_date += dt.timedelta(days=d) # add xx days
        self.time_repository.set_current_time(today)# I save here the new data in the time repository

    def retreat_days(self, d):
        today: SuperpyTime = self.time_repository.get_current_time()
        today.current_date -= dt.timedelta(days=d)
        self.time_repository.set_current_time(today)

# this method allows to reset the time to the current real date.
    def reset_time_to_today(self):
        today = SuperpyTime(dt.date.today().strftime("%Y-%m-%d")) #ogni cosa con set viene riscritto
        self.time_repository.set_current_time(today)

# function utility: I used to "plot" my graphic using the module Matplot: it gives an array of value in a specific time range
    def get_time_array_in_time_range(self, date1, date2):
        delta = dt.timedelta(days=1)
        date1 = dt.datetime.strptime(date1, "%Y-%m-%d")
        date2 = dt.datetime.strptime(date2, "%Y-%m-%d")
        dates = list()
        while date1 <= date2:
            dates.append(date1)
            date1 += delta
        return dates
                        