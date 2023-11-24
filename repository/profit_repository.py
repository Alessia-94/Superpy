#Repository: profit repository, i load here my database and with the data imported I build a dictionary 

from dbo.data_base import Data_Base
from models.profit import Profit 
class Profit_repository:

    profit_table = dict()

    def __init__(self):
        profits = Data_Base.loadprofitDB() # here we indicate the pointer to the file
        for line in profits:
            self.profit_table [line[1]] = Profit(line[0], line[1], line[2]) 