from dbo.data_base import Data_Base
from ..models.profit import Profit #importiamo la classe
class Profit_repository:

    profit_table = dict()

    def __init__(self):
        profits = Data_Base.loadprofitDB() #qui prendiamo il puntatore del file
        for line in profits:
            self.profit_table [line[1]] = Profit(line[0], line[1], line[2])#, indicat separatore elementi della lista, con gli index della lista indico quale elemento prendere
            #1 e la chiave del dizionare, poi abbiamo caricato tutti i profit dal db che e il nostro cvs. e abbiamo riempito il dizionario ed e accessibile dagli heandler

