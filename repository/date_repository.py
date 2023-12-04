#Repository: time repository, 

from dbo.data_base import Data_Base
from models.superpy_time import SuperpyTime 
import datetime as dt

# ..
class Time_repository: 
    superpy_time = None #dichiariamo vuota   

    def __init__(self):
        time = Data_Base.loadtimeDB()
        for t in time:
            self.superpy_time = SuperpyTime(t[0]) #la riga 0 e la carichiamo nel superpy quella con none
        
    def get_current_time(self): # data del csv
        return self.superpy_time

    def set_current_time(self, set_time):
        set_time = dt.datetime.strftime(set_time.current_date, "%Y-%m-%d")
        Data_Base.savetimeDB(set_time) #riscirvere data 
        