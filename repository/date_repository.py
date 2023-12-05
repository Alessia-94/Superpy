#Repository: time repository

from dbo.data_base import Data_Base
from models.superpy_time import SuperpyTime 
import datetime as dt

#I build the list of the data, by taking the data from the database and I build my class. 
class Time_repository: 
    superpy_time = None  

    def __init__(self):
        self.loadtime()

# here I store the time-data that I use
    def get_current_time(self):
        return self.superpy_time

# here I save the time-data. I used only to re-write the data
    def set_current_time(self, set_time):
        set_time = dt.datetime.strftime(set_time.current_date, "%Y-%m-%d")
        Data_Base.savetimeDB(set_time) 
        self.loadtime()
    
# # Here I indicate which command the database has to do: update with the new calculated time-data the info in the csv
    def loadtime (self):
        time = Data_Base.loadtimeDB()
        for t in time:
            self.superpy_time = SuperpyTime(t[0])
        