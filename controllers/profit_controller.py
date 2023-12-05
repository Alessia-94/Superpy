#Profit controller

from repository.profit_repository import Profit_repository
from models.profit import Profit

#I initialise the profit repository 
class Profit_controller:
    profits = dict ()
    profit_repository = Profit_repository() 
 #I  assign to the controller the profit table from the repository so the controller can handle the data.   
    def __init__(self):
        self.profits = self.profit_repository.profit_table
        
#test to avoid crush in the program. I test that for each type I have a profit
    def get_profit_by_type (self, type):
        if type in self.profits.keys():
            return self.profits.get(type) 
        else:
            return None 
        
#Methods to insert and save a new profit in case I add a new product to the supermarket list, or I need to update it
    def insert_new_profit(self, params):
        new_id = self.profit_repository.get_max_id()
        p = Profit(new_id, params[0], params[1])
        self.profits[params[0]] = p 
        self.save_profits()
        return p
    
    def save_profits(self):
        self.profit_repository.save_profits(self.profits.values())
        
        