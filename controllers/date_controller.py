#Date controller

from repository.date_repository import Time_repository
from models.superpy_time import SuperpyTime
import datetime as dt

# I made a class where we import the current date with the date that I indicate in the csv, this is called get_current_date
class Date_controller:
    time_repository = Time_repository()
    
    def get_current_date(self):
        return self.time_repository.get_current_time()
# here I write two method which allows the advancing and retreat of the time, by adding or removing specific numbers of date set in the main.file
    def advance_days(self, d):
        today: SuperpyTime = self.time_repository.get_current_time()# data che sta nel cvs nel repositoru
        today.current_date += dt.timedelta(days=d) # aggiunta dei gg
        self.time_repository.set_current_time(today)# qui lo saviamo csv set current time nel reposity 

    def retreat_days(self, d):
        today: SuperpyTime = self.time_repository.get_current_time()
        today.current_date -= dt.timedelta(days=d)
        self.time_repository.set_current_time(today)

    def reset_time_to_today(self):
        today = SuperpyTime(dt.date.today().strftime("%Y-%m-%d")) #ogni cosa con set viene riscritto
        self.time_repository.set_current_time(today)

    def get_time_array_in_time_range(self, date1, date2):
        delta = dt.timedelta(days=1)
        date1 = dt.datetime.strptime(date1, "%Y-%m-%d")
        date2 = dt.datetime.strptime(date2, "%Y-%m-%d")
        dates = list()
        while date1 <= date2:
            dates.append(date1)
            date1 += delta
        return dates
                        