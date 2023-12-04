#Model: superpy_time this is the class for the time. This class is used to keep track of the time concept in the code.

import datetime as dt

# in the class SuperpyTime I do a check if the string is empty. I am initialising all the data informations of the product as Superpytime. There are some "known" date (buy_date, expiring_date). The date not known is the selling_date. If a product is not sold, I set it as None.
class SuperpyTime:

    current_date = None #....

    def __init__(self, current_date):
        if current_date not in (None, ""): #check if the string is empty
            self.current_date = dt.datetime.strptime(current_date, "%Y-%m-%d").date()
        else:
            self.current_date = None

#We know the buy_date and expired_date of each product. We do not know the selling_date. If the product is not sold, we set it as None.

#Date_to_check = expired_date. Current_date_gt and current_date_lt are two methods that we do as check (comparison method)

#If expired date (date_to_check) doesn’t exist, return current date is always bigger.   
    def current_date_gt (self, date_to_check):
        date_to_check: SuperpyTime 
        if date_to_check is None: return True 
        return self.current_date > date_to_check.current_date
    
#If expired date (date_to_check) exist, the expired date is bigger than the existing date. 
    def current_date_lt (self, date_to_check):
        date_to_check: SuperpyTime 
        if date_to_check is None: return False 
        return self.current_date < date_to_check.current_date

#gte= greater than equal 
    def current_date_gte (self, date_to_check):
        date_to_check: SuperpyTime 
        if date_to_check is None: return True 
        return self.current_date >= date_to_check.current_date
    
#lte= .... 
    
    def current_date_lte (self, date_to_check):
        date_to_check: SuperpyTime 
        if date_to_check is None: return False 
        return self.current_date <= date_to_check.current_date

#If expired date (date_to_check) doesn’t exist, return 0 days as number of days tot he current date (because it doesn't exist)   
    def time_delta (self, date_to_check):
        date_to_check: SuperpyTime 
        if date_to_check is None: return 0
        delta = self.current_date - date_to_check.current_date
        return delta.days 
    
