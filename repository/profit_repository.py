#Repository: profit repository, I load here my database and with the data imported I build a dictionary 

from dbo.data_base import Data_Base
from models.profit import Profit 

class Profit_repository:

    profit_table = dict()

    def __init__(self):
        self.load_profit()

# Here I used this method to add new "ID" in case I add a new profit to the list
    def get_max_id(self):
        return len(self.profit_table.values())

# Here I indicate which command the database has to do: load the profit from the database and save the new updated profit in the database    
    def load_profit(self):
        profits = Data_Base.loadprofitDB() # here we indicate the pointer to the file
        self.profit_table.clear()
        for line in profits:
            self.profit_table [line[1]] = Profit(line[0], line[1], line[2]) 

    def save_profits(self, profits):
        Data_Base.saveprofitDB(profits)