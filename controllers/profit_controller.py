#Profit controller

from repository.profit_repository import Profit_repository

# we initialise the profit repository 
class Profit_controller:
    profits = dict ()
    profit_repository = Profit_repository() 
 # we assign to the controller the profit table from the repository so he can handle the data.   
    def __init__(self):
        self.profits = self.profit_repository.profit_table
        
#test to avoid crush in the program. I test that for each type we have a profit
    def get_profit_by_type (self, type):
        if type in self.profits.keys():
            return self.profits.get(type) 
        else:
            return None 
        
        
        
        #noi abbiamo un dizionario di profitto. Se abbiamo un tipo nuovo che non vi e nei profitto. gestione degli errori runtime