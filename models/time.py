import datetime as dt
class SuperpyTime:
    def __init__(self, current_date):
        self.current_date = dt.datetime.strptime(current_date, "%Y-%m-%d")
    
    def current_date_gt (self, date_to_check):
        return self.current_date > date_to_check
    
    def current_date_lt (self, date_to_check):
        return self.current_date <= date_to_check
    
    def time_delta (self, date_to_check):
        delta = self.current_date - date_to_check
        return delta.days
    
    
        
    
    #date_to_check datadi scadenza
    #lt e gt sono due check , metodi di comparazione current time e piu grande della scadenza?
    #ma il current date e minore alla data di scadena, minore o uguale
    # date time prende linformazione e la trasforma in data
 # data del prodotto di scadenza con il current time gt= current time, lt= per capire se non e scaduto, se non e scaduto calcoliamo il delta. finestra di tempo tra la scadenza e oggi