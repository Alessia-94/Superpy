#Repository: time repository, 

from dbo.data_base import Data_Base
from models.superpy_time import SuperpyTime #importiamo la classe
import datetime as dt

class Time_repository: #il tempo e uguale per tutti quindi facciamo la classe statica
    superpy_time = None  # abbiamo istanziato il tempo al tempo corrente usando il metodo dt.datetime.now
    
    
    def get_current_time(self):
        time = Data_Base.loadtimeDB()
        for t in time:
            self.superpy_time = SuperpyTime(t[0]) #qua riscriviamo la data dell'excell, e usa la concezione di tempo
