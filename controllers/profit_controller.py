from repository.profit_repository import Profit_repository

class Profit_controller:
    profits = dict ()
    profit_repository = Profit_repository() #abbiamo inizializzato il repositori e lo abbiamo caricato tutto 
    
    def __init__(self):
        self.profits = self.profit_repository.profit_table #prendiamo la tabella e li asseniamo al controller, li puoi elaborare. Staimo separando le responsibilita. 

    def get_profit_by_type (self, type):
        if type in self.profits.keys():
            return self.profits.get(type) #type nostro key
        else:
            return None #noi abbiamo un dizionario di profitto. Se abbiamo un tipo nuovo che non vi e nei profitto. gestione degli errori runtime