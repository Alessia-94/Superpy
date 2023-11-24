#Model: superpy_time this is the class for the time. This class is used to keep track of the time concept in the code.

import datetime as dt
class SuperpyTime:
    def __init__(self, current_date):
        if current_date not in (None, ""): #check if the string is empty
            self.current_date = dt.datetime.strptime(current_date, "%Y-%m-%d")
        else:
            self.current_date = None

#We know the buy_date and expired_date of each product. We do not know the selling_date. If the product is not sold, we set it as None.

#Date_to_check = expired_date. Current_date_gt and current_date_lt are two methods that we do as check (comparison method)

#Is current_date > expired_date (date_to_check)? yes ---> product expired

#Is current_date <= expired_date (date_to_check)? no ---> product not expired. In this case, we can calculate the delta, which is the amount of days before the expired date. If the delta is > xx amount of days, we can put it on sale (we do this in the controllers)

    
    def current_date_gt (self, date_to_check):#se una delle due date non esite, quella corrente vince e maggiore
        if date_to_check is None: return True 
        return self.current_date > date_to_check
    
    def current_date_lt (self, date_to_check):
        if date_to_check is None: return False 
        return self.current_date <= date_to_check
    
    def time_delta (self, date_to_check):
        if date_to_check is None: return 0 #numeri di giorni che mancano 0
        delta = self.current_date - date_to_check
        return delta.days #we have to specify delta.days, because we want only the date and not the seconds
    
